import sys
import random

rolling_number = int(sys.argv[1])
total = 0


for i in range (rolling_number):
    yours = random.randrange(1, 7)
    total = total + yours

Estimated_value = total / rolling_number

print('Rolling', rolling_number, 'times')
print('Estimated expectation:', Estimated_value)