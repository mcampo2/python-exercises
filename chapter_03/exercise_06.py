#!/usr/bin/env python3

# (Find the character of an ASCII code) Write a program that recieves an ASCII
# code (an integer between 0 and 127) and displays its character. For example, if the
# user enters 97, the program displays the character a. Here is a sample run:

#   Enter an ASCII code: 69 [Enter]
#   The character is E

code = eval(input("Enter an ASCII code: "))
print("The character is", chr(code))
