
from karel import *

def pick_one_both_end():
    turn_around()
    if beepers_present():
        pick_beeper()
        move_to_wall()
        turn_around()
    if beepers_present():
            pick_beeper()


def prepare_for_continue():
    if front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
        else:
            turn_around()
            move()
        if front_is_clear():
            move()

def turn_around():
    turn_left()
    turn_left()

def move_to_end_pick_beeper():
    while beepers_present():
        move()
    turn_around()
    move()
    pick_beeper()
    move()

def according_facing_place_put_beeper():
    if facing_east():
        turn_around()
        if front_is_clear():
            move()
        put_beeper()
    else:
        turn_around()
        put_beeper()
        if front_is_clear():
            move()
        put_beeper()

def fill_one_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def move_to_wall():
    while front_is_clear():
        move()




begin_karel_program()

fill_one_row()
pick_one_both_end()
prepare_for_continue()

end_karel_program()
