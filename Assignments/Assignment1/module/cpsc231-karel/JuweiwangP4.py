

from karel import *

def turn_around():
    turn_left()
    turn_left()

def fill_one_row():
    move()
    while (front_is_clear() and not beepers_present()):
        put_beeper()
        move()

def turn_around_to_the_other_side():
    turn_around()
    move()
    if beepers_present():
        pick_beeper()
        move()
    while front_is_clear():
        move()
        if not beepers_present():
            turn_around()
            move()
            if not beepers_present():
                put_beeper()
                end_karel_program()
            pick_beeper()






begin_karel_program()

fill_one_row()
turn_around_to_the_other_side()

end_karel_program()