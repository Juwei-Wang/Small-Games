import  stdarray
import  random
import  wwcat

game_array = [[2,-1,3,4,3],
              [7,-1,-1,-1,-1],
              [8,-1,8,8,8],
              [1,9,8,5,3]]

index = wwcat.get_the_falling_elimination_index(game_array)
index2 = wwcat.get_the_falling_elimination_index_2(game_array)
score = wwcat.caculate_the_score(game_array)

print(score)
print(index)
print(index2)
