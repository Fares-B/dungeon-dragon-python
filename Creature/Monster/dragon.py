from Creature.Monster.monster import Monster
from random import randint


class Dragon(Monster):

    def __init__(self):
        super().__init__()
        self.race = "Dragon"
        self.set_life(randint(350, 400))
        self.set_strength(randint(40, 80))
        self.max_gold = 150
        self.setup()
        self.inventory.potion.update_resurrection(1)
        self.inventory.potion.update_normal(6)
        self.inventory.potion.update_medium(3)
        self.inventory.potion.update_big(2)
