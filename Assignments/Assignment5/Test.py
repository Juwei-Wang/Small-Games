import stddraw

stddraw.setYscale(0, 4)
stddraw.setXscale(0, 4)

game_array = [[0, 1, 3, 2, 2, 4, 4],
              [5, 3, 2, 5, 2, 4, 5],
              [2, 3, -1, 2, 0, 2, 5],
              [5, 5, -1, 3, 5, 1, 3],
              [0, 5, -1, 4, 2, 2, 4],
              [4, 0, -1, 5, 2, 0, 1],
              [1, 5, 4, 0, 1, 1, 3],
              [0, 3, 2, 1, 0, 2, 4],
              [4, 4, 3, 2, 1, 1, 5]]


same_line = True


def check_weather_win(test):
    if len(test) >= 3:
        win = False
        count_the_same = 0
        count_the_same1 = 0
        count_the_same2 = 0
        for i in range(len(test)):
            if test[i][0] == 0:
                count_the_same += 1
            if test[i][0] == 1:
                count_the_same1 += 1
            if test[i][0] == 2:
                count_the_same2 += 1
            if count_the_same >= 3 or count_the_same1 >= 3 or count_the_same2 >= 3:
                win = True
        count_the_same = 0
        count_the_same1 = 0
        count_the_same2 = 0
        for i in range(len(test)):
            if test[i][1] == 0:
                count_the_same += 1
            if test[i][1] == 1:
                count_the_same1 += 1
            if test[i][1] == 2:
                count_the_same2 += 1
            if count_the_same >= 3 or count_the_same1 >= 3 or count_the_same2 >= 3:
                win = True
        count = 0
        for i in range(len(test)):
            if test[i] == [1, 1]:
                count += 1
            if test[i] == [0, 0]:
                count += 1
            if test[i] == [2, 2]:
                count += 1
            if count >= 3:
                win = True
        count = 0
        for i in range(len(test)):
            if test[i] == [1, 1]:
                count += 1
            if test[i] == [0, 2]:
                count += 1
            if test[i] == [2, 0]:
                count += 1
            if count >= 3:
                win = True
    return win


def player_one_draw(game_array_in_def):
    x = stddraw.mouseX()
    y = stddraw.mouseY()
    for j in range(3):
        for k in range(3):
            if x >= j and x <= j + 1 and y >= k and y <= k + 1:
                stddraw.circle(j + 0.5, k + 0.5, 0.3)
                game_array_in_def[j][k] = 1

    return game_array_in_def


def player_two_draw(game_array_in_def):
    x = stddraw.mouseX()
    y = stddraw.mouseY()
    for j in range(3):
        for k in range(3):
            if x >= j and x <= j + 1 and y >= k and y <= k + 1:
                stddraw.line(j + 0.3, k + 0.7, j + 0.7, k + 0.3)
                stddraw.line(j + 0.3, k + 0.3, j + 0.7, k + 0.7)
                game_array_in_def[j][k] = 2

    return game_array_in_def


def draw_the_picture(game_array):
    stddraw.line(0, 2, 3, 2)
    stddraw.line(0, 1, 3, 1)
    stddraw.line(1, 0, 1, 3)
    stddraw.line(2, 0, 2, 3)
    stddraw.line(3, 0, 3, 3)
    stddraw.line(0, 3, 3, 3)
    for i in range(3):
        for x in range(3):
            if game_array[i][x] == 1:
                stddraw.circle(i + 0.5, x + 0.5, 0.3)
            if game_array[i][x] == 2:
                stddraw.line(i + 0.3, x + 0.7, i + 0.7, x + 0.3)
                stddraw.line(i + 0.3, x + 0.3, i + 0.7, x + 0.7)


def expend_the_player_array(game_player, number):
    for i in range(3):
        for x in range(3):
            if game_array[i][x] == number:
                game_player = game_player + [[i, x]]
    return game_player


def there_is_no_winner(game_playertwo_click, game_playerOne_click):
    if len(game_playertwo_click) + len(game_playerOne_click) >= 9:
        stddraw.clear()
        stddraw.setFontSize(30)
        stddraw.text(1.5, 2.5, "There is no winner ! ")
        stddraw.text(1.5, 1.5, "please close you window !")
        stddraw.show(1)
        exit()


def determine_the_winner(game_player_click, playernumber, game_win):
    if len(game_player_click) >= 3:
        win = check_weather_win(game_player_click)
        playernumber_str = str(playernumber)
        if win == True:
            stddraw.clear()
            stddraw.setFontSize(30)
            stddraw.text(1.5, 2.5, "player" + playernumber_str + " win !")
            stddraw.text(1.5, 1.5, "please close you window !")
            game_win = False
            exit()
    return game_win


game_win = True
count = 0
mouse_clicked = False
game_playerOne_click = []
game_playertwo_click = []

while game_win == True:

    """playerOne turn"""
    mouse_clicked = False

    while mouse_clicked == False:
        mouse_clicked = stddraw.mousePressed()  # return boolean

        stddraw.clear()
        stddraw.setFontSize(30)
        stddraw.text(1, 3.5, "Is playerOne's turn")

        draw_the_picture(game_array)

        if mouse_clicked:
            game_array = player_two_draw(game_array)

        game_playertwo_click = []
        game_playertwo_click = expend_the_player_array(game_playertwo_click, 2)
        game_win = determine_the_winner(game_playertwo_click, 2, game_win)

        there_is_no_winner(game_playertwo_click, game_playerOne_click)

        stddraw.show(1)

    """playerOne turns"""
    mouse_clicked = False

    while mouse_clicked == False:
        mouse_clicked = stddraw.mousePressed()  # return boolean

        stddraw.clear()
        stddraw.setFontSize(30)
        stddraw.text(1, 3.5, "Is playerTwo's turn")

        draw_the_picture(game_array)

        if mouse_clicked:
            game_array = player_one_draw(game_array)

        game_playerOne_click = []
        game_playerOne_click = expend_the_player_array(game_playerOne_click, 1)
        game_win = determine_the_winner(game_playerOne_click, 1, game_win)

        there_is_no_winner(game_playertwo_click, game_playerOne_click)

        stddraw.show(1)











