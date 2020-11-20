#!/usr/bin/env python3

# (Geometry: area of a hexagon) Write a program that prompts the user to enter the
# side of a hexagon and displays its area. The formula for computing the area of a
# hexagon is

#   Area = 3 * 3 ** 0.5 / 2 * s ** 2

# where s is the length of a side. Here is a sample run:

#   Enter the side: 5.5 [Enter]
#   The area of the hexagon is 78.5895

s = eval(input("Enter the side: "))
area = 3 * 3 ** 0.5 / 2 * s ** 2
area = round(area * 10000) / 10000
print("The area of the hexagon is", area)
