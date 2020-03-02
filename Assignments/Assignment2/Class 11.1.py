"""
Sequrntial model of execution

1. statement excuted one at a time

in a certain order

conditions

loops

functions

only interaction / human is input

while we don't want to quit

1.CHECK for user input or other events

2. respond to those events

3。do other stuff in  a small finite amount of time


"""
import stddraw

# while we don't want to quit

#respond to those events
circle_radius = 0.05
#do other things I need to

while True:
    mouse_clicked = stddraw.mousePressed()  # return boolean

    key_has_been_typed = stddraw.hasNextKeyTyped()

    if mouse_clicked:

        x = stddraw.mouseX()
        y = stddraw.mouseY()
        stddraw.filledCircle(x,y,circle_radius)

    if key_has_been_typed:
        the_key = stddraw.hasNextKeyTyped()
        if the_key == "1":
            circle_radius = 0.01

        elif the_key =="2":
            circle_radius = 0.02

        elif the_key == "3":
            circle_radius = 0.03

        if the_key == " ":
            stddraw.clear()




    stddraw.show(0.05)
