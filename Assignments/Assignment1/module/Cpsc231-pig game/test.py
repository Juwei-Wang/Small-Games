input_file =open('movies.txt')
lines = input_file.readlines()
input_file.close()
for line_of_text in lines:
    line_without_newline = line_of_text.rstrip()
    elements = line_without_newline.split(',')
    city = elements[0]
    print(city, 'is at', ' and ',)