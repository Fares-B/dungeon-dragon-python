from potion import Potion
from termcolor import colored


class Inventory:

    def __init__(self):
        self.gold = 0
        self.potion = Potion()

    def update_gold(self, gold):
        self.gold += gold

    def drop(self, inventory):
        self.update_gold(inventory.gold)
        self.potion.update(inventory.potion)
        inventory.clear()

    def clear(self):
        self.gold = 0
        self.potion.clear()

    def get_info(self):
        print(colored(f"{self.gold} gold, "
                      f"Potions: {self.potion.normal} normal,"
                      f" {self.potion.medium} medium,"
                      f" {self.potion.big} big,"
                      f" {self.potion.resurrection} resurrection.", 'green'))
