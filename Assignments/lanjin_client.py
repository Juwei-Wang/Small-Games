import stddraw
import stdarray
import juweimodule
import lj

stddraw.setXscale(0, 11)
stddraw.setYscale(0, 11)
turns = 1
moves = 12

def select_first(game_array_select):
    global turns
    global moves
    if turns == 1:
        turns = 2
        x = stddraw.mouseX()
        y = stddraw.mouseY()
        for i in range(7):
            for j in range(9):
                if x > i and x < i + 1 and y > j and y < j + 1:
                    stddraw.setPenColor(stddraw.RED)
                    stddraw.square(i + 0.5, j + 0.5, 0.5)
                    game_array_select[j][i] = 1
    return game_array_select


def select_first_position():
    for i in range(7):
        for j in range(9):
            if a[j][i] == 1:
                position = [j, i, game_board[j][i]]
    return position


def scan_for_same():
    c = []
    d = []
    x = []
    y = []
  
    for i in range(9):
        c = []
        for j in range(1, 7):
            if game_board[i][j-1] == game_board[i][j]:
                a = [i, j-1]
                b = [i, j]
                if a not in c:
                    c.append(a)
                if b not in c:
                    c.append(b)
            if game_board[i][j-1] != game_board[i][j]:
                c = []
            if len(c) >= 3:
                x.extend(c)

    for j in range(7):
        d = []
        for i in range(1, 9):
            if game_board[i-1][j] == game_board[i][j]:
                e = [i-1, j]
                f = [i, j]
                if e not in d:
                    d.append(e)
                if f not in d:
                    d.append(f)
            if game_board[i-1][j] != game_board[i][j]:
                d = []
            if len(d) >= 3:
                x.extend(d)

    for i in range(len(x)):
        if x[i] not in y:
            y.append(x[i])
    
    for i in range(len(y)):
        game_board[y[i][0]][y[i][1]] = -1
  
def display():
    a = 0
    for i in range(9):
        for j in range(7):
            if -1 == game_board[i][j]:
                a = 1
    return a

def reminding_faulse_move():
    stddraw.setFontSize(28)
    stddraw.setPenColor(stddraw.RED)
    stddraw.text(5.2, 10.5, "Your second choice is not adjacent to the first one")
    stddraw.show(1200)

def reminding_not_matching():
    stddraw.setFontSize(28)
    stddraw.setPenColor(stddraw.RED)
    stddraw.text(5.2, 10.5, "Taffies are not matching")
    stddraw.show(1200) 




def select_second(game_array_select):
    global turns
    global moves
    row1 = first_position[0]
    column1 = first_position[1]
    if turns == 2:
        turns = 1
        x = stddraw.mouseX()
        y = stddraw.mouseY()
        for i in range(9):
            for j in range(7):         
                if x > j and x < j + 1 and y > i and y < i + 1:
                    if i == row1 and j == column1: 
                        stddraw.setPenColor(stddraw.WHITE)
                        stddraw.square(first_position[1] + 0.5, first_position[0] + 0.5, 0.5)  
                        juweimodule.draw_new_things(game_board, score)
                    else:
                        if i == row1 and j != column1:
                            if j - 1 == column1 or j + 1 == column1:
                                swap = game_board[i][j]
                                game_board[i][j] = game_board[row1][column1]
                                game_board[row1][column1] = swap
                                scan_for_same()
                                if display() == 1:
                                    moves -= 1
                                    juweimodule.draw_new_things(game_board, score)
                                else:
                                    swap = game_board[i][j]
                                    game_board[i][j] = game_board[row1][column1]
                                    game_board[row1][column1] = swap  
                                    reminding_not_matching()

                            else: 
                                reminding_faulse_move()     
                                
                        elif j == first_position[1] and i != first_position[0]:
                            if i - 1 == row1 or i + 1 == row1: 
                                swap = game_board[i][j]
                                game_board[i][j] = game_board[row1][column1]
                                game_board[row1][column1] = swap
                                scan_for_same()
                                if display() == 1:
                                    moves -= 1
                                    juweimodule.draw_new_things(game_board, score)
                                else:
                                    swap = game_board[i][j]
                                    game_board[i][j] = game_board[row1][column1]
                                    game_board[row1][column1] = swap 
                                    reminding_not_matching()
                            else:
                                reminding_faulse_move()                               
                        else:
                            reminding_faulse_move()
                           
    return game_array_select

def print_remaining_moves():
    global moves
    stddraw.setFontSize(30)
    if moves == 12:
        stddraw.text(9, 7, "12")
    if moves == 11:
        stddraw.text(9, 7, "11")
    if moves == 10:
        stddraw.text(9, 7, "10")
    if moves == 9:
        stddraw.text(9, 7, "9")
    if moves == 8:
        stddraw.text(9, 7, "8")
    if moves == 7:
        stddraw.text(9, 7, "7")
    if moves == 6:
        stddraw.text(9, 7, "6")
    if moves == 5:
        stddraw.text(9, 7, "5")
    if moves == 4:
        stddraw.text(9, 7, "4")
    if moves == 3:
        stddraw.text(9, 7, "3")
    if moves == 2:
        stddraw.text(9, 7, "2")
    if moves == 1:
        stddraw.text(9, 7, "1")
    if moves == 0:
        stddraw.text(9, 7, "0")
    stddraw.show(500)

def game_over():
    if winning_score < score:
        return False
    else:
        return True
    if moves < 0:
        return False
    else:
        return True
            
game_board = juweimodule.draw_all_the_things()
score = 0
score1 = str(0)
stddraw.text(5.5, 9.2, score1)
print(game_board)
winning_score = 1000000


while game_over():
    print(game_board)
    if turns == 1 and stddraw.mousePressed():
        a = stdarray.create2D(9, 7, 0)
        select_first(a)
        first_position = select_first_position()
    if turns == 2 and stddraw.mousePressed():
        select_second(a)
        score = score + juweimodule.creat_a_new_useful_game(game_board, score)
        print_remaining_moves()
   
    stddraw.show(15)
stddraw.setFontSize(28)
stddraw.setPenColor(stddraw.BLUE)
if moves < 0 and score < winning_score:
    stddraw.text(5.2, 10.5, "You lose!")
    stddraw.show() 
else:
    stddraw.text(5.2, 10.5, "You win!")
    stddraw.show() 



# python3 lanjin_client.py

