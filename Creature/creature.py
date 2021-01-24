from inventory import Inventory
from termcolor import colored


class Creature:

    def __init__(self):
        self.life = 100
        self.max_life = self.life
        self.strength = 10
        self.agility = 14
        self.race = "creature"
        self.name = self.race
        self.inventory = Inventory()
        self.dead = False

    def set_life(self, life):
        self.life = life

    def get_life(self):
        return f"{self.life}/{self.max_life}"

    def set_strength(self, strength):
        self.strength = strength

    def get_race(self):
        return self.race

    def damage(self, strength):
        self.set_life(self.life - strength)
        if self.life <= 0:
            self.set_life(0)
            self.dead = True

    def attack(self, creature):
        if self.life <= 0:
            print(colored(f"{self.name} vous êtes mort, vous ne pouvez pas attaquer !", 'red'))
        elif creature.life > 0:
            creature.damage(self.strength)
            print(colored(f"{self.name} inflige {str(self.strength)} à {creature.name}", 'cyan'))

        else:
            print(colored("Vous ne pouvez plus attaquer, la cible est déjà morte", 'red'))
        if creature.dead is True:
            # if not isinstance(self, Monster): # circular import
            if not hasattr(self, 'monster'):
                print(colored(f"{self.name} loot le butin de {creature.name}", 'magenta'))
                self.inventory.drop(creature.inventory)

    def get_bio(self):
        print(colored(f"\n***** BIO *****\n\n"
                      f"Nom : {self.name}\n"
                      f"Race : {self.get_race()}\n"
                      f"PV : {self.get_life()}\n"
                      f"ATK : {str(self.strength)}\n"
                      f"AGI : {str(self.agility)}\n", 'green'))
        self.inventory.get_info()
        print(colored("***** --- *****\n", 'green'))

    def get_stats(self):
        print(colored(f"{self.name}, {self.get_life()} pv", 'yellow'))
