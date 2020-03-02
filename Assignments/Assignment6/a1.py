
import math
import sys
import stddraw
import stdrandom
import stdarray
import stdaudio

stddraw.setYscale(-1,1)
stddraw.setXscale(0,129)
## 7 is the time that 128 can not be divided by 2
"""
def fill_brownian1(a,x0, y0, x1, y1, var, beta, n=7):
    if n == 0:
        stddraw.line(x0, y0, x1, y1)
        return

    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    ix = int((((x0 + x1) / 2.0)* 128))
    delta = stdrandom.gaussian(0.0, math.sqrt(var))
    a[ix] = ym + delta
    fill_brownian(a,x0, y0, xm, ym+delta, var/beta, beta, n-1)
    fill_brownian(a,xm, ym+delta, x1, y1, var/beta, beta, n-1)
"""

def fill_brownian(a, i0, i1, variance, scale):
    if i1 - i0 == 1:
        return

    Xm = int ((i0 + i1) / 2)
    ym = (a[i0] + a[i1]) /2
    delta = stdrandom.gaussian(0, math.sqrt(variance))
    a[Xm] = ym + delta
    fill_brownian(a, i0, Xm, variance/scale, scale)
    fill_brownian(a, Xm, i1, variance/scale, scale)


hurstExponent = float(sys.argv[1])
stddraw.setPenRadius(0.0)
a = stdarray.create1D(129,0)
beta = 2.0 ** (2.0 * hurstExponent)
fill_brownian(a, 0,128, 0.05, beta)
for i in range(len(a)):
    if i < len(a) - 1:
        stddraw.line(i,a[i],i+1,a[i+1])

stddraw.show()





