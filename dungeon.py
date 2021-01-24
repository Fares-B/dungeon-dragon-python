from Room.hall import Hall
from Room.active import Active
from Room.enemy import Enemy
from Room.boss import Boss
from Room.room import Room
from random import randint


class Dungeon:

    def __init__(self, player, nb_room=4):
        self.player = player
        self.nb_room = nb_room
        self.rooms = []
        self.reset = False

    def add_room(self, room):
        if isinstance(room, Room):
            self.rooms.append(room)

    def create(self):
        for i in range(self.nb_room):
            r = randint(1, 3)
            if r == 1:
                self.add_room(Active())
            if r == 2:
                self.add_room(Enemy())
            if r == 3:
                self.add_room(Hall())
        self.add_room(Boss())

    def game_over(self):
        self.clear()
        self.player.inventory.potion.update_resurrection()
        self.player.use_resurrection()
        print("\n\n\n\n\n\nNew Game ! \n\n")
        print("Vous pouvez garder votre ancien inventaire !\n\n")

    def action(self):
        for index, room in enumerate(self.rooms):
            if not self.reset:
                input()
                self.player.get_bio()
                print("\n\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")
                print(f"{self.player.name} vous entrez dans la salle n°{index + 1}, elle est de type {room.type}")
                if isinstance(room, Enemy):
                    print(f"{room.number} enemie(s)")
                    room.spawn()
                    for monster in room.monsters:
                        monster.get_bio()
                        self.player.action(monster)
                        if self.player.dead:
                            print(f"{self.player.name} est mort contre {monster.name}")
                            self.reset = True
                            break
                elif isinstance(room, Active):
                    print("Vous récuperez de la salle aux trésors : ")
                    room.treasures.get_info()
                    self.player.inventory.drop(room.treasures)
                else:
                    print("Vous vous baladez tranquillement jusqu'à atteindre la prochaine salle")

    def clear(self):
        self.reset = False
        self.rooms.clear()
