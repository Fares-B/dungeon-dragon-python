class Store:

    def __init__(self, player):
        self.player = player
        self.potion_price = {"normal": 5, "medium": 10, "big": 15, "resurrection": 200}

    def get_price(self):
        print("\n*****  Store  *****")
        print("potion :")
        for k in self.potion_price:
            print(f"\t{k}: {self.potion_price[k]} gold")
        print("")

    def possible_to_buy(self, potion, number):
        if self.player.inventory.gold >= self.potion_price[potion] * number:
            price = -1*(self.potion_price[potion] * number)
            print(f"{self.player.name} vient d'acheter {number} potion(s), {price} gold.")
            self.player.inventory.update_gold(price)
            return True
        missing_gold = -1 * (self.player.inventory.gold - self.potion_price[potion] * number)
        print(f"Pas assez de fonds, manque {missing_gold} gold")
        return False

    def buy_normal_potion(self, number=1):
        if self.possible_to_buy("normal", number):
            self.player.inventory.potion.update_normal(number)

    def buy_medium_potion(self, number=1):
        if self.possible_to_buy("medium", number):
            self.player.inventory.potion.update_medium(number)

    def buy_big_potion(self, number=1):
        if self.possible_to_buy("big", number):
            self.player.inventory.potion.update_big(number)

    def buy_resurrection_potion(self, number=1):
        if self.possible_to_buy("resurrection", number):
            self.player.inventory.potion.update_resurrection(number)
