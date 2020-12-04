#!/usr/bin/env python3

# (Geometry: area of a pentagon) The area of a pentagon can be computed using the
# following formula (s is the length of a side):

#   Area = (5 X s²) / (4 X tan(π/5))

# Write a program that prompts the user to enter the side of a pentagon and displays
# the area. Here is a sample run:

#   Enter the side: 5.5 [Enter]
#   The area of the pentagon is 53.04444136781625

import math

s = eval(input("Enter the side: "))
area = (5 * s ** 2) / (4 * math.tan(math.pi/5))
print("The area of the pentagon is", area)
