#!/usr/bin/env python3

# (Turtle: draw a circle) Write a program that prompts the user to enter the
# center and radius of a circle, and then displays the circle and its area, as shown
# in Figure 2.5.

import turtle

PI = 3.1415
x,y = eval(input("Enter the center of a circle: "))
radius = eval(input("Enter the radius of a circle: "))
area = radius * radius * PI
area = round(area * 100) / 100

turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write(area)

turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()

turtle.circle(radius)

turtle.done()
