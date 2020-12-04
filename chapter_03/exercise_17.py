#!/usr/bin/env python3

# (Turtle: triangle area) Write a program that prompts the user to enter the three
# points p1, p2, and p3 for a triangle and display its area below the triangle, as
# shown in Figure 3.7a. The formula for computing the area of a triangle is given
# in Exercise 2.14.

import turtle

x1, y1 = eval(input("Enter point 1 (x1, y1): "))
x2, y2 = eval(input("Enter point 2 (x2, y2): "))
x3, y3 = eval(input("Enter point 3 (x3, y3): "))

area = (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
turtle.penup()
turtle.goto(min(x1, x2, x3)-50, min(y1, y2, y3)-50)
turtle.pendown()
turtle.write("The area of the triangle is " + format(area, ".1f"))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p1 (" + str(x1) + ", " + str(y1) + ")")
turtle.goto(x2, y2)
turtle.write("p2 (" + str(x2) + ", " + str(y2) + ")")
turtle.goto(x3, y3)
turtle.write("p3 (" + str(x3) + ", " + str(y3) + ")")
turtle.goto(x1, y1)

turtle.hideturtle()
turtle.done()
