
from karel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def moving():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

def facing_move():
    while front_is_clear():
        put_beeper()
        move()
        if (facing_east() and not front_is_clear()):
            turn_left()
            move()
            put_beeper()
            turn_left()
            move()
        if (facing_west() and not front_is_clear()):
            turn_right()
            move()
            put_beeper()
            turn_right()
            move()
        move()


begin_karel_program()

facing_move()


end_karel_program()


