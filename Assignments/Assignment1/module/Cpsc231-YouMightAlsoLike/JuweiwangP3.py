input_file = open('cpsc231-ratings.txt', 'r')
lines_rating = input_file.readlines()
input_file.close()
rating_array = []
add_claculate_array = []
input_file = open('cpsc231-movies.txt')
lines = input_file.readlines()
input_file.close()
for i in range (len(lines)):
    add_claculate_array = add_claculate_array + [0]


"""find the popularity movies array"""
for i in range(len(lines_rating)):
    if i < ((len(lines_rating) - 1) / 2):
        elements = lines_rating[(i * 2) + 1].split(',')
        add_value = []
        for j in range(len(elements)):
            value = int(elements[j])
            add_value.append(value)
        for d in range (len(add_value)):
            if (add_value[d] != 0):
                add_claculate_array[d] = add_claculate_array[d] + 1
store_number_popular = []
store_number_least_popular = []
store_number_popular = sorted(add_claculate_array)

"""find the most popular movies"""
boolean = []
highest_movies_array = []
highest_movies_score_array = []
index = 0

for i in range(len(add_claculate_array)):
    boolean += [False]

for i in range(5):

    index = 0

    while(boolean[index] == True):
        index = index + 1
    store_numnber = add_claculate_array[index]

    for z in range(len(add_claculate_array)):
        if (add_claculate_array[z] >= store_numnber and boolean[z] == False):
            store_numnber = add_claculate_array[z]
            index = z

    boolean[index] = True
    highest_movies_array.append(store_numnber)
    highest_movies_score_array.append(index)

"""find the least popular movies"""
boolean = []
lowest_movies_array = []
lowest_score_array = []
index = 0

for i in range(len(add_claculate_array)):
    boolean += [False]

for i in range(5):

    index = 0

    while(boolean[index] == True):
        index = index + 1
    store_numnber = add_claculate_array[index]

    for z in range(len(add_claculate_array)):
        if (add_claculate_array[z] <= store_numnber and boolean[z] == False):
            store_numnber = add_claculate_array[z]
            index = z

    boolean[index] = True
    lowest_movies_array.append(store_numnber)
    lowest_score_array.append(index)

"""find average number array of the movies that student view """
see_number_array = []

for i in range(len(lines_rating)):
    if i < ((len(lines_rating) - 1) / 2):
        elements = lines_rating[(i * 2) + 1].split(',')
        add_value = []
        for j in range(len(elements)):
            value = int(elements[j])
            add_value.append(value)
            see_number = 0
        for d in range (len(add_value)):
            if (add_value[d] != 0):
                see_number = see_number + 1
        see_number_array.append(see_number)


"""find average rating for every movie except for no seeing"""
average_times = []
student_rating_array = []
average_rating = []
for i in range(len(lines)):
    average_times = average_times + [0]

for i in range (len(lines)):
    student_rating_array = student_rating_array + [0]

for i in range(len(lines)):
    average_rating = average_rating + [0]


for i in range(len(lines_rating)):

    if i < ((len(lines_rating) - 1) / 2):
        elements = lines_rating[(i * 2) + 1].split(',')
        add_value = []

        for j in range(len(elements)):
            value = int(elements[j])
            add_value.append(value)

        for d in range(len(add_value)):

            if (add_value[d] != 0):
                student_rating_array[d] = student_rating_array[d] + add_value[d]
                average_times[d] = average_times[d] + 1

for i in range(len(average_rating)):
    average_rating[i] = student_rating_array[i] / average_times[i]

"""find the highest rating movies"""
boolean = []
highest_rating_array = []
highest_rating_movies_array = []
index = 0

for i in range(len(average_rating)):
    boolean += [False]

for i in range(5):

    index = 0

    while(boolean[index] == True):
        index = index + 1
    store_numnber = average_rating[index]

    for z in range(len(average_rating)):
        if (average_rating[z] >= store_numnber and boolean[z] == False):
            store_numnber = average_rating[z]
            index = z

    boolean[index] = True
    highest_rating_array.append(store_numnber)
    highest_rating_movies_array.append(index)

"""find the most lowest rated array"""
boolean = []
lowest_rating_array = []
lowest_rating_movies_array = []
index = 0

for i in range(len(average_rating)):
    boolean += [False]

for i in range(5):

    index = 0

    while(boolean[index] == True):
        index = index + 1
    store_numnber = average_rating[index]

    for z in range(len(average_rating)):
        if (average_rating[z] <= store_numnber and boolean[z] == False):
            store_numnber = average_rating[z]
            index = z

    boolean[index] = True
    lowest_rating_array.append(store_numnber)
    lowest_rating_movies_array.append(index)

"""find average rating for every movie except for no seeing"""
average_times = []
student_rating_array = []
average_rating = []
for i in range(len(lines)):
    average_times = average_times + [0]

for i in range (len(lines)):
    student_rating_array = student_rating_array + [0]

for i in range(len(lines)):
    average_rating = average_rating + [0]


for i in range(len(lines_rating)):

    if i < ((len(lines_rating) - 1) / 2):
        elements = lines_rating[(i * 2) + 1].split(',')
        add_value = []

        for j in range(len(elements)):
            value = int(elements[j])
            add_value.append(value)

        for d in range(len(add_value)):

            if (add_value[d] != 0):
                student_rating_array[d] = student_rating_array[d] + add_value[d]
                average_times[d] = average_times[d] + 1

for i in range(len(average_rating)):
    average_rating[i] = student_rating_array[i] / average_times[i]

"""calculate variance"""
variance = []
for i in range(len(lines)):
    variance = variance + [0]

for i in range(len(lines_rating)):

    if i < ((len(lines_rating) - 1) / 2):
        elements = lines_rating[(i * 2) + 1].split(',')
        add_value = []

        for j in range(len(elements)):
            value = int(elements[j])
            add_value.append(value)

        for d in range(len(add_value)):
            if (add_value[d] != 0 ):
                variance[d] = variance[d] + ((add_value[d] - average_rating[d]) ** 2)
variance2 = []
for i in range(len(lines)):
    variance2 = variance2  + [0]
for i in range(len(variance)):
    variance2[i] = variance[i] / (add_claculate_array[i] - 1)
print(variance2)
"""find the contentious movies list"""

boolean = []
highest_variance_index = []
highest_variance_movies_array = []
index = 0

for i in range(len(variance2)):
    boolean += [False]

for i in range(5):

    index = 0

    while(boolean[index] == True):
        index = index + 1
    store_numnber = variance2[index]

    for z in range(len(variance2)):
        if (variance2[z] >= store_numnber and boolean[z] == False):
            store_numnber = variance2[z]
            index = z

    boolean[index] = True
    highest_variance_index.append(store_numnber)
    highest_variance_movies_array.append(index)


for i in range(len(highest_variance_index)):
    highest_variance_index [i] = round(highest_variance_index[i])
"calculate the avarage movies that people see"

total_number = 0
for i in range(len(see_number_array)):
    total_number = total_number + see_number_array[i]
average_number = total_number / len(see_number_array)


"Print the outcome"
print("The average student in CPSC 231 has seen", round(average_number,1), "of the 100 movies")

print("The most popular movies were:")
for i in range(5):
    for z in range(len(lines)):
        lines_of_text = lines[highest_movies_score_array[i]]
        lines_without_newline = lines_of_text.rstrip()
        uu = highest_movies_array[i]
    print("\t",lines_without_newline, "with",uu,"views.")
print("The least popular movies were")
for i in range(5):
    for z in range(len(lines)):
        lines_of_text = lines[lowest_score_array[i]]
        lines_without_newline = lines_of_text.rstrip()
        uu = lowest_movies_array[i]
    print("\t",lines_without_newline, "with",uu,"views.")
print("The highest rated movies were")
for i in range(5):
    for z in range(len(lines)):
        lines_of_text = lines[highest_rating_movies_array[i]]
        lines_without_newline = lines_of_text.rstrip()
        uu = round(highest_rating_array[i],2)
    print("\t",lines_without_newline, "with an average rating of",uu,)
print("The lowest rated movies were")
for i in range(5):
    for z in range(len(lines)):
        lines_of_text = lines[lowest_rating_movies_array[i]]
        lines_without_newline = lines_of_text.rstrip()
        uu = round(lowest_rating_array[i],2)
    print("\t",lines_without_newline, "with an average rating of",uu,)
print("The most contentious movies were")
for i in range(5):
    for z in range(len(lines)):
        lines_of_text = lines[highest_variance_movies_array[i]]
        lines_without_newline = lines_of_text.rstrip()
        uu = round(highest_variance_index[i],2)
    print("\t",lines_without_newline)
