import math
import sys
import stddraw
import random
import stdarray
import stdrandom
import stdaudio
"""
def fill_brownian1(a,x0, y0, x1, y1, var, beta, n=12):
    if n == 0:
        stddraw.line(x0, y0, x1, y1)
        return

    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    ix = int((((x0 + x1) / 2.0)* 4096))
    delta = stdrandom.gaussian(0.0, math.sqrt(var))
    a[ix] = ym + delta
    fill_brownian(a,x0, y0, xm, ym+delta, var/beta, beta, n-1)
    fill_brownian(a,xm, ym+delta, x1, y1, var/beta, beta, n-1)
"""
"""
def fill_brownian(a, i0, i1, variance, scale):
    if i0 - i1 == -1:
        return

    ym = 0
    Xm = ((i0 + i1) / 2)
    index = int(Xm)
    delta = stdrandom.gaussian(0, math.sqrt(variance))
    a[index] = delta
    fill_brownian(a, i0, Xm, variance/scale, scale)
    fill_brownian(a, Xm, i1, variance/scale, scale)
    

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
a_brown_total = []
for i in range(20):
    stddraw.setPenRadius(0.0)
    a_brown = stdarray.create1D(44100, 0)
    beta = 2.0 ** (2.0 * hurstExponent)
    fill_brownian(a_brown, 0, 44099, 0.05, beta)
    a_brown_total = a_brown_total+ a_brown



a_total_white = stdarray.create1D(882000,0)
for i in range(len(a_total_white)):
    if (i % 44100) == 0:
        a_total_white[i] = 0
    else:
        a_total_white[i] = stdrandom.uniformFloat(-0.25,0.25)

y = stdarray.create1D(882000,0)
for i in range(882000):
    f = 0.25
    t = i / 44100
    y[i] = ((1 - (math.sin(math.pi * f * t)) ** 6) * a_brown_total[i]) + (((math.sin(math.pi * t * f)) ** 6) * a_total_white[i])

"""
for i in range(len(y)):
    if i < len(y) - 1:
        stddraw.line(i,a_brown_total[i],i+1,a_brown_total[i+1])
"""
stdaudio.playSample(y)







