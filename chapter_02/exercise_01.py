#!/usr/bin/env python3

# (Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from
# the console and converts it to Fahrenheit and displays the result. The formula for
# the conversion is a s follows:

#   fahrenheit = (9 / 5) * celsius + 32

# Here is a sample run of the program:

#   Enter a degree in Celsius: 43 [Enter]
#   43 Celsius is 109.4 Fahrenheit

celsius = eval(input("Enter a degree in Celsius: "))
fahrenheit = (9 / 5) * celsius + 32

print(celsius, "Celsius is", fahrenheit, "Fahrenheit")
