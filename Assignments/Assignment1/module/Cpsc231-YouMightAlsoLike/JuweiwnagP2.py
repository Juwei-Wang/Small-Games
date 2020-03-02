import  numpy as np

input_file = open('rating.txt','r')
lines_rating = input_file.readlines()
input_file.close()
elements = lines_rating[1].split(',')
elements_2 = lines_rating[0].split(':')
name = elements_2[1].rstrip()
elements_number = len(elements)
inttype = []

for i in range(len(elements)):
    value = int(elements[i])
    inttype.append(value)

highest = inttype[0]
highest_index = []
for i in range(len(inttype)):
    mid = inttype[i]
    if 0 < mid and mid > highest:
        highest = inttype[i]
for i in range(len(inttype)):
    if (inttype[i] == highest):
        highest_index.append(i)

lowest = inttype[0]
lowest_index = []
for i in range(len(inttype)):
    mid_2 = inttype[i]
    if 0 < mid_2 and mid_2 < lowest:
        lowest = inttype[i]
for i in range(len(inttype)):
    if (inttype[i] == lowest):
        lowest_index.append(i)

seen_index = []
see_number = 0
for i in range(len(inttype)):
    if inttype[i] != 0:
        see_number = see_number + 1

input_file = open('movies.txt')
lines = input_file.readlines()
input_file.close()

print("Hello: " + name + "!")
print("It looks like your've seen", see_number , "of the 100 movies")
print("Your favourite movies were:")
for i in range(len(highest_index)):
    index_number = highest_index[i]
    highest_index_text = lines[index_number].rstrip()
    print(highest_index_text)
print("Your least favourite movies were:")
for i in range(len(lowest_index)):
    index_number_2 = lowest_index[i]
    lowest_index_text = lines[index_number_2].rstrip()
    print(lowest_index_text)
















