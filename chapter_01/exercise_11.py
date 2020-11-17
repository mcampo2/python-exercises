#!/usr/bin/env python3

# (Population projection) The US Census Bureau projects population based on the
# following assumptions:
#     One birth every 7 seconds
#     One death every 13 seconds
#     One new immigrant every 45 seconds
# Write a program to display the population for each of the next five years. Assume the
# current population is 312032486 and one year has 365 days. Hint: in Python, you
# can use integer division operator // to perform division. The result is an integer. For
# example, 5 //4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).

print("Population: " + str(312032486))
print("Population n+1:", (312032486 + round(365*24*60*60*(1/7 - 1/13 + 1/45) * 1)))
print("Population n+2:", (312032486 + round(365*24*60*60*(1/7 - 1/13 + 1/45) * 2)))
print("Population n+3:", (312032486 + round(365*24*60*60*(1/7 - 1/13 + 1/45) * 3)))
print("Population n+4:", (312032486 + round(365*24*60*60*(1/7 - 1/13 + 1/45) * 4)))
print("Population n+5:", (312032486 + round(365*24*60*60*(1/7 - 1/13 + 1/45) * 5)))
