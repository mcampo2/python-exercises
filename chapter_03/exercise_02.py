#!/usr/bin/env python3

# (Geometry: great circle distance) The great circle distance is the distance between
# two points on the surface of a sphere. Let (x1, y2) and (x2, y2) be the geographical
# latitude and longitude of two points. The great circle distance between the two
# points can be computed using the following formula:

#   d = radius X arccos(sin(x₁) X sin(x₂) + cos(x₁) X cos(x₂) X cos(y₁ - y₂))

# Write a program that prompts the user to enter the latitude and longitude of two
# points on the earth in degrees and displays its great circle distance. The average
# earth radius is 6,371.01 km. Note that you need to convert the degrees into radians
# using the math.radians function since the Python trigonometric functions use
# radians. The latitude and longitude degrees in the formula are for north and west.
# Use negative to indicate south and east degrees. Here is a sample run:

#   Enter point 1 (latitude and longitude) in degrees:
#   39.55, -116.25 [Enter]
#   Enter point 2 (latitude and longitude) in degrees:
#   41.5, 87.37 [Enter]
#   The distance between the two points is 10691.79183231593 km

import math

RADIUS = 6371.01
x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

distance = RADIUS * math.acos(math.sin(x1) * math.sin(x2) \
    + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
print("The distance between the two points is", distance, "km")
