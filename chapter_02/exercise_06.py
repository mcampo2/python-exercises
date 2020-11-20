#!/usr/bin/env python3

# (Sum the digits in an integer) Write a program that reads an integer between 0 and
# 1000 and adds all the digits in the integer. For example, if an integer is 932, the
# sum of all it's digits is 14. (Hint: Use the % operator to extract digits, and use the //)
# operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
# 10 = 93.) Here is a sample run:

#   Enter a number between 0 and 1000: 999 [Enter]
#   The sum of the digits is 27

number = eval(input("Enter a number between 0 and 1000: "))
sum = number // 1000
sum += number % 1000 // 100
sum += number % 100 // 10
sum += number % 10
print("The sum of the digits is", sum)
