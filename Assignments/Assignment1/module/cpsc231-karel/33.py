

from karel import *

def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_the_cross():
    while front_is_clear():
        move()
        if (not front_is_clear() and not right_is_clear()):
            turn_left()
            move()
            turn_left()
            move()
        if (not front_is_clear() and facing_west()):
            turn_right()
            move()
            if front
            turn_right()
            move()
            turn_right()
            move()


def safe_put_beeper():
    while (left_is_clear and not beepers_present()):
        turn_left()
        put_beeper()
        move()
        if right_is_clear():
            turn_right()
            move()
            turn_right()
            move()
        if not front_is_clear():
            turn_right()
    while (right_is_clear and not beepers_present()):
        turn_right()
        put_beeper()
        move()
        if left_is_clear():
            turn_left()
            move()
            turn_left()
            move()
        if not front_is_clear():
            turn_right()

begin_karel_program()

find_the_cross()
safe_put_beeper()


end_karel_program()