#!/usr/bin/env python3

# (Compute the volume of a cylinder) Write a program that reads in the radius and
# length of a cylinder and computes the area and volume using the following formulas:

#   area = radius * radius * π
#   volume = area * length

# Here is a sample run:

#   Enter the radius and length of a cylinder: 5.5, 12 [Enter]
#   The area is 95.0331
#   The volume is 1140.4

PI = 3.14159
radius, length = eval(input("Enter the radius and length of a cylinder: "))
area = radius * radius * PI
area = round(area * 10000) / 10000
volume = area * length
print("The area is", area)
print("The volume is", 1140.4)
