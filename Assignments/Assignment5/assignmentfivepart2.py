import stddraw
import math
import stdarray
import random
from color import Color

stddraw.setXscale(0,10)
stddraw.setYscale(0,10)

def draw_a_parallelogram(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 0:
                x_axie = [k + 0.4, k + 0.2, k + 0.6, k + 0.8]
                y_axie = [j + 0.8, j + 0.4, j + 0.4, j + 0.8]
                stddraw.polygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.BLUE)
                stddraw.filledPolygon(x_axie,y_axie)



def draw_a_pentagon(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 1:
                x_axie = [k + 0.2, k + 0.5, k + 0.8, k + 0.7, k + 0.3]
                y_axie = [j + 0.5, j + 0.2, j + 0.5, j + 0.8, j + 0.8]
                stddraw.setPenColor(stddraw.PINK)
                stddraw.filledPolygon(x_axie, y_axie)
                stddraw.setPenRadius(0.003)
                stddraw.polygon(x_axie, y_axie)


def draw_a_square(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 2:
                x_axie = [k + 0.2, k + 0.2, k + 0.8, k + 0.8]
                y_axie = [j + 0.8, j + 0.2, j + 0.2, j + 0.8]
                stddraw.polygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.YELLOW)
                stddraw.filledPolygon(x_axie,y_axie)


def draw_a_inclined(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 3:
                x_axie = [k + 0.2 , k + 0.5, k + 1 - 0.2, k + 0.5]
                y_axie = [j + 0.5, j + 0.2, j + 0.5, j + 1 - 0.2]
                stddraw.polygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.GREEN)
                stddraw.filledPolygon(x_axie,y_axie)


def draw_a_circle(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 4:
                stddraw.circle(k + 0.5, j + 0.5, 0.3)
                stddraw.setPenColor(stddraw.RED)
                stddraw.filledCircle(k + 0.5 , j + 0.5 , 0.3)


def draw_a_regular_triangle(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 5:
                x_axie = [k + 0.2, k + 0.8, k + 0.5]
                y_axie = [j + 0.3, j + 0.3, j + 0.7]
                stddraw.polygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.ORANGE)
                stddraw.filledPolygon(x_axie,y_axie)


def the_array_can_be_used(game_array):
    useful = False

    for i in range(9):
        current_number = -1
        count = 1
        for k in range(7):
            if k == 0:
                current_number = game_array[i][k]
            if k >= 1:
                if game_array[i][k] == current_number:
                    count += 1
                else:
                    current_number = game_array[i][k]
                    count = 1
            if count >= 3:
                useful = True
    return useful



def the_array_can_be_used2(game_array):
    useful = False

    for i in range(7):
        current_number = -1
        count = 1
        for k in range(9):
            if k == 0:
                current_number = game_array[k][i]
            if k >= 1:
                if game_array[k][i] == current_number:
                    count += 1
                else:
                    current_number = game_array[k][i]
                    count = 1
            if count >= 3:
                useful = True

    return useful


def creat_an_useful_array():
    useful = True
    game_array = stdarray.create2D(9, 7, 1)
    while useful or useful2:

        for i in range(9):
            for k in range(7):
                game_array[i][k] = random.randrange(0, 6)

        useful = the_array_can_be_used(game_array)
        useful2 = the_array_can_be_used2(game_array)


    return game_array


def draw_all_the_things():
    stddraw.setFontSize(30)
    stddraw.text(1.5, 9.2, "Hi Handsome")
    stddraw.text(5, 9.2, "Your current Score:")
    game_array = creat_an_useful_array()
    draw_a_circle(game_array)
    draw_a_inclined(game_array)
    draw_a_square(game_array)
    draw_a_regular_triangle(game_array)
    draw_a_pentagon(game_array)
    draw_a_parallelogram(game_array)

def falling_down(game_array):
    for i in range(len(game_array[0])):
        exchange = True
        while exchange == True:
            exchange = False
            for j in range(len(game_array)):
                if j < len(game_array) -1:
                    if game_array[j][i] == -1 and game_array[j + 1][i] != -1:
                        change = game_array[j + 1][i]
                        game_array[j + 1][i] = game_array[j][i]
                        game_array[j][i] = change
                        exchange = True
    return game_array

def refill_the_vacant(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[0])):
            if game_array[i][j] == -1:
                game_array[i][j] = random.randrange(0, 6)

    return  game_array

def get_the_falling_elimination_index(game_array):
    index_together = []
    for i in range(len(game_array)):
        current_number = -1
        count = 1
        index = []
        for k in range(len(game_array[0])):
            if k == 0:
                current_number = game_array[i][k]
                index.append([i, k])
            if k >= 1:
                if game_array[i][k] == current_number:
                    count += 1
                    index.append([i, k])
                else:
                    current_number = game_array[i][k]
                    count = 1
                    index = []
                    index.append([i, k])
            if count == 3:
                useful = True
                index_together = index_together + index
            if count >= 4:
                index_together = index_together + [index[len(index) - 1]]

        return index_together

def get_the_falling_elimination_index_2(game_array):
    index_together = []
    for i in range(len(game_array[0])):
        current_number = -1
        count = 1
        index = []
        for k in range(len(game_array)):
            if k == 0:
                current_number = game_array[k][i]
                index.append([k, i])
            if k >= 1:
                if game_array[k][i] == current_number:
                    count += 1
                    index.append([k, i])
                else:
                    current_number = game_array[k][i]
                    count = 1
                    index = []
                    index.append([k, i])
            if count == 3:
                useful = True
                index_together = index_together + index
                print(index)
            if count >= 4:
                index_together = index_together + [index[len(index) - 1]]
        return index_together

def change_the_elimination_value(game_array,index_together):
    for i in range(len(index_together)):
        game_array[index_together[i][0]][index_together[i][1]] = -1
    return game_array

def check_the_falling_part(game_array):

    useful = the_array_can_be_used(game_array)
    useful2 = the_array_can_be_used2(game_array)

    if useful:
        index1 = get_the_falling_elimination_index(game_array)
        game_array = change_the_elimination_value(game_array,index1)

    if useful2:
        index2 = get_the_falling_elimination_index_2(game_array)
        game_array = change_the_elimination_value(game_array,index2)




def creat_a_new_useful_game(game_array):
    falling_down(game_array)
    refill_the_vacant(game_array)
    check_the_falling_part(game_array)











draw_all_the_things()
stddraw.show()













