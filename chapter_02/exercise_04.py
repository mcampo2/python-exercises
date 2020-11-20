#!/usr/bin/env python3

# (Convert pounds into kilograms) Write a program that converts pounds into
# kilograms. The program prompts the user to enter a value in pounds, converts it to
# kilograms, and displays the result. One pound is 0.454 kilograms. Here is a
# sample run:

#   Enter a value in pounds: 55.5 [Enter]
#   55.5 pounds is 25.197 kilograms

pounds = eval(input("Enter a value in pounds: "))
kilograms = pounds * 0.454
print(pounds, "pounds is", kilograms, "kilograms")
