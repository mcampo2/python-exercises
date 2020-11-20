#!/usr/bin/env python3

# (Split digits) Write a program that prompts the user to enter a four-digit integer
# and displays the number in reverse order. Here is a sample run:

#   Enter an integer: 3125 [Enter]
#   3
#   1
#   2
#   5

number = eval(input("Enter an integer: "))
print(number // 1000)
print(number % 1000 // 100)
print(number % 100 // 10)
print(number % 10 // 1)
