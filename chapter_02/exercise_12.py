#!/usr/bin/env python3

# (Print a table) Write a program that displays the folowing table:

#   a     b     a ** b
#   1     2     1
#   2     3     8
#   3     4     81
#   4     5     1024
#   5     6     15625

print("a     b     a ** b")
a = 1
print(a, "   ", a + 1, "   ", a ** (a + 1))
a = 2
print(a, "   ", a + 1, "   ", a ** (a + 1))
a = 3
print(a, "   ", a + 1, "   ", a ** (a + 1))
a = 4
print(a, "   ", a + 1, "   ", a ** (a + 1))
a = 5
print(a, "   ", a + 1, "   ", a ** (a + 1))
