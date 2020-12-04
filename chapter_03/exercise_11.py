#!/usr/bin/env python3

# (Reverse numbers) Write a program that prompts the user to enter a four-digit int-
# ger and displays the number in reverse order. Here is a sample run:

#   Enter an integer: 3125 [Enter]
#   The reversed number is 5213

reverse = ""
integer = eval(input("Enter an integer: "))
reverse += str(integer % 10)
integer //= 10
reverse += str(integer % 10)
integer //= 10
reverse += str(integer % 10)
integer //= 10
reverse += str(integer % 10)
integer //= 10

print("The reversed number is", reverse)
