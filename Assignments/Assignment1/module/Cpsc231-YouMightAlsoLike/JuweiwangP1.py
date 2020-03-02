import sys
import random

enter = input("What's your name ?")
print("Hi,", enter,"!")

print("Please tell us your favourite movies using the following scale:")
print("0 = Never seen it")
print("1 = It was terrible")
print("2 = Didn't like it")
print("3 = It was OK")
print("4 = liked it")
print("5 = It was awesome")
input_file = open('movies.txt')
lines = input_file.readlines()
input_file.close()

output_file = open('rating.txt', 'w')
num_lines = len(lines)
output_file.write( "User name :" + enter)
output_file.write('\n')
last = num_lines - 1

for i in range(last):
    lines_of_text = lines[i]
    lines_without_newline = lines_of_text.rstrip() + "? "
    enter = input(lines_without_newline)
    output_file.write(enter + ",")

last_lines_of_text = lines[num_lines - 1]
last_lines_of_text_without = last_lines_of_text.rstrip() + "? "
enter2 = input(last_lines_of_text_without)
output_file.write(enter2)

print("Thank you!")
print("your rating were saved to ratings.txt")

output_file.close()