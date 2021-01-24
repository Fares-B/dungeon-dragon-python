from Creature.Player.orc import Orc

from dungeon import Dungeon
# from Room.Active import Active
# from Room.Enemy import Enemy
# from Room.Hall import Hall


def main():
    player = Orc(input("Votre nom : "))
    print("################")
    dungeon = Dungeon(player)

    while True:
        dungeon.create()
        dungeon.action()
        if "o" == input("Voulez vous rejouer ? o/n "):
            dungeon.game_over()
        else:
            break


    # goblin = Goblin()
    # goblin.attack(player_human)
    # slime = Slime()
    # slime.attack(player_human)
    # dragon = Dragon()
    # player.get_bio()
    #
    # player.inventory.gold = 1000
    # player.store.buy_normal_potion(20)
    # player.store.buy_medium_potion(6)
    # player.store.buy_big_potion(2)
    #
    # player.get_bio()

    # goblin.inventory.potion.big = 2
    # dragon.get_bio()
    # dragon.attack(player)
    # dragon.attack(player)
    # dragon.attack(player)
    # dragon.attack(player)
    # player.get_bio()

    # player.store.get_price()
    # player.store.buy_resurrection_potion(1)
    # player.use_resurrection()
    # player.get_bio()
    # player.store.buy_normal_potion()
    # player.store.buy_medium_potion()
    # player.store.buy_big_potion()
    # player.use_normal()
    # player.get_bio()

    # for room in dungeon:
    #     room.action()
    # print(dungeon[0].get_type())


if __name__ == '__main__':
    main()
