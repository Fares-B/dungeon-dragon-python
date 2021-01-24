from Creature.Monster.monster import Monster
from random import randint


class Goblin(Monster):

    def __init__(self):
        super().__init__()
        self.race = "Goblin"
        self.set_life(randint(20, 30))
        self.set_strength(randint(4, 8))
        self.max_gold = 30
        self.setup()
