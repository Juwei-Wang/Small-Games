from random import randint

currentScore = 0
turnScore = 0

while currentScore + turnScore< 100 :
    dice = randint(1, 6)
    if turnScore <= 20:
        if dice == 1:
            print("You rolled a 1! Pig out!")
            print('You turned 0.')
            turnScore = 0
        else:
            turnScore = turnScore + dice
            print('You rolled a ', dice)
    else:
        print("You turned ", turnScore)
        currentScore = currentScore + turnScore
        print('Your current score is', currentScore)
        turnScore = 0

print('Final Score = ', currentScore + turnScore)

if currentScore > 100:
    win = input('Winner!')
