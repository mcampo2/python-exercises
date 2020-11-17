#!/usr/bin/env python3

# (Turtle: display a clock) Writ a program that displays a clock to show the time
# 9:15:00, as shown in Figure 1.20c.

import turtle

# clock circle
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(150)

# hour hand
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.right(180)
turtle.forward(100)

# minute hand
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.right(180)
turtle.forward(100)

# second hand
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.right(270)
turtle.forward(125)

turtle.penup()
turtle.goto(135, 50)
turtle.write("3")

turtle.penup()
turtle.goto(-1, 185)
turtle.write("12")

turtle.penup()
turtle.goto(-135, 50)
turtle.write("9")

turtle.penup()
turtle.goto(0, -100)
turtle.write("6")

turtle.penup()
turtle.goto(-20, -125)
turtle.write("9:15:00")

turtle.done()
