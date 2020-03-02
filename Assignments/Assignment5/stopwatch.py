"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


Abstraction of a stopwatch that we can use to time things in our program.
See Program 3.2.2 in the text for a similar, more concise example.
"""

import time
import math

# step 0: declare our class name
class Stopwatch:
    # step 1: define a constructor
    def __init__(self):
        """
        Set up the initial state of my object
        """
        # instance variable to keep track of elapsed time
        self._elapsed_time = 0.0
        # instance variable to remember when we started the watch
        self._start_time = 0.0

    # step 2: define methods (operations) for using a stopwatch
    def start(self):
        # remember the time we hit start for later
        self._start_time = time.time()

    def stop(self):
        # add to the elapsed time, the time between now and when we started
        dt = time.time() - self._start_time
        self._elapsed_time += dt

    def lap(self):
        # haven't implemented this yet
        pass

    def reset(self):
        self._elapsed_time = 0.0

    def elapsed(self):
        """
        :return: number of seconds on the readout (elapsed time after hitting stop)
        """
        return self._elapsed_time


# let's test our stopwatch
if __name__ == '__main__':
    # create a stopwatch
    timer = Stopwatch()
    # time how long it takes to compute 1000000 square roots?
    timer.start()
    for i in range(1000000):
        math.sqrt(float(i))
    timer.stop()

    seconds = timer.elapsed()
    print('It took', seconds, 'seconds to compute 1000000 square roots!')
