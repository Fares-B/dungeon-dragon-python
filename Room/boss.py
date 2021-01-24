from Creature.Monster.dragon import Dragon
from Room.enemy import Enemy


class Boss(Enemy):

    def __init__(self):
        super().__init__()
        self.type = "Boss"
        self.number = 1

    def spawn(self):
        self.add_monster(Dragon())

    def action(self):
        super().action()
        pass
