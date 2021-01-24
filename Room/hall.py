from Room.room import Room


class Hall(Room):

    def __init__(self):
        super().__init__()
        self.set_type("Hall")
