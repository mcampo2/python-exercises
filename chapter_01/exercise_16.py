#!/usr/bin/env python3

# (Turtle: draw four circles) Write a program that draws four circles in the center of
# the screen, as shown in Figure 1.19a.

import turtle

turtle.circle(50)
turtle.right(180)
turtle.circle(50)

turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.circle(50)

turtle.right(180)
turtle.circle(50)

turtle.penup()
turtle.goto(100, -100)
turtle.pendown()

turtle.done()
