#!/usr/bin/env python3

# (Random character) Write a program that displays a random uppercase letter
# using the time.time() function.

import time

time = time.time()
letter = time*10000000 % 26 + ord('A')
letter = chr(int(letter))
print("Random letter:", letter)
