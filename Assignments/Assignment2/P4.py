import random
import stddraw
import sys
import math
import problemfour

problemfour.set_the_scale()

input_file = open("cpsc231-lexicon.txt")

line_words = input_file.readlines()

input_file.close()

line_without_new = []

"""Apply the words in Txt """
for i in range(len(line_words)):
    line_without = line_words[i].rstrip()
    line_without_new.append(line_without)


"""Claim the principles of the orders """
word_array =[]
word_array_index = []
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

"To make sure there are at least 4 letters in the word"
word = ""
while len(word) < 4:

    """Select the word"""
    word1 = line_without_new[random.randrange(0, len(line_without_new))]

    word = word1.lower()

"""Split the word into array"""
for i in range(len(word)):
    single = str(word[i])
    word_array.append(single)
    """word_array = ['a', 'p', 'p', 'l', 'e']"""

"""Calculate the letter orders"""
for i in range(len(word_array)):
    for j in range(len(alpha)):
        if word_array[i] == alpha[j]:
            index = j
            word_array_index.append(index)
    """word_array_index = [0, 15, 15, 11, 4]"""


"""Create an array for changing and printing"""
result = []
string_result = ""
for i in range (len(word_array)):
    result += ["-"]
    """result = [-, -, -, - ,-]"""

word_guess_index = []

"""To detect the game conditions"""
decision_to_continue = False
for i in range(len(result)):
    if result[i] == "-":
        decision_to_continue = True

array_store =[]

times = 8

print("welcome to CPSC 231 Console Hangman!")
print()
print("The secret word looks like ")


already_guess = ""

while decision_to_continue:

    if already_guess != "":
        print("Your bad guesses so far:" ,already_guess)

    print("You have", times , "gusses remaining")


    word_guess = input("what's your next guess ?")

    word_guess_index = []
    for i in range(len(word_array)):
        if word_guess == word_array[i]:
            word_guess_index.append(i)
        """input = p   word_guess_index = [1,2]"""

    for i in range(len(word_guess_index)):
        result[word_guess_index[i]] = alpha[word_array_index[word_guess_index[i]]]

    if word_guess_index ==[]:
        already_guess = already_guess + " " + word_guess
        print("Sorry, there is no", """ " """, word_guess, """ " """)
        print()
        times = times - 1


    else:
        print("nice guess !")
        print()

    if times <= 7:
        problemfour.set_the_head()
    if times <= 6:
        problemfour.set_the_torso()
    if times <= 5:
        problemfour.set_the_left_arm()
    if times <= 4:
        problemfour.set_the_right_arm()
    if times <= 3:
        problemfour.set_the_left_leg()
    if times <= 2:
        problemfour.set_the_right_leg()
    if times <= 1:
        problemfour.set_the_gallows()
    if times <= 0:
        problemfour.set_the_face()

    if word_guess_index != []:
        string_result = ""
        for i in range(len(result)):
            string_result += " " + result[i]
    else:
        string_result = ""
        for i in range(len(result)):
            string_result += " " + result[i]

    x = "Your bad guesses so far:" + already_guess
    y = "The secret word looks like: " + string_result

    stddraw.setFontSize(30)
    stddraw.text(6, 11, x)
    stddraw.text(6, 9, y)


    problemfour.std_show()

    stddraw.clear()


    decision_to_continue = False
    for i in range(len(result)):
        if result[i] == "-":
            decision_to_continue = True

    if decision_to_continue == False:
        stddraw.text(6, 11, "Congratulation! You win the game !")
        print("Congratulation!")
        print("You guess the secret word:",word1)
        exit()
    if times >= 1 and decision_to_continue == True:
        print("The secret word looks like: ", string_result)

    if times < 1 and decision_to_continue == True:
        stddraw.text(6, 11, "The game is over !")
        problemfour.std_show()
        print("You lose the game! The word is :",word1)
        exit()
