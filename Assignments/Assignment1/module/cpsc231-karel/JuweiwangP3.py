


from karel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_the_cross():
    while front_is_clear():
        move()
        if (left_is_clear() and not right_is_clear):
            turn_left()
            move()
    else:
        turn_left()
        move()
        if (left_is_clear() and right_is_clear()):
            turn_right()
            move()
            turn_right()
            move()
        if not right_is_clear():
            turn_left()
            move()


def safe_put_beeper():
    while (left_is_clear and not beepers_present()):
        put_beeper()
        move()
        if right_is_clear():
            turn_right()
            move()
            turn_right()
            move()
        if not front_is_clear():
            turn_left()



begin_karel_program()

move()
move()
move()
turn_left()
move()
safe_put_beeper()

end_karel_program()