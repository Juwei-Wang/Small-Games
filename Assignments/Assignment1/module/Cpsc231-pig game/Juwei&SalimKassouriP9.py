from random import randint


def roll_player():
    turnScore = 0
    keep = 1
    while keep == 1:
        dice = randint(1, 6)
        if dice == 1:
            print("You rolled a 1!")
            print("Pigged out !")
            turnScore = 0
            keep = 0
        else:
            turnScore = turnScore + dice
            print('You rolled a ', dice)
            enter = input("Do you want to roll again? r=roll or h=hold >")
            if enter == "r":
                keep = 1
            else:
                keep = 0
    print("Your Turn score = ", turnScore)
    return turnScore


def roll_computer():
    turnScore = 0
    while turnScore <= 20:
        dice = randint(1, 6)
        if dice == 1:
            print("Player2 rolled a 1!")
            print("Pigged out!")
            turnScore = 0
            break
        else:
            turnScore = turnScore + dice
            print('Player2 rolled a ', dice)
    else:
        print("Player2 Turn score = ", turnScore)
    return turnScore


def main():
    player1 = 0
    player2 = 0
    while player1 < 100 and player2 < 100:
        up = roll_player()
        player1 += up
        print('Player1 current score is : ', player1)
        print('Player2 current score is : ', player2)
        print('This turn is over.')
        up = roll_computer()
        player2 += up
        print('Player1 current score is : ', player1)
        print('Player2 current score is : ', player2)
        print('This turn is over.')
    print('The game is over.')
    print('Player1 final grade is ', player1)
    print('Player2 final grade is ', player2)
    if player1 > player2:
        print('Player1 is the winner.')
    elif player1 < player2:
        print('Player2 is the winner.')
    else:
        print('Tie game.')


main()
