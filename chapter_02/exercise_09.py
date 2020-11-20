#!/usr/bin/env python3

# (Science: wind-chill temperature) How cold is it outside? The temperature alone is
# not enough to provide the answer. Other factors including wind speed, relative
# humidity, and sunshine play important roles in determining coldness outside. In
# 2001, the National Weather Service (NWS) implemented the new wind-chill tem-
# perature to measure the coldness using temperature and wind speed. The formula
# is given as follows:

#   tₓ = 35.74 + 0.6215tₐ - 35.75v⁰·¹⁶ + 0.4275tₐv⁰·¹⁶

# where tₐ is the outside temperature measured in degrees Fahrenheit and v is the
# speed measured in miles per hour. tₓ is the wind-chill temperature. The formula
# cannot be used for wind speeds below 2 mph or for temperatures below -58°F or
# above 41°F

# Write a program that prompts the user to enter a temperature between -58°F and
# 41°F and a wind speed greater than or equal to 2 and displays the wind-chill tem-
# perature. Here is a sample run:

# Enter the temperature in Fahrenheit between -58 and 41: 5.3 [Enter]
# Enter the wind speed in miles per hour: 6 [Enter]
# The wind chill index is -5.56707

temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
windSpeed = eval(input("Enter the wind speed in miles per hour: "))
windChill = 35.74 + 0.6215*temperature - 35.75*windSpeed**0.16 \
            + 0.4275*temperature*windSpeed**0.16
windChill = round(windChill * 100000) / 100000
print("The wind chill index is", windChill)
