#!/usr/bin/env python3

# (Physics: find runway length) Given an airplane's acceleration a and take-off
# speed v, you can compute the minimum runway length needed fro an airplane to
# take off using the following formula:

#   length = v²/2a

# Write a program that prompts the user to enter v in meters/second (m/s) and the
# acceleration a in meters/second squared (m/s²), and displays the minimum runway
# length. Here is a  sample run:

#   Enter speed and acceleration: 60, 3.5 [Enter]
#   The minimum runway length for this airplane is 514.286 meters

speed, acceleration = eval(input("Enter speed and acceleration: "))
length = speed ** 2 / (2 * acceleration)
length = round(length * 1000) / 1000
print("The minimum runway length for this airplane is", length, "meters")
