#!/usr/bin/env python3

# (Turtle: draw the Olympic symbol) Write a program that prompts the user to
# enter the radius of the rings and draws an Olympic symbol of five rings of the
# same size with the colors blue, black, red, yellow, and green as shown in
# Figure 3.5c

import turtle

turtle.pensize(8)

# blue
turtle.penup()
turtle.color("blue")
turtle.goto(-120, 30)
turtle.pendown()
turtle.circle(50)

# black
turtle.penup()
turtle.color("black")
turtle.goto(0, 30)
turtle.pendown()
turtle.circle(50)

# red
turtle.penup()
turtle.color("red")
turtle.goto(120, 30)
turtle.pendown()
turtle.circle(50)

# yellow
turtle.penup()
turtle.color("yellow")
turtle.goto(-60, -30)
turtle.pendown()
turtle.circle(50)

# green
turtle.penup()
turtle.color("green")
turtle.goto(60, -30)
turtle.pendown()
turtle.circle(50)

turtle.hideturtle()
turtle.done()
