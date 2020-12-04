#!/usr/bin/env python3

# (Geometry: area of a pentagon) Write a program that prompts the user to enter the
# length from the center of a pentagon to a vertex and computes the area of the pen-
# tagon, as shown in the following figure.

# The formula ofr computing the area of a pentagon is Area = (3√3)/2 * s², where s is
# the length of a side. The side can be computed using the formula s = 2r*sin(π/5),
# where r is the length from the center of a pentagon to a vertex. Here is a sample
# run:

#   Enter the length from the center to a vertex: 5.5 [Enter]
#   The area of the pentagon is 108.61

import math

radius = eval(input("Enter the length from the center to a vertex: "))
side = 2 * radius * math.sin(math.pi/5)
area = 3*3**0.5/2*side**2
print("The area of the pentagon is", round(area,2))
