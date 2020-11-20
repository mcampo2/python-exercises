#!/usr/bin/env python3

# (Physics: acceleration) Average acceleration is defined as the change of velocity
# divided by the time taken to make the change, as shown in the following formula:

#   a = (v₁ - v₀) / t

# Write a program that prompts the user to enter the starting velocity v₀ in
# meters/second, and ending velocity v₁ in meters/second and the time span t in
# seconds, and displays the average acceleration. Here is a sample run:

#   Enter v0, v1, and t: 5.5, 50.9, 4.5 [Enter]
#   The average acceleration is 10.0889

v0, v1, t = eval(input("Enter v0, v1, and t: "))
a = (v1 - v0) / t
a = round(a * 10000) / 10000
print("The average acceleration is", a)
