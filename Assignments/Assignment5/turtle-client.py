"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


A client that uses the Turtle data type from turtle.py to draw an octagon.
"""
from turtle import Turtle
import math
import stddraw

my_turtle = Turtle(0.5, 0.5)

# draw an octagon
for i in range(8):
    my_turtle.go_forward(0.2)
    angle = math.radians(45.0)
    my_turtle.turn_left(angle)

stddraw.show()
