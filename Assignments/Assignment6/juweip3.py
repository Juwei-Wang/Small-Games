import math
import stdarray
import stdaudio
import stdrandom
import stddraw
import collections

class GuitarString:
    def __init__(self, frequency):
        self.p = math.ceil(44100/frequency)
        self.y = 0
        self.list = [0] * self.p
        self.deque = collections.deque(self.list)

    def pluck(self):
        for i in range(self.p):
            self.list[i] = stdrandom.uniformFloat(-0.5,0.5)
        self.deque = collections.deque(self.list)
        return self.deque

    def tick(self):
        self.y = ((self.deque[0] + self.deque[1]) / 2) * 0.996
        self.deque.append(self.y)
        self.deque.popleft()
        return self.y














