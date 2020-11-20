#!/usr/bin/env python3

# (Health application: compute BMI) Body mass index (BMI) is a measure of health
# based on weight. It can be calculated by taking your weight in kilograms and
# dividing it by the square of your height in meters. Write a program that prompts
# the user to enter a weight in pounds and height in inches and displays the BMI.
# Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters.
# Here is a sample run:

# Enter weight in pounds: 95.5 [Enter]
# Enter height in inches: 50 [Enter]
# BMI is 26.8573

pounds = eval(input("Enter weight in pounds: "))
inches = eval(input("Enter height in inches: "))
kilograms = pounds * 0.45359237
meters = inches * 0.0254
bmi = kilograms / meters ** 2
bmi = round(bmi * 10000) / 10000
print("BMI is", bmi)
