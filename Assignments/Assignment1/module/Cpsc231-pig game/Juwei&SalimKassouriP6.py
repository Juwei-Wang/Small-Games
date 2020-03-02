from random import randint
import sys

roll = int(sys.argv[1]) or 100

currentScore = roll
turnScore = 0
print('Enter current score:', roll)

while currentScore+turnScore < 100:
    dice = randint(1, 6)
    if turnScore <= 20:
        if dice == 1:
            print("You rolled a  1!")
            print("Pigged out!")
            print("Turn score =  0")
            print('New total score =', currentScore)
            turnScore = 0
        else:
            turnScore = turnScore + dice
            print('You rolled a ', dice)
    else:
        print("Turn score = ", turnScore)
        currentScore = currentScore + turnScore
        print('New total score =', currentScore)
        turnScore = 0

print('Turn score =',turnScore)
print('New total score = ', currentScore+turnScore)

