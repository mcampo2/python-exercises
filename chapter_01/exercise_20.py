#!/usr/bin/env python3

# (Turtle: display a rectanguloid) Write a program that displays a rectanguloid, as
# shown in Figure 1.20b.

import turtle

# first rectangle
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

# line to second rectangle
turtle.right(30)
turtle.forward(25)
turtle.right(60)

# top line
turtle.forward(100)
# connector
turtle.right(120)
turtle.forward(25)
turtle.right(180)
turtle.forward(25)
turtle.right(150)

# right line
turtle.forward(50)
# connector
turtle.right(30)
turtle.forward(25)
turtle.right(180)
turtle.forward(25)
turtle.right(240)

# bottom line
turtle.forward(100)
# connector
turtle.right(300)
turtle.forward(25)
turtle.right(180)
turtle.forward(25)
turtle.right(330)

# left line
turtle.forward(50)
turtle.penup()
turtle.goto(1000, 1000)
turtle.pendown()

turtle.done()
