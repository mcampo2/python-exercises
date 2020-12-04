#!/usr/bin/env python3

# (Geography: estimate areas) Find the GPS locations for Atlanta, Georgia;
# Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
# www.gps-data-team.com/map/ and compute the estimated area enclosed by these
# four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
# distance between two cities. Divide the polygon into two triangles and use the for-
# mula in Programming Exercise 2.14 to compute the area of a triangle.)

import math

RADIUS = 6371.01
x1, y1 = (33.72427,-84.57858) # Atlanta, Georgia
x2, y2 = (28.41153,-81.52504) # Orlando, Florida
x3, y3 = (32.00849,-81.21437) # Savannah, Georgia
x4, y4 = (35.13361,-80.96363) # Charlotte, North Carolina

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)
x3 = math.radians(x3)
y3 = math.radians(y3)
x4 = math.radians(x4)
y4 = math.radians(y4)

distance1 = RADIUS * math.acos(math.sin(x1) * math.sin(x2) \
    + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
distance2 = RADIUS * math.acos(math.sin(x2) * math.sin(x3) \
    + math.cos(x2) * math.cos(x3) * math.cos(y2 - y3))
distance_ = RADIUS * math.acos(math.sin(x1) * math.sin(x3) \
    + math.cos(x1) * math.cos(x3) * math.cos(y1 - y3))
distance3 = RADIUS * math.acos(math.sin(x3) * math.sin(x4) \
    + math.cos(x3) * math.cos(x4) * math.cos(y3 - y4))
distance4 = RADIUS * math.acos(math.sin(x4) * math.sin(x1) \
    + math.cos(x4) * math.cos(x1) * math.cos(y4 - y1))

s1 = (distance1 + distance2 + distance_) / 2
s2 = (distance3 + distance4 + distance_) / 2

area1 = (s1 * (s1 - distance1) * (s1 - distance2) * (s1 - distance_)) ** 0.5
area2 = (s2 * (s2 - distance3) * (s2 - distance4) * (s2 - distance_)) ** 0.5
area = area1 + area2
area = round(area * 100) / 100

print("The area is", area, "km")
