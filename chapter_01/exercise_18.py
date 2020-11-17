#/usr/bin/env python3

# (Turtle: draw a star) Write a program that draws a star, as shown in Figure 1.19c.
# (Hint: The inner angle of each point in the star is 36 degrees.)

import turtle

turtle.right(36+36)
turtle.forward(180)
turtle.right(180-36)
turtle.forward(180)
turtle.right(180-36)
turtle.forward(180)
turtle.right(180-36)
turtle.forward(180)
turtle.right(180-36)
turtle.forward(180)

turtle.done()
