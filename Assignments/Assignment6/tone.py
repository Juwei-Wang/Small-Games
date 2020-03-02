"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


Fill and array with five notes of the chromatic scale, each as a one-second
simple tone, starting from concert A pitch (440 Hz), then play to stdaudio.
See Programs 1.5.8 and 2.1.4 in the course text for more sophisticated and
better documented examples that demonstrate the same concepts.
"""
def curve(list, i0, i1, var, scale):
    if n == 0:
        return

    xm = (i0 + i1) / 2.0
    var = var / scale
    delta = stdrandom.gaussian(0.0, math.sqrt(var))
    list.append(curve(list, xm, ))

    curve(x0, y0, xm, ym + delta, var / beta, beta, n - 1)
    curve(xm, ym + delta, x1, y1, var / beta, beta, n - 1)

import stdaudio
import math

SAMPLE_RATE = 44100
CONCERT_A = 440
DURATION = 5

# generate an array with 5 seconds of the A tone
# 44100 * 5 = 220500 samples

num_samples = SAMPLE_RATE * DURATION

# array of samples
samples = []
for i in range(num_samples):
    # time in seconds
    t = i / SAMPLE_RATE
    semitone = math.floor(t)
    f = CONCERT_A * (2 ** (semitone / 12.0))
    y = math.sin(2.0 * math.pi * f * t)
    samples += [y]

print(samples)
stdaudio.playSamples(samples)
stdaudio.wait()
help(stdaudio)