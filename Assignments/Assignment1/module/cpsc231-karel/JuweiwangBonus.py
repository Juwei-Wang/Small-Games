

from karel import*

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def flat_the_beepers():
    while front_is_clear():
        move()
        if beepers_present():
            collect_all_the_beepers()
            turn_left()
        if beepers_in_bag():
            put_beeper()
        turn_back_to_first_line()


def turn_back_to_first_line():
    if not front_is_clear():
        if (facing_north() and not front_is_clear()):
            turn_right()
            move()
            turn_right()
        if (facing_south() and not front_is_clear()):
            turn_left()
            move

def collect_all_the_beepers():
    while beepers_present():
        pick_beeper()

def searching_the_second_peak():
    while front_is_clear():
        move()
        if not front_is_clear():
            turn_around()
            move()
            turn_right()
        if beepers_present():
            turn_right()
            move()
            if beepers_present():
                turn_around()
                move()
                turn_right()
            if not beepers_present():
                turn_around()
                while front_is_clear():
                    move()
                    pick_beeper()

def back_to_1_1():
    turn_right()
    while front_is_clear():
        move()

def put_second_number_beeper_at_1_1():
    while beepers_in_bag():
        put_beeper()

def return_all_the_beepers():
    while front_is_clear():
        return_single_row_beepers()
        if (not front_is_clear() and facing_south()):
            put_second_number_beeper_at_1_1()
            turn_left()
            move()

def return_single_row_beepers():
    while front_is_clear():
        move()
        if beepers_present():
            turn_left()
            while beepers_present():
                pick_beeper()
                move()
                if not beepers_present():
                    turn_around()
                if (facing_north() and not front_is_clear()):
                    pick_beeper()
                    turn_around()



def turn_back_to_first_line_second_round():
    while front_is_clear():
        move()
        if not front_is_clear():
            if (facing_north() and not front_is_clear()):
                turn_right()
                move()
                turn_right()
            if (facing_south() and not front_is_clear()):
                turn_right()
                move()
                put_second_number_beeper_at_1_1()
                turn_around()





begin_karel_program()

flat_the_beepers()
turn_back_to_first_line()
turn_left()
searching_the_second_peak()
back_to_1_1()
put_second_number_beeper_at_1_1()
turn_around()
return_all_the_beepers()
turn_right()
back_to_1_1()
collect_all_the_beepers()


end_karel_program()