from Creature.Player.player import Player


class Orc(Player):

    def __init__(self, name):
        super().__init__(name)
        self.race = "orc"
        self.max_life = 120
        self.life = 120
        self.strength = 200
        self.agility = 7
