import random
import math

input_file = open("cpsc231-lexicon.txt")
line_words = input_file.readlines()
input_file.close()
line_without_new = []


for i in range(len(line_words)):
    line_without = line_words[i].rstrip()
    line_without_new.append(line_without)

word = line_without_new[random.randrange(0,len(line_without_new))]


popular_rank = 0
for i in range(len(line_without_new)):
    if word == line_without_new[i]:
        popular_rank = i + 1

word1 = word.lower()
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
word_boolean = []

for i in range (26):
    word_boolean.append(False)
word_list = list(word1)
alpha_index = []

for i in range(len(word_list)):
    alpha_number = 0
    while alpha[alpha_number] != word_list[i]:
        alpha_number += 1
    alpha_index.append(alpha_number)


string_vocabulary = ""

for i in range(len(alpha_index)):
    word_boolean[alpha_index[i]] = True

index_array = []

for i in range(len(word_boolean)):
    if word_boolean[i]:
        index_array.append(i)

for i in range(len(index_array)):
    string_vocabulary = string_vocabulary + " " + alpha[index_array[i]]

word_guess = input()


""" 提取输入的信息的引索"""
guess_alpha_index = 0
for i in range(len(alpha)):
    if word_guess == alpha[i]:
        guess_alpha_index = i

for







