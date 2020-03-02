"""
This program is so simple that I don't need the usual DISCLAIMER...

Plays white noise forever by streaming random numbers to audio output.
"""

import math
import sys
import stddraw
import stdrandom
import stdarray

def curve(a,x0, y0, x1, y1, var, beta, n=7):
    if n == 0:
        stddraw.line(x0, y0, x1, y1)
        return

    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    ix = int((((x0 + x1) / 2.0)* 128))
    delta = stdrandom.gaussian(0.0, math.sqrt(var))
    a[ix] = ym + delta
    curve(a,x0, y0, xm, ym+delta, var/beta, beta, n-1)
    curve(a,xm, ym+delta, x1, y1, var/beta, beta, n-1)

hurstExponent = float(sys.argv[1])
stddraw.setPenRadius(0.0)
a = stdarray.create1D(129,0)
beta = 2.0 ** (2.0 * hurstExponent)
curve(a, 0.0, 0.5, 1.0, 0.5, 0.01, beta)
print(a)
stddraw.show()

"""def curve(a,x0, y0, x1, y1, var, beta, n=7):
    if n == 0:
        stddraw.line(x0, y0, x1, y1)
        return

    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    ix = int(xm)
    delta = stdrandom.gaussian(0.0, math.sqrt(var))
    a[ix] = ym + delta
    curve(a,x0, y0, xm, ym+delta, var/beta, beta, n-1)
    curve(a,xm, ym+delta, x1, y1, var/beta, beta, n-1)

list = stdarray.create1D(129,0)
hurstExponent = float(sys.argv[1])
stddraw.setPenRadius(0.0)
beta = 2.0 ** (2.0 * hurstExponent)
curve(list, 0.0, 0.5, 128.0, 0.5, 0.01, beta)
stddraw.show()
"""