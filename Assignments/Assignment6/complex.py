"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


Our own implementation (pedagogical example) of a complex number data type.
See Program 3.2.6 in the text for a similar, more concise example.
"""
import math

class Complex:
    """
    Our own implementation of a complex number data type that supports
    addition, multiplication, magnitude
    """

    def __init__(self, real=0.0, imag=0.0):
        # declare our class instance variables
        self._real = real
        self._imag = imag

    def re(self):
        return self._real

    def im(self):
        return self._imag

    def __add__(self, other):
        real = self.re() + other.re()
        imag = self.im() + other.im()
        return Complex(real, imag)

    def __mul__(self, other):
        real = self.re() * other.re() - self.im() * other.im()
        imag = self.re() * other.im() + self.im() * other.re()
        return Complex(real, imag)

    def __abs__(self):
        """
        :return: magnitude of this complex number (real value)
        """
        return math.sqrt(self.re() ** 2.0 + self.im() ** 2.0)

    def __str__(self):
        s = str(self.re()) + ' + ' + str(self.im()) + 'i'
        return s
