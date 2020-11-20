#!/usr/bin/env python3

# (Turtle: draw a rectangle) Write a program that prompts the user to enter the
# center of a rectangle, width, and height, and displays the rectangle, as shown in
# Figure 2.4c

import turtle

x, y = eval(input("Enter the center of a rectangle: "))
height = eval(input("Enter the height of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))

turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)

turtle.penup()
turtle.goto(1000, 1000)
turtle.pendown()

turtle.done()
