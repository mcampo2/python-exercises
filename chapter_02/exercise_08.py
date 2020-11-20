#!/usr/bin/env python3

# (Science: calculate energy) Write a program that calculates the energy needed to
# head water from an initial temperature to a final temperature. Your program should
# prompt the user to enter the amount of water in kilograms and the initial and final
# temperatures of the water. The formula to compute energy is

#   Q = M * (finalTemperature - initialTemperature) * 4184

# where M is the weight of water in kilograms, temperatures are in degrees Celsius,
# and energy Q is measured in joules. Here is a sample run:

# Enter the amount of water in kilograms: 55.5 [Enter]
# Enter the initial temperature: 3.5 [Enter]
# Enter the final temperature: 10.5 [Enter]
# The energy needed is 1625484.0

mass = eval(input("Enter the amount of water in kilograms: "))
initialTemperature = eval(input("Enter the initial temperature: "))
finalTemperature = eval(input("Enter the final temperature: "))
energy = mass * (finalTemperature - initialTemperature) * 4184
print("The energy need is", energy)
