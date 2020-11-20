#!/usr/bin/env python3

# (Financial application: calculate interest) If you know the balance and the annual
# percentage interest rate, you can compute the interest on the next monthly pay-
# ment using the following formula:

#   interest = balance * (annualInterestRate / 1200)

# Write a program that reads the balance and teh annual percentage interest rate
# and displays the interest for the next month. Here is a sample run:

#   Enter balance and interest rate (e.g., 3 for 3%): 1000, 3.5 [Enter]
#   The interest is 2.91667

balance, interestRate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))
annualInterestRate = interestRate
interest = balance * annualInterestRate / 1200
interest = round(interest * 100000) / 100000
print("The interest is", interest)
