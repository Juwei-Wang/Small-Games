import sys
import random

value1 = 0
value2 = 0
playerone_ture_total = 0
playertwo_ture_total = 0
playerone_total = 0
playertwo_total = 0
strategy_number = 0
strategy_store = 0
strategy_number2 = 0
strategy_store2 = 0


def rolling_playerone_round():
    global value1
    global playerone_ture_total
    while (value1 != 1 and playerone_ture_total < 20):
        value1 = random.randrange(1, 7)
        print('rolled a', value1)
        playerone_ture_total = playerone_ture_total + value1
        if (value1 == 1):
            playerone_ture_total = 0
            print('Pigged out!')
            print('Total turn score =', playerone_ture_total)
        if (value1 != 1 and playerone_ture_total >= 20):
            print('Total turn score =', playerone_ture_total)

def keep_playing():
    global playerone_total
    global playerone_ture_total
    global playertwo_total
    global value1
    if (playerone_total <= 80):
        print("Player One's score :", playerone_total)
        print("Player Two's score :", playertwo_total)
        print("It's Player One's turn")
        rolling_playerone_round()
        playerone_total = playerone_total + playerone_ture_total
        playerone_ture_total = 0
        value1 = 0


def computer_strategy():
    global  value1
    global  playerone_total
    global  strategy_number
    global  strategy_store
    global  playertwo_total
    if (playerone_total > 80):
        print("Player One's score :", playerone_total)
        print("Player Two's score :", playertwo_total)
        print("It's Player One's turn")
        while (value1 != 1 and playerone_total < 100):
            value1 = random.randrange(1, 7)
            print('rolled a', value1)
            playerone_total = playerone_total + value1
            strategy_number = strategy_number + value1
            strategy_store  = strategy_store + value1
            if (value1 == 1):
                print('Pigged out!')
                print('Total turn score = 0')
                strategy_number = 0
                playerone_total = playerone_total - strategy_store
            if (playerone_total >= 100 ):
                print('Total turn score =', strategy_number)
                strategy_number = 0

def rolling_playertwo_round():
    global value2
    global playertwo_ture_total
    while (value2 != 1 and playertwo_ture_total < 20):
        value2 = random.randrange(1, 7)
        print('rolled a', value2)
        playertwo_ture_total = playertwo_ture_total + value2
        if (value2 == 1):
            playertwo_ture_total = 0
            print('Pigged out!')
            print('Total turn score =', playertwo_ture_total)
        if (value2 != 1 and playertwo_ture_total >= 20):
            print('Total turn score =', playertwo_ture_total)

def keep_playing2():
    global playertwo_total
    global playertwo_ture_total
    global playerone_total
    global value2
    if (playertwo_total <= 80):
        print("Player One's score :", playerone_total)
        print("Player Two's score :", playertwo_total)
        print("It's Player Two's turn")
        rolling_playertwo_round()
        playertwo_total = playertwo_total + playertwo_ture_total
        playertwo_ture_total = 0
        value2 = 0


def computer_strategy2():
    global  value2
    global  playertwo_total
    global  strategy_number2
    global  strategy_store2
    global  playerone_total
    if (playertwo_total > 80):
        print("Player One's score :", playerone_total)
        print("Player Two's score :", playertwo_total)
        print("It's Player Two's turn")
        while (value2 != 1 and playertwo_total < 100):
            value2 = random.randrange(1, 7)
            print('rolled a', value2)
            playertwo_total = playertwo_total + value2
            strategy_number2 = strategy_number2 + value2
            strategy_store2  = strategy_store2 + value2
            if (value2 == 1):
                print('Pigged out!')
                print('Total turn score = 0')
                strategy_number2 = 0
                playertwo_total = playertwo_total - strategy_store
            if (playertwo_total >= 100 ):
                print('Total turn score =', strategy_number2)
                strategy_number2 = 0



def play_others():
    global playerone_total
    global playertwo_total
    global value1
    global value2
    while (playerone_total < 100 and playertwo_total < 100):
        if (playerone_total > 80):
            computer_strategy()
            value1 = 0
            if (playerone_total >= 100):
                print("Final score:", playerone_total, " VS ", playertwo_total)
                print("Player One wins !")
                breakpoint()
        if (playerone_total <= 80):
            keep_playing()
            if (playerone_total >= 100):
                print("Final score:", playerone_total, " VS ", playertwo_total)
                print("Player One wins !")
                breakpoint()
        if (playertwo_total > 80):
            computer_strategy2()
            value2 = 0
            if (playertwo_total >= 100):
                print("Final score:", playerone_total, " VS ", playertwo_total)
                print("Player Two wins !")
                breakpoint()
        if (playertwo_total <= 80):
            keep_playing2()
            if (playertwo_total >= 100):
                print("Final score:", playerone_total, " VS ", playertwo_total)
                print("Player Two wins !")
                breakpoint()



play_others()