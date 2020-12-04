#!/usr/bin/env python3

# (Turtle: triangle angles) Revise Listing 3.2, ComputeAngles.py, to write a pro-
# gram that prompts the user to enter the three points p1, p2, and p3 for a triangle
# and displays its angles, as shown in Figure 3.7b.

import math
import turtle

x1, y1 = eval(input("Enter point 1 (x1, y1): "))
x2, y2 = eval(input("Enter point 2 (x2, y2): "))
x3, y3 = eval(input("Enter point 3 (x3, y3): "))

a = math.sqrt((x2-x3)**2 + (y2-y3)**2)
b = math.sqrt((x1-x3)**2 + (y1-y3)**2)
c = math.sqrt((x1-x2)**2 + (y1-y2)**2)

A = math.degrees(math.acos((a**2-b**2-c**2)/(-2*b*c)))
B = math.degrees(math.acos((b**2-a**2-c**2)/(-2*a*c)))
C = math.degrees(math.acos((c**2-a**2-b**2)/(-2*a*b)))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p1 (" + format(A,".2f") + ")")
turtle.goto(x2, y2)
turtle.write("p2 (" + format(B,".2f") + ")")
turtle.goto(x3, y3)
turtle.write("p3 (" + format(C,".2f") + ")")
turtle.goto(x1, y1)

turtle.hideturtle()
turtle.done()
