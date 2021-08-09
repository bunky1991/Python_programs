from random import randint

censored_words = ["blah", "blah blah", "player", "unknown"]


class Character:
    #character object
    def __init__(self)->None:
        self.name = None
        self.health = 100
        self.inventoryPack = self.inventory()
        self.alive = True
        self.defence = randint(3, 10)
        self.damage = randint(3, 10)
        self.playerDamage = []
        self.playerDefence = []

    def __str__(self) -> str:
        """
        How the object will be formatted in the output console
        :return: a string with the stats of the player
        """
        return f"{self.name}, HP: {self.health}, items: {self.inventoryPack}"

    #This is so player can see whats in the inventory and it will be numbered aswell
    def Player_Pack_Check(self) -> None:
        """
        Checks the players inventory pack
        :return: doesn't return anything
        """
        for counter, item in enumerate(self.inventoryPack):
            print(counter, item)

    #to check how much health is left after a attack
    def Player_Health_Check(self):
        print("{} has {} health left".format(self.name, self.health))

    #to check is player is alive
    def isAlive(self):
        if self.health > 0:
            self.Player_Health_Check()
        else:
            self.alive = False

    # randomizes the inventory for each player, also removes item that is already been selected
    def inventory(self) -> [str]:
        """
        fills a list with unique values from another list, as  one item is added it removes the item from the first list to ensure no duplicates
        :return: list of str [str]
        """
        inventory_to_use = []
        items = ["Apple", "Sword", "Shield", "Dagger"]

        for item_in_items in range(2):
            if item_in_items <= 2:
                index = randint(0, len(items)) - 1
                inventory_to_use.append(items[index])
                del items[index]
        return inventory_to_use


    # when am item is used to then get the corrisponding action for the item, basic layout
    def item_usage(item, self) -> None:
        """
        :param item: the item the user has chosen to use
        :param self: referencing itself
        :return: None
        """
        if item == "Apple":
            self.health += 20
            self.inventoryPack.remove(item)
            print(f"{self.name} used the {item}")
        elif item == "Sword":
            self.damage += 10
            self.inventorypack.remove(item)
            print(f"{self.name} used the {item}")
        elif item == "Shield":
            self.defence += 10
            self.inventorypack.remove(item)
            print(f"{self.name} used the {item}")
        elif item == "Dagger":
            self.damage += 5
            self.inventorypack.remove(item)
            print(f"{self.name} used the {item}")


    # for game analysis at the end
    def Player_report(self, randdamage, enemy) -> None:
        """
        This is so the over view of the game can be displayed in a plot
        :param randdamage: random generated number from 1-10
        :param enemy: the player thats being attacked
        :return: None
        """
        self.playerDamage.append(self.damage + randdamage)
        self.playerDefence.append(enemy.defence)


playeroneTurn = True

playerOne = Character()
playerTwo = Character()


# define platers name
def player_name(player: Character) -> None:
    """
    This function is to ensure that the players dont enter the same name or a specific name
    :param player: referencing player object
    :return:
    """
    global censored_words
    while player.name == "":
        playerName = str(input("please enter player one's name: "))
        for i in censored_words:
            if playerName == i:
                print("please choose another name")
                playerName = " "
            elif playerName == playerTwo.name or playerName == playerOne.name:
                print("please choose another name")
                playerName = " "
            else:
                player.name = playerName


player_name(playerOne)
player_name(playerTwo)

# this is the random for the attacking
def attack(playerA: Character, playerB: Character) -> None:
    """
    PlayerA will attack player B with a random, but taking in concideration the defence value and current attack
    :param playerA: the player that is attacking
    :param playerB: the player that is being atatcked
    :return: None
    """
    randomdamage = randint(0, 10)
    print(f"random damage: {randomdamage}")
    if playerB.defence > (playerA.damage + randomdamage):
        print(f"{playerB.name} defence over powered {playerA.damage}'s attack")
    else:
        playerB.health -= (playerA.damage - playerB.defence) + randomdamage
    playerB.isAlive()
    playerA.Player_report((randomdamage + playerA.damage), playerB)


# starting of game, if both are alive
while playerOne.alive and playerTwo.alive:
    print(f"Welcome Player One: {playerOne.name} and Player Two: {playerTwo.name}")
    if playeroneTurn:
        playeroneTurn = False
        print(f"{playerOne}")
        print(f"{playerOne.name}'s turn")
        if playerOne.inventoryPack:
            playerOne.Player_Pack_Check()
            # uncomment this line to enable the player to choose which item to use
            userPlayerOne = input("do you want to use an item?  yes or no").lower()
            if userPlayerOne == "yes":
                itemtouse = int(input("which item do you want to use, please enter the number"))
                for item in range(len(playerOne.inventoryPack)):
                    if item == itemtouse:
                        playerOne.item_usage(playerOne.inventoryPack[item])
                        break
                    else:
                        print("ERROR: you entered a invalid number")
            else:
                attack(playerOne, playerTwo)
        else:
            attack(playerOne, playerTwo)
    else:
        playeroneTurn = True
        print(f"{playerTwo}")
        print(f"{playerTwo.name}'s turn")
        if playerTwo.inventoryPack:
            playerTwo.Player_Pack_Check()

            # uncomment this line to enable the player to choose which item to use
            userPlayerTwo = input("do you want to use an item?  yes or no").lower()
            if userPlayerTwo == "yes":
                itemtouse = int(input("which item do you want to use, please enter the number"))
                for item in range(len(playerTwo.inventoryPack)):
                    if item == itemtouse:
                        playerTwo.item_usage(playerTwo.inventoryPack[item])
                        break
                    else:
                        print("ERROR: you entered a invalid number")
            else:
                attack(playerTwo, playerOne)
        else:
            attack(playerTwo, playerOne)


def gameCondictionCheck():
    if playerOne.isAlive():
        print(f"{playerOne.name} has won, with {playerOne.health} health left")
    elif playerTwo.isAlive():
        print(f"{playerTwo.name} has won, with {playerTwo.health} health left")
    else:
        print("ERROR: run game again")


gameCondictionCheck()

print("analysis of the game")

if len(playerOne.playerDamage) > len(playerTwo.playerDefence):
    x = len(playerOne.playerDamage) - len(playerTwo.playerDefence)
    print(f"new list length {x}")
    playerOne.playerDamage.remove(x)

import matplotlib.pyplot as plt

plt.scatter(playerOne.playerDamage, playerTwo.playerDefence)
plt.show()
