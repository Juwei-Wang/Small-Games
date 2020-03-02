"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


A simple (and largely incomplete) data type to keep track of time of day.
See Exercise 3.3.20 in the course text for relevant context and discussion.
"""

class Time:

    def __init__(self, h, m, s):
        self._h = h
        self._m = m
        self._s = s

    def hour(self):
        return self._h

    def minute(self):
        return self._m

    def second(self):
        return self._s

    def __eq__(self, other):
        if self.hour() == other.hour() \
            and self.minute() == other.minute() \
            and self.second() == o ther.second():
            return True
        return False

    def __str__(self):
        s = str(self._h) + ':' + str(self._m) + ':' + str(self._s)
        return s

# test code
if __name__ == '__main__':
    t = Time(16, 30, 2)
    t2 = Time(16, 30, 2)
    print(t.hour())
    print(t)
    equal = t == t2
    print(equal)
    print(id(t), id(t2))
