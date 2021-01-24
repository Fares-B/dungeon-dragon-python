from Creature.creature import Creature
from store import Store


class Player(Creature):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.store = Store(self)

    def use(self, potion, care):
        self.inventory.get_info()
        if potion < 0:
            print("Plus de potion de ce type")
        elif self.life == self.max_life:
            print(f"{self.name}  vous êtes déjà au maximum de vos points de vie "
                  f"{self.max_life}/{self.max_life}")
        else:
            if self.dead and self.inventory.potion.resurrection_care == care:
                self.dead = False
                care = self.max_life
                print(f"{self.name} revient à la vie !")
            if self.dead is False:
                self.set_life(care + self.life)
                if self.life > self.max_life:
                    self.set_life(self.max_life)
                print(f"{self.name} regagne {care} points de vie.")
            return potion-1
        return potion

    def use_normal(self):
        self.inventory.potion.normal = self.use(self.inventory.potion.normal, self.inventory.potion.normal_care)

    def use_medium(self):
        self.inventory.potion.medium = self.use(self.inventory.potion.medium, self.inventory.potion.medium_care)

    def use_big(self):
        self.inventory.potion.big = self.use(self.inventory.potion.big, self.max_life)

    def use_resurrection(self):
        self.inventory.potion.resurrection = self.use(
            self.inventory.potion.resurrection, self.inventory.potion.resurrection_care
        )

    def get_options(self):
        options = {"a": "attack"}
        if self.inventory.potion.normal > 0:
            options["1"] = "normal heal"
        else:
            options["6"] = "buy normal heal"
        if self.inventory.potion.medium > 0:
            options["2"] = "medium heal"
        else:
            options["7"] = "buy medium heal"
        if self.inventory.potion.big > 0:
            options["3"] = "big heal"
        else:
            options["8"] = "buy big heal"
        if self.inventory.potion.resurrection > 0:
            options["4"] = "resurrection"
        else:
            options["9"] = "buy resurrection"
        return options

    def action(self, monster):
        while monster.dead is False and self.dead is False:
            options = self.get_options()
            print("Voici les choix qui s'offre à vous : ", options)
            choice = input("Que voulez vous faire ? ")
            if choice in options:
                if choice == "a":
                    self.attack(monster)
                    monster.get_stats()
                    monster.attack(self)
                elif "1" == choice:
                    self.use_normal()
                elif "2" == choice:
                    self.use_medium()
                elif "3" == choice:
                    self.use_big()
                elif "4" == choice:
                    self.use_resurrection()
                elif "6" == choice:
                    self.store.buy_normal_potion()
                elif "7" == choice:
                    self.store.buy_medium_potion()
                elif "8" == choice:
                    self.store.buy_big_potion()
                elif "9" == choice:
                    self.store.buy_resurrection_potion()
                self.get_stats()
                # le get_stats n'est pas à jour
