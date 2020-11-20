#!/usr/bin/env python3

# (Turtle: draw four hexagons) Write a program that draws four hexagons in the
# center of the screen as shown in Figure 2.4b.

import turtle

# bottom left
turtle.right(30)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)

# top left
turtle.right(240)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)

turtle.penup()
turtle.goto(100, 0)
turtle.pendown()

# bottom right
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)

# bottom left
turtle.right(240)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)

# realign cursor
#turtle.right(90)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(210)

turtle.done()
