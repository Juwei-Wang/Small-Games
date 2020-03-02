import sys
import random

value1 = 0
playerone_ture_total = 0
playertwo_ture_total = 0
playerone_total = 0
playertwo_total = 0
strategy_number = 0
strategy_store = 0



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
            print('Turn score =', playerone_ture_total)
        if (value1 != 1 and playerone_ture_total >= 20):
            print('Turn score =', playerone_ture_total)

def keep_playing():
    global playerone_total
    global playerone_ture_total
    global value1
    while (playerone_total < 100):
        rolling_playerone_round()
        playerone_total = playerone_total + playerone_ture_total
        playerone_ture_total = 0
        value1 = 0
        print('New total score =',playerone_total)
        if (playerone_total > 80):
            computer_strategy()

def computer_strategy():
    global  value1
    global  playerone_total
    global  strategy_number
    global  strategy_store
    while (playerone_total > 80):
        while (value1 != 1 and playerone_total < 100):
            value1 = random.randrange(1, 7)
            print('rolled a', value1)
            playerone_total = playerone_total + value1
            strategy_number = strategy_number + value1
            strategy_store  = strategy_store + value1
            if (value1 == 1):
                print('Pigged out!')
                print('Turn score = 0')
                value1 = 0
                playerone_total = playerone_total - strategy_number
                print('New total score =', playerone_total)
                strategy_number = 0
            if (playerone_total >= 100 ):
                print('Turn score =', strategy_number)
                print('New total score =', playerone_total)
                strategy_number = 0

keep_playing()