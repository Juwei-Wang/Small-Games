import stddraw
import math

def set_the_scale():
    stddraw.setXscale(0, 15)
    stddraw.setYscale(0, 15)


def set_the_head():
    stddraw.setPenRadius(0.005)
    stddraw.circle(6,6,1)

"""torso"""
def set_the_torso():
    stddraw.line(6,5,6,3)

"""left arm"""
def set_the_left_arm():
    stddraw.line(6,4,6 - (math.cos(math.radians(30)) * 1),4 - 0.5)

"""right arm"""
def set_the_right_arm():
    stddraw.line(6,4,6 + (math.cos(math.radians(30)) * 1),4 - 0.5)

"""left leg"""
def set_the_left_leg():
    stddraw.line(6,3,6 - (math.cos(math.radians(30)) * 1),3 - 0.5)

"""right leg"""
def set_the_right_leg():
    stddraw.line(6,3,6 + (math.cos(math.radians(30)) * 1),3 - 0.5)

"""gallows"""
def set_the_gallows():
    stddraw.line(6,7,6,8)
    stddraw.line(6,8,9,8)
    stddraw.line(9,8,9,1)
    x = [4,4,9,9]
    y = [1,0,0,1]
    stddraw.polygon(x,y)

"""face"""
def set_the_face():
    stddraw.line(6-0.1,6,5.5,6.5)
    stddraw.line(5.5,6,6-0.1,6.5)

    stddraw.line(6+0.1,6,6.5,6.5)
    stddraw.line(6.5,6,6+0.1,6.5)

    for i in range(30):
        stddraw.point(6 + (i * 0.01),5.6 - (i * 0.005))
        stddraw.point(6 - (i * 0.01),5.6 - (i * 0.005))


def std_show():
    stddraw.show(0)


