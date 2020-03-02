"""
drawing funtion
stddraw line( x, y, x1,y1)
point(x,y)
Control function
stddraw show()
setXscale ( min, max)
setyscale (min, max)
3 step:
import stddraw
call drawfunction
call show()
stddraw.setPencolor(stddraw.Blue)
stddraw.setpenRadius(radius)



1st. problem  graphing calculator
2 determine domain and range
3. repeat for 100 times
A select x-value btw -10, 10
B calculate y value
C store (x, y ) in list
4. draw line segment
repeat for

"""
import stddraw
my_xs = []
my_ys = []
xmin = -10.0
xmax = 10.0
ymin = -10.0
ymax = 10.0
stddraw.setXscale(xmin, xmax)
stddraw.setYscale(ymin, ymax)
for i in range(100):
    xrange = xmax - xmin
    step = xrange / 100.0
    x = xmin + i * step
    y = x * x
    my_xs += [x]
    my_ys += [y]

repetitions = len(my_xs) - 1
for i in range(repetitions):
    x0 = my_xs[i]
    y0 = my_ys[i]
    x1 = my_xs[i + 1]
    y1 = my_ys[i + 1]
    stddraw.line(x0,y0,x1,y1)

stddraw.show()



