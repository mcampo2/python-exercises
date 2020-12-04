#!/usr/bin/env python3

# (Turtle: display a STOP sign) Write a program that displays a STOP sign, as
# shown in Figure 3.5b. The hexagon is in red and the text is in white.

import turtle

turtle.penup()
turtle.right(90)
turtle.goto(-100, 0)
turtle.pendown()

turtle.begin_fill()
turtle.color("red")
turtle.circle(100, steps=6)
turtle.end_fill()

turtle.penup()
turtle.color("white")
turtle.goto(-60, -25)
turtle.write("STOP", font=("Times", 35, "bold"))
turtle.pendown()

turtle.hideturtle()
turtle.done()
