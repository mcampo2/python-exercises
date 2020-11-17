#!/usr/bin/env python3

# (Turtle: draw a cross) Write a program that draws a cross as shown in Figure 1.18b.

import turtle

turtle.forward(100)
turtle.penup()

turtle.right(180)
turtle.forward(50)

turtle.right(90)
turtle.forward(50)

turtle.pendown()
turtle.right(180)
turtle.forward(100)

turtle.done()
