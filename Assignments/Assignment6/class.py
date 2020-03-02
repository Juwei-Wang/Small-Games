import math
import collections




class Circle: # note that class titles are capitalized (the filename is not)
	def __init__(self,diameter):
		self.radius = diameter / 2
		self.area = math.pi * (self.radius ** 2)
		self.circumference = math.pi * diameter
		self.data = collections.deque()
		# make sure you define data storage types as a property of each 		# object!! Python's creators recommend it so heed their command.

    def combine(self):
        for i in range(3):
            self.data.extend(0.0)
        # make note of how you can initialize data in a deque
        # it's different from lists and can
        # cause your brain some pain
        # replacing data in a deque
            self.data[0] = self.radius
            self.data[1] = self.circumference
            self.data[2] = self.area
        return self.data


bigboi = Circle(9999999)  # where that big ol' number is it's diameter
a = bigboi.data
print(a)
