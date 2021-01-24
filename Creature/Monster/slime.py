from Creature.Monster.monster import Monster
from random import randint


class Slime(Monster):

    def __init__(self):
        super().__init__()
        self.race = "Slime"
        self.set_life(randint(7, 20))
        self.set_strength(randint(2, 5))
        self.max_gold = 17
        self.setup()
