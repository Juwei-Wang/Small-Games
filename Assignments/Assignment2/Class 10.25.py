import stddraw
import random

def roll_die():
    return random.randrange(1,7)

def draw_bar(x , y , w, h):
    stddraw.filledRectangle(x, y , w, h)

stddraw.setYscale(0.0, 0.25)

tallies = [0] * 13
def oo():
    for trial in range(100):
        roll1 = roll_die()
        roll2 = roll_die()
        total = roll1 + roll2
        tallies[total] += 1
        return roll1,roll2,total,tallies

oo()
print(oo())


for i in range(len(tallies)):
    tallies[i] = float(tallies[i]) / 100.0

print(tallies)


bar_number = 0
for dice_sum in range(2,13):
    frequency = tallies[dice_sum]
    x = bar_number * 1.0 / 11.0
    y = 0.0
    width = 1.0 / 22.0
    height = frequency
    draw_bar(x, y , width , height)


"""
stddraw.show() stop and wait for user to close window
stddraw.show(milliseconds) flip buffers the wait for millisecond and return control
stddraw.clear() clears the back buffer
"""
"""
Bouncing ball example
keep track f ball's position and velocity
repeat continuously through time  
a: advance the ball's position
b: check if it hit a wall
c: reflect the velocity about the wall it hit
d draw ball


"""