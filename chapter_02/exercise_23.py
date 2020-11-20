#!/usr/bin/env python3

# (Turtle: draw four circles) Write a program that prompt the user to enter the
# radius and draws four circles in teh center of the screen, as shown in Figure 2.4a.

import turtle

radius = eval(input("Enter the radius: "))

turtle.circle(radius)
turtle.right(180)
turtle.circle(radius)

turtle.penup()
turtle.goto(radius*2, 0)
turtle.pendown()
turtle.circle(radius)

turtle.right(180)
turtle.circle(radius)

turtle.penup()
turtle.goto(radius*2, -radius*2)
turtle.pendown()

turtle.done()
