import stddraw
import math
import stdrandom
import sys
import stdarray
stddraw.setXscale(0, 129)
stddraw.setYscale(-1, 1)

array = stdarray.create1D(129, 0)
def fill_brownian(a, i0, i1, variance, scaleFactor):  
    if i0 - i1 == -1:
        stddraw.line(i0, a[i0], i1, a[i1])
        return 

    ym = int((i0 + i1) * 1/2)
    delta = stdrandom.gaussian(0, math.sqrt(variance))
    a[ym] = delta
    fill_brownian(a, i0, ym, variance/scaleFactor, scaleFactor)
    fill_brownian(a, ym, i1, variance/scaleFactor, scaleFactor)

def main():
    hurstExponent = float(sys.argv[1])
    stddraw.setPenRadius(0.0)
    stddraw.clear(stddraw.LIGHT_GRAY)
    scaleFactor = 2 ** (2.0 * hurstExponent)
    fill_brownian(array, 0, 128, 0.05, scaleFactor)
    stddraw.show()
    

if __name__ == '__main__':
    main()
    



# python3 lanjin_problem1.py 0.05

# python3 lanjin_problem1.py 0.5

# python3 lanjin_problem1.py 1
