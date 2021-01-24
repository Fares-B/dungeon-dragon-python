from Creature.Player.player import Player


class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        self.race = "human"
