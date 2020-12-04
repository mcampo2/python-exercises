#!/usr/bin/env python3

# (Turtle: draw a star) Write a program that prompts the user to enter the length of
# the star and draw a star, as shown in Figure 3.5a. (Hint: The inner angle of each
# point in the star is 36 degrees.)

import turtle

length = eval(input("Enter the length of the star: "))

turtle.right(36 * 2)
turtle.forward(length)
turtle.right(36 * 4)
turtle.forward(length)
turtle.right(36 * 4)
turtle.forward(length)
turtle.right(36 * 4)
turtle.forward(length)
turtle.right(36 * 4)
turtle.forward(length)

turtle.done()
