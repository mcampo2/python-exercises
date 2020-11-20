#!/usr/bin/env python3

# (Financial application: calculate future investment value) Write a program that
# reads in an investment amount, the annual interest rate, and the number of years,
# and displays the future investment value using the following formula:

#   futureInvestmentValue = investmentAmount X (1 + monthlyInterestRate)ⁿᵘᵐᵇᵉʳᴼᶠᴹᵒⁿᵗʰˢ

# For example, if you enter the amount 1000, an annual interest rate of 4.25%,
# and the number of years as 1, the future investment value is 1043.33. Here is a
# sample run:

#   Enter investment amount: 1000 [Enter]
#   Enter annual interest rate: 4.25 [Enter]
#   Enter number of years: 1 [Enter]
#   Accumulated value is 1043.33

investmentAmount = eval(input("Enter investment amount: "))
monthlyInterestRate = eval(input("Enter annual interest rate: ")) / 100 / 12
numberOfMonths = eval(input("Enter number of years: ")) * 12
futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths
futureInvestmentValue = int(futureInvestmentValue * 100) / 100
print("Accumulated value is", futureInvestmentValue)
