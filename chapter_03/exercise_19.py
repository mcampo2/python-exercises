#!/usr/bin/env python3

# (Turtle: draw a line) Write a program that prompts the user to enter two points
# and draw a line to connec the points and displays the coordinates of the points,
# as shown in Figure 3.7c.

import turtle

x1, y1 = eval(input("Enter point 1 (x1, y1): "))
x2, y2 = eval(input("Enter point 2 (x2, y2): "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("(" + str(x1) + ", " + str(y1) + ")")
turtle.goto(x2, y2)
turtle.write("(" + str(x2) + ", " + str(y2) + ")")

turtle.hideturtle()
turtle.done()
