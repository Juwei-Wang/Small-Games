input_file = open('cpsc231-ratings.txt', 'r')
lines_rating = input_file.readlines()
input_file.close()
rating_array = []
add_claculate_array = []
for i in range (100):
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

print(add_claculate_array)
Lowest_popular_score = add_claculate_array[i]
for i in range(len(add_claculate_array)):
    if (Lowest_popular_score > add_claculate_array[i]):
        Lowest_popular_score = add_claculate_array[i]

"""find the most popular  5 movies"""
store_P_number = 0
popular_movies_array = []
copy_popularity_array = []
for i in range(len(add_claculate_array)):
    copy_popularity_array.append(add_claculate_array[i])
for i in range(5):
    store_P_number = 0
    for x in range(len(copy_popularity_array)):
        if (copy_popularity_array[x] >= store_P_number):
            store_P_number = x
    copy_popularity_array[store_P_number] = Lowest_popular_score - 1
    popular_movies_array.append(store_P_number)
print(popular_movies_array)
"""find the most popular movie to compute in the next step"""
Lowest_popular_score = add_claculate_array[i]
for i in range(len(add_claculate_array)):
    if (Lowest_popular_score > add_claculate_array[i]):
        Lowest_popular_score = add_claculate_array[i]