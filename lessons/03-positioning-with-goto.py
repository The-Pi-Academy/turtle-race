# Lesson 3: Positioning with goto()
# Learn how to move the turtle to specific coordinates

import turtle

# Set up the turtle
turtle.speed(5)
turtle.penup()

# Move to a specific position (x, y)
turtle.goto(-100, 100)
turtle.pendown()

# Draw a square at this position
for side in range(4):
    turtle.forward(50)
    turtle.right(90)

# Move to another position
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()

# Draw a triangle
for side in range(3):
    turtle.forward(60)
    turtle.right(120)

# Move to center
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Draw a circle
turtle.circle(30)

input('Press enter to close')