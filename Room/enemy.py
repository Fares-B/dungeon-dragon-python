from Room.room import Room
from Creature.Monster.goblin import Goblin
from Creature.Monster.slime import Slime
from Creature.Player.human import Human
from Creature.Player.orc import Orc
from random import randint
from faker import Faker


class Enemy(Room):

    def __init__(self):
        # super().__init__()
        self.set_type("Enemy")
        self.monsters = []
        self.number = randint(1, 3)

    @staticmethod
    def random_monster():
        r = randint(1, 12)
        faker = Faker()
        if r == 11:
            return Human(faker.name())
        elif r == 12:
            return Orc(faker.name())
        elif r % 2 == 0:
            return Slime()
        else:
            return Goblin()

    def spawn(self):
        for i in range(self.number):
            self.add_monster(self.random_monster())

    def add_monster(self, monster):
        self.monsters.append(monster)
