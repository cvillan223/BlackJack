import random


def drawCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    randomCard = random.randint(0, len(cards) - 1)
    return cards[randomCard]


def CheckBust(Cards):
    Sum = sum(Cards)
    if Sum > 21:
        if 11 in Cards:
            Cards.remove(11)
            Cards.append(1)
            return Cards
        else:
            return True

    return False


def Dealer():
    DealerCards = [drawCard(), drawCard()]
    if sum(DealerCards) == 21:
        print("BlackJack! Dealer wins!\n")
        return DealerCards

    else:
        while sum(DealerCards) < 17:
            DealerCards.append(drawCard())

    return DealerCards


def CheckWinner(Player, Dealer):

    if sum(Player) == sum(Dealer):
        Dealer.append(drawCard())

    if sum(Player) > sum(Dealer):
        return True
    else:
        return False


def PlayAgain():
    Input = input("Would you like to play again enter y/n: \n").lower()
    if Input == "y":
        return True
    return False


if __name__ == '__main__':

    Play = True
    while Play:
        logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """

        print(logo + "\n")
        CardList = [drawCard(), drawCard()]
        print("Your cards: \n")
        print(CardList)
        DealerCards = Dealer()
        PlayerBust = False

        print("Dealers first card: \n" + str(DealerCards[0]))

        if sum(CardList) == 21:
            print("Player wins blackjack!")
            PlayerBust = True

        while not PlayerBust:
            Hit = input("Enter y/n for hit: \n").lower()
            if Hit == "y":
                CardList.append(drawCard())
                PlayerBust = CheckBust(CardList)
                print("Your cards: " + str(CardList))

                if PlayerBust:
                    print("Bust! You lose\n")
                    PlayerBust = True
            else:
                DealerBust = CheckBust(DealerCards)

                if DealerBust:
                    print("You win! Dealer Bust!\n" + "Dealer's cards: \n" + str(DealerCards))
                    PlayerBust = True
                    break
                elif sum(DealerCards) == 21:
                    print("Dealer wins! Blackjack!")
                    PlayerBust = True

                Winner = CheckWinner(CardList, DealerCards)
                if not Winner:
                    print("You lose! Dealer's cards: \n" + str(DealerCards))
                    PlayerBust = True
                else:
                    print("You win! Dealer's cards: \n" + str(DealerCards))
                    PlayerBust = True

        Play = PlayAgain()

    print("Goodbye!")
