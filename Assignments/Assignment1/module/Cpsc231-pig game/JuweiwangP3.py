import sys
import random


rolling_number = int(sys.argv[1])
total = 0
total_times = 0
times_count = rolling_number

def one_round_times():
    global yours
    yours = 0
    global times
    times = 0
    while (yours != 1):
        yours = random.randrange(1, 7)
        times = times +1

while (times_count != 0):
    times_count = times_count - 1
    one_round_times()
    total_times = total_times + times

Average_time = total_times / rolling_number

print('Simulating', rolling_number,'turns')
print('Estimated expectation:',Average_time)