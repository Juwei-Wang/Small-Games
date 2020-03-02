import stddraw
import math
import stdarray
import random
import picture as Picture
from color import Color

stddraw.setXscale(0, 11)
stddraw.setYscale(0, 11)

def draw_a_parallelogram(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 0:
                x_axie = [k + 0.5, k + 0.2, k + 0.6, k + 0.9]
                y_axie = [j + 0.8, j + 0.3, j + 0.3, j + 0.8]
                stddraw.setPenColor(stddraw.BLUE)
                stddraw.filledPolygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.polygon(x_axie, y_axie)



def draw_a_pentagon(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 1:
                x_axie = [k + 0.2, k + 0.5, k + 0.8, k + 0.7, k + 0.3]
                y_axie = [j + 0.5, j + 0.2, j + 0.5, j + 0.8, j + 0.8]
                stddraw.setPenColor(stddraw.PINK)
                stddraw.filledPolygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.setPenRadius(0.005)
                stddraw.polygon(x_axie, y_axie)


def draw_a_square(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 2:
                x_axie = [k + 0.2, k + 0.2, k + 0.8, k + 0.8]
                y_axie = [j + 0.8, j + 0.2, j + 0.2, j + 0.8]
                stddraw.setPenColor(stddraw.YELLOW)
                stddraw.filledPolygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.polygon(x_axie, y_axie)


def draw_a_inclined(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 3:
                x_axie = [k + 0.15, k + 0.5, k + 0.85, k + 0.5]
                y_axie = [j + 0.5, j + 0.15, j + 0.5, j + 0.85]
                stddraw.setPenColor(stddraw.GREEN)
                stddraw.filledPolygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.polygon(x_axie, y_axie)


def draw_a_circle(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 4:         
                stddraw.setPenColor(stddraw.RED)
                stddraw.filledCircle(k + 0.5, j + 0.5, 0.39)
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.circle(k + 0.5, j + 0.5, 0.39)
               
            
def draw_a_regular_triangle(game_array):
    for j in range(9):
        for k in range(7):
            if game_array[j][k] == 5:
                x_axie = [k + 0.2, k + 0.8, k + 0.5]
                y_axie = [j + 0.3, j + 0.3, j + 0.7]            
                stddraw.setPenColor(stddraw.GRAY)
                stddraw.filledPolygon(x_axie, y_axie)
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.polygon(x_axie, y_axie)


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
    stddraw.text(2.2, 9.2, "Your current Score:")
    stddraw.text(9, 8, "Remaining Moves")
    stddraw.text(9, 7, "12")
    game_array = creat_an_useful_array()
    draw_a_circle(game_array)
    draw_a_inclined(game_array)
    draw_a_square(game_array)
    draw_a_regular_triangle(game_array)
    draw_a_pentagon(game_array)
    draw_a_parallelogram(game_array)
    return game_array

def draw_new_things(game_array,score):
    stddraw.clear()
    stddraw.setFontSize(30)
    stddraw.text(2.2, 9.2, "Your current Score:")
    stddraw.text(9, 8, "Remaining Moves")
    score1 = str(score)
    stddraw.text(5.5, 9.2, score1)
    draw_a_circle(game_array)
    draw_a_inclined(game_array)
    draw_a_square(game_array)
    draw_a_regular_triangle(game_array)
    draw_a_pentagon(game_array)
    draw_a_parallelogram(game_array)

#让数组中所有还没消掉的宝石下沉
def falling_down(game_array):
    for i in range(len(game_array[0])):
        exchange = True
        while exchange == True:
            exchange = False
            for j in range(len(game_array)):
                if j < len(game_array) - 1:
                    if game_array[j][i] == -1 and game_array[j + 1][i] != -1:
                        change = game_array[j + 1][i]
                        game_array[j + 1][i] = game_array[j][i]
                        game_array[j][i] = change
                        exchange = True
    return game_array

# 把数组里面所有—1的数字改变成有宝石代表的数字
def refill_the_vacant(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[0])):
            if game_array[i][j] == -1:
                game_array[i][j] = random.randrange(0, 6)

    return game_array

# 找到一个数组横向连续超过3个相同的数字的index
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

# 找到一个数组纵向向连续超过3个相同的数字的index
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
            if count >= 4:
                index_together = index_together + [index[len(index) - 1]]
    return index_together

# 把数组中所有超过三个连续的数字变成-1
def change_the_elimination_value(game_array, index_together):
    for i in range(len(index_together)):
        game_array[index_together[i][0]][index_together[i][1]] = -1
    return game_array

## 给予一个已经经过了补充的新数组，判断是否有连续三个存在
## 如果有连续三个存在，自动消除
def check_the_falling_part(game_array):
    useful = the_array_can_be_used(game_array)
    useful2 = the_array_can_be_used2(game_array)

    if useful:
        index1 = get_the_falling_elimination_index(game_array)
        game_array = change_the_elimination_value(game_array, index1)

    if useful2:
        index2 = get_the_falling_elimination_index_2(game_array)
        game_array = change_the_elimination_value(game_array, index2)

    return game_array

## 给予一个已经被消除而且数值存在至少3个以上都是负一的数组
## 并且产出一个全新的能玩的，不重复3个的游戏
## 并且计算本轮得分
def creat_a_new_useful_game(game_array,score):
    minor1_in_array = True
    while minor1_in_array:
        minor1_in_array = False
        score = score + caculate_the_score(game_array)
        game_array = falling_down(game_array)
        game_array = refill_the_vacant(game_array)
        draw_new_things(game_array,score)
        game_array = check_the_falling_part(game_array)
        for i in range(len(game_array)):
            for k in range(len(game_array[0])):
                if game_array[i][k] == -1:
                    minor1_in_array = True

    return score

## 给予一个已经被消除而且数值存在至少3个连续以上都是负一的数组
## 查找-1的个数来增加分数
## 如果有存在互相交叉的数字，这个分数会被乘以2倍
def caculate_the_score(game_array):
    score = 0
    for i in range(len(game_array)):
        for j in range(len(game_array[0])):
            if game_array[i][j] == -1:
                score += 1
    index1 = get_the_falling_elimination_index(game_array)
    index2 = get_the_falling_elimination_index_2(game_array)
    intersection = False
    for i in range(len(index1)):
        for j in range(len(index2)):
            if index1[i] == index2[j]:
                intersection = True
    if intersection == True:
        score = (score - 1) * 2
    return score




#python3 wwcat.py








