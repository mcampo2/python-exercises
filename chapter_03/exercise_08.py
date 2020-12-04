#!/usr/bin/env python3

# (Financial application: monetary units) Rewrite Listing 3.4, ComputeChange.py,
# to fix the possible loss of accuracy when converting a float value to an int value.
# Enter the input as an integer whose last two digits represent the cents. For exam-
# ple, the input 1156 represents 11 dollars and 56 cents.

# Receive the amount
amount = eval(input("Enter an amount in cents, for example, 1156: "))

# Convert the amount to cents
# remainingAmount = int(amount * 100)
remainingAmount = amount

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print("Your amount of", amount, "cents consists of\n"
    "\t", numberOfOneDollars, "dollars\n",
    "\t", numberOfQuarters, "quarters\n",
    "\t", numberOfDimes, "dimes\n",
    "\t", numberOfNickels, "nickels\n",
    "\t", numberOfPennies, "pennies")
