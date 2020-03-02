input_file = open('cpsc231-ratings.txt', 'r')
lines_rating = input_file.readlines()
input_file.close()
input_file = open('my-ratings.txt','r')
My_rating_lines = input_file.readlines()
input_file.close()
rating_array = []
add_claculate_array = []
My_rating_array = []

"""transalate my rating"""
original_my_rating = []
elements = My_rating_lines[1].split(',')
for i in range(len(elements)):
    My_score = 0
    value = int(elements[i])
    original_my_rating.append(value)
    if (value == 0):
        My_score = 0
    elif (value == 1):
        My_score = -5
    elif (value == 2):
        My_score = -3
    elif (value == 3):
        My_score = 1
    elif (value == 4):
        My_score = 3
    elif value == 5:
        My_score = 5
    My_rating_array.append(My_score)


"""calculate the similarity between people and me"""
for i in range(len(lines_rating)):
    if i < ((len(lines_rating) - 1) / 2):
        elements = lines_rating[(i * 2) + 1].split(',')
        add_value = []
        score_array = []
        Similarity = 0
        for j in range(len(elements)):
            value = int(elements[j])
            add_value.append(value)
            if (value == 0):
                Temp = 0
            elif (value == 1):
                Temp = -5
            elif (value == 2):
                Temp = -3
            elif (value == 3):
                Temp = 1
            elif (value == 4):
                Temp = 3
            elif value == 5:
                Temp = 5
            score_array.append(Temp)
        for z in range(len(score_array)):
            Similarity = Similarity + (score_array[z] * My_rating_array[z])
        add_claculate_array.append(Similarity)

"""Find the person with highest similarity array"""
highest_person_score = 0
for i in range(len(add_claculate_array)):
    if (add_claculate_array[i] > highest_person_score):
        highest_person_score = add_claculate_array[i]
        highest_person_index = i

boolean = []
higest_similarity_array = []
higest_peopeo_index_array = []
index = 0

for i in range(len(add_claculate_array)):
    boolean += [False]

for i in range(len(add_claculate_array)):

    index = 0

    while(boolean[index] == True):
        index = index + 1
    store_numnber = add_claculate_array[index]

    for z in range(len(add_claculate_array)):
        if (add_claculate_array[z] >= store_numnber and boolean[z] == False):
            store_numnber = add_claculate_array[z]
            index = z

    boolean[index] = True
    higest_similarity_array.append(store_numnber)
    higest_peopeo_index_array.append(index)

"""find the recommandation """

best_people_array_int = []
best_people_array = lines_rating[(higest_peopeo_index_array[0] * 2) + 1].split(',')
for i in range (len(best_people_array)):
        My_score = 0
        best_people_rating = int(best_people_array[i])
        best_people_array_int.append(best_people_rating)

"compare the movies between the people and me"
best_movies = []
store_number = 0
"find the highest rating in the best people array and find the best movies to recommand"
highest_number_in_best_people_array = 0
for i in range(len(best_people_array_int)):
    if (highest_number_in_best_people_array < best_people_array_int[i]):
        highest_number_in_best_people_array = best_people_array_int[i]
for i in range(len(best_people_array_int)):
    if (original_my_rating[i] == 0 and best_people_array_int[i] == highest_number_in_best_people_array):
        store_number = i
        best_movies.append(store_number)
"""find the lowest similar people to use in next step"""
lowest_similarity_number = min(add_claculate_array)

"find the second similar people until there is at least one movie in list"
array_number = 0
while (best_movies == []):
    array_number = array_number + 1
    for i in range(len(add_claculate_array)):
        best_people_array_int = []
        best_people_array = lines_rating[(higest_peopeo_index_array[array_number] * 2) + 1].split(',')
    for j in range(len(best_people_array)):
        My_score = 0
        best_people_rating = int(best_people_array[j])
        best_people_array_int.append(best_people_rating)
    best_movies = []
    store_number = 0
    highest_number_in_best_people_array = 0
    for k in range(len(best_people_array_int)):
        if (highest_number_in_best_people_array < best_people_array_int[k]):
            highest_number_in_best_people_array = best_people_array_int[k]
    for u in range(len(best_people_array_int)):
        if (original_my_rating[u] == 0 and best_people_array_int[u] == highest_number_in_best_people_array):
            store_number = u
            best_movies.append(store_number)
"""print the recomandation"""
input_file = open('cpsc231-movies.txt','r')
movies_lines = input_file.readlines()
lines_without_newline = My_rating_lines[0].rstrip()
print("Hello", lines_without_newline,"!!")
print("From your rating of out 100 movies , our CPSC 231 class believes that you might also like")
for i in range(len(best_movies)):
    lines_without_newline_for_movies = movies_lines[best_movies[i]].rstrip()
    print(lines_without_newline_for_movies)


