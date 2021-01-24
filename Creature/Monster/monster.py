from Creature.creature import Creature
from random import randint
from faker import Faker


class Monster(Creature):

    def __init__(self):
        super().__init__()
        self.race = "Monster"
        self.max_gold = 10
        self.monster = True

    def setup(self):
        self.max_life = self.life
        faker = Faker()
        self.name = faker.name()
        self.inventory.update_gold(randint(round(self.max_gold * 0.8), self.max_gold))
        # 1 chance sur 100 d'obtenir un monstre rare
        if 1 == randint(1, 100):
            self.race = "Gold " + self.race
            self.inventory.update_gold(randint(round(self.max_gold * 2.5 * 0.8), round(self.max_gold * 2.5)))
        # 1 chance sur 5 d'obtenir une potion
        if 1 == randint(1, 5):
            self.inventory.potion.normal = 1
        if 1 == randint(1, 20):
            self.inventory.potion.medium = 1
        if 1 == randint(1, 50):
            self.inventory.potion.big = 1
