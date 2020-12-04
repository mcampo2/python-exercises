#!/usr/bin/env python3

# (Turtle: paint a smiley face) Write a program that paints a smiley face, as shown in
# Figure 3.6a.

import turtle

# circle
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(100)

# left eye
turtle.penup()
turtle.goto(-50, 75)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# right eye
turtle.penup()
turtle.goto(50, 75)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# nose
turtle.penup()
turtle.goto(-30, 0)
turtle.pendown()
turtle.goto(0, 60)
turtle.goto(30, 0)

# mouth
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.goto(0, -25)
turtle.goto(50, 0)

turtle.hideturtle()
turtle.done()
