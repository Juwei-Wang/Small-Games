import stddraw
import math
import time

time_aggregate = time.localtime()
hour = time_aggregate.tm_hour
minute = time_aggregate. tm_min
second = time_aggregate. tm_sec

if hour > 12:
    hour = hour - 12
seconds = hour * 60 * 60 + minute * 60 + second
angle_hour = 450 - ((seconds / (12 * 60 * 60)) * 360)

minutes_angle = 450 - (minute / 60) * 360

seconds_angle = 450 - (second / 60) * 360




stddraw.circle(0.5,0.5,.5)
stddraw.circle(0.5,0.5,.45)



x = (math.cos(math.radians(seconds_angle)) * 0.5 * 0.7) + 0.5
y = (math.sin(math.radians(seconds_angle)) * 0.5 * 0.7) + 0.5

x1 = (math.cos(math.radians(minutes_angle)) * 0.5 * 0.5) + 0.5
y1 = (math.sin(math.radians(minutes_angle)) * 0.5 * 0.5) + 0.5

x2 = (math.cos(math.radians(angle_hour)) * 0.5 * 0.3) + 0.5
y2 = (math.sin(math.radians(angle_hour)) * 0.5 * 0.3) + 0.5

test3 = 0
adjust_number = 9
adjust_number2 = 3
for i in range(12):
    stddraw.setFontSize(30)
    test3x = (math.cos(math.radians(test3)) * 0.5 * 0.82) + 0.5
    test3y = (math.sin(math.radians(test3)) * 0.5 * 0.82) + 0.5
    store_number = i
    if store_number == 0:
        store_number = 3
    elif store_number == 1:
        store_number = 2
    elif store_number == 2:
        store_number = 1
    elif store_number >= 3:
        store_number = store_number + adjust_number
        adjust_number = adjust_number - 2
    xx = str(store_number)
    stddraw.text(test3x, test3y, xx)
    test3 = test3 + 30


stddraw.line(.5,.5,x,y)
stddraw.setPenColor(stddraw.BLUE)
stddraw.line(.5,.5,x1,y1)
stddraw.setPenRadius(0.01)
stddraw.setPenColor(stddraw.RED)
stddraw.line(.5,.5,x2,y2)
stddraw.setPenColor(stddraw.BLACK)
stddraw.setPenRadius(0.02)
stddraw.point(.5,.5)


stddraw.show()