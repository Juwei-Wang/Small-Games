import sys
import random

yours = int(sys.argv[1])
rolling_number = int(sys.argv[2])
total = 0
value1 = 0

for i in range (rolling_number ):
    mine = random.randrange(1, 7)
    while (mine != 1):
        value1 = ((mine)*(1/6)) + value1


for i in range (rolling_number):
    yours = random.randrange(1, 7)
    total = total + yours

execpted_value = total / rolling_number

print('I love you', yours, mine, 'i hate you')
print(mine)
print(execpted_value)
print(yours)
print(total)