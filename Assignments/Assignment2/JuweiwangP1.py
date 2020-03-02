input_file = open("cpsc231-lexicon.txt")
line_words = input_file.readlines()
input_file.close()
line_without_new = []
word = input()

for i in range(len(line_words)):
    line_without = line_words[i].rstrip()
    line_without_new.append(line_without)

popular_rank = 0
for i in range(len(line_without_new)):
    if word == line_without_new[i]:
        popular_rank = i + 1

word1 = word.lower()
ic = 0
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(alpha)):
    if word1 == alpha[i]:
        ic = i
print(ic)
print(word1)

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

if str(popular_rank)[len(str(popular_rank)) - 1] == "1":
    popular_rank_str = str(popular_rank) + "st"
if str(popular_rank)[len(str(popular_rank)) - 1] == "2":
    popular_rank_str = str(popular_rank) + "nd"
if str(popular_rank)[len(str(popular_rank)) - 1] == "3":
    popular_rank_str = str(popular_rank) + "rd"
else:
    popular_rank_str = str(popular_rank) + "th"


if popular_rank == 0:
    print("""According to our lexicon, """, """ " """, word, """ " """, "is not in the most 4000"
    " common words of contemporary American English. """)
else:
    print("""According to our lexicon, """, """ " """, word, """ " """, "is the", popular_rank_str,
    " most common word in contemporary American English . """)

print("It contains the following letters :")
print(string_vocabulary)