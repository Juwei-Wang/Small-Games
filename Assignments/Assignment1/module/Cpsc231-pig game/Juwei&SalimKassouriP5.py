import sys
import random



def rolling_one_round():
    global value1
    value1 = 0
    global total
    total = 0
    while (value1 != 1 and total < 20):
        value1 = random.randrange(1, 7)
        print('rolled a', value1)
        total = total + value1
        if (value1 == 1):
            print('Pigged out!')
            print('Turn score =',"0")
    if (total >= 20):
        print('Turn score =', total)

rolling_one_round()