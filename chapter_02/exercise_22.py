#!/usr/bin/env python3

# (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
# number of years and displays the population after that many years. Here is a
# sample run of the program:

# Enter the number of years: 5 [Enter]
# The population in 5 years is 325932970

years = eval(input("Enter the number of years: "))
population = 312032486 + round(365*24*60*60*(1/7 - 1/13 + 1/45) * years)
print("The population in", years, "years is", population)
