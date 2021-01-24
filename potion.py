class Potion:

    def __init__(self):
        self.normal = 0
        self.medium = 0
        self.big = 0
        self.resurrection = 0
        self.normal_care = 30
        self.medium_care = 60
        # self.big_care = self.player.max_life
        self.resurrection_care = 1

    def clear(self):
        self.normal = 0
        self.medium = 0
        self.big = 0

    def update_normal(self, normal=1):
        self.normal += normal

    def update_medium(self, medium=1):
        self.medium += medium

    def update_big(self, big=1):
        self.big += big

    def update_resurrection(self, resurrection=1):
        self.resurrection += resurrection

    def update(self, potion):
        self.normal += potion.normal
        self.medium += potion.medium
        self.big += potion.big
        self.resurrection += potion.resurrection
