from Room.room import Room
from inventory import Inventory
from random import randint


class Active(Room):

    def __init__(self):
        super().__init__()
        self.set_type("Active")
        self.treasures = Inventory()
        self.create()

    def create(self):
        self.treasures.update_gold(randint(100, 500))
        r = randint(1, 10)
        if 1 == r:
            self.treasures.potion.update_resurrection(2)
        elif r % 3 == 0:
            self.treasures.potion.update_resurrection()

        r = randint(1, 2)
        if 1 == r:
            self.treasures.potion.update_big(randint(1, 3))
        self.treasures.potion.update_medium(randint(2, 5))
        self.treasures.potion.update_normal(randint(4, 12))

    def action(self):
        super().action()
        pass
#       drop a item or gold
