#!/usr/bin/env python3

# (Financial application: investment amount) Suppose you want to deposit a
# certain amount of money into a savings account with a fixed annual interest rate.
# What amount do you need to deposit in order to have $5,000 in the account after
# three years? The initial deposit amount can be obtained using the following
# formula:

#   initialDepositAmount = finalAccountValue / (1 + monthlyInterestRate) ** numberOfMonths

# Write a program that prompts the user to enter final account value, annual interest
# rate in percent, and the number of years, and displays teh initial deposit amount.
# Here is a sample run:

#   Enter final account value: 1000 [Enter]
#   Enter annual interest rate in percent: 4.25 [Enter]
#   Enter number of years: 5 [Enter]
#   Initial deposit value is 808.8639197424636

finalAccountValue = eval(input("Enter final account value: "))
monthlyInterestRate = eval(input("Enter annual interest rate in percent: ")) / 100 / 12
numberOfMonths = eval(input("Enter number of years: ")) * 12
initialDepositAmount = finalAccountValue / (1 + monthlyInterestRate) ** numberOfMonths
print("Initial deposit value is", initialDepositAmount)
