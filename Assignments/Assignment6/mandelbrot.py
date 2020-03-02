"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


A client program that uses our Complex data type to sketch the Mandelbrot set.
See Program 3.2.7 in the course text for a more well-developed client.
"""

from complex import Complex
import stddraw

ab = complex(7,8)
print(ab)
# a function to repeatedly apply the Mandelbrot function, and see if
# a given initial complex value "escapes" (tends to infinity)
def escapes(z0):
    """
    :param z0: Initial complex value of function
    :return: True if repeated application tends to infinity, False otherwise
    """
    iterations = 100
    z = z0
    for i in range(iterations):
        z = z*z + z0
        if abs(z) > 4.0:
            return True
    return False

xmin = -2
xmax = 2
ymin = -2
ymax = 2
pixels = 256

stddraw.setXscale(xmin, xmax)
stddraw.setYscale(ymin, ymax)

for i in range(pixels):
    x = (i / pixels) * (xmax - xmin) + xmin
    for j in range(pixels):
        y = (j / pixels) * (ymax - ymin) + ymin
        z = Complex(x, y)
        print(z)
        if not escapes(z):
            stddraw.point(x, y)
    stddraw.show(0.0)


stddraw.show()



# z1 = Complex(2.0, 3.0)
# z2 = Complex(1.0,-4.0)
#
# print(z1)
# print(z2)
# print(z1 + z2)
# print(z1 * z2)
# print(abs(z1))
