#!/usr/bin/env python3

# (Find the number of years and days) Write a program that prompts the user to
# enter the minutes (e.g., 1 billion), and displays the number of years and days for
# the minutes. For simplicity, assume a year has 365 days. Here is a sample run:

#   Enter the number of minutes: 1000000000 [Enter]
#   1000000000 minutes is approximately 1902 years and 214 days

minutes = eval(input("Enter the number of minutes: "))
years = minutes // 60 // 24 // 365
days = minutes // 60 // 24 % 365
print(minutes, "minutes is approximately", years, "years and", days, "days")
