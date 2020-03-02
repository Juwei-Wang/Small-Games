import stddraw
import random

pos_x = 0.5
pos_y = 0.5

vel_x = random.random()
vel_y = random.random()



delta_t = 0.01

while True:
    delta_x = vel_x * delta_t
    delta_y = vel_y * delta_t

    pos_x += delta_x
    pos_y += delta_y

    if pos_x < 0.0 or pos_x > 1.0:

        vel_x = -vel_x

    if pos_y < 0.0 or pos_y > 1.0:

        vel_y = - vel_y
