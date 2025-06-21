# Lesson 4: Loops and Patterns
# Learn how to use loops to create patterns

import turtle

turtle.speed(8)

# Simple loop to draw a square
print("Drawing a square with a loop:")
for side in range(4):
    turtle.forward(100)
    turtle.right(90)

# Move to new position
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

# Loop to create dashed line
print("Drawing a dashed line:")
for dash in range(10):
    turtle.forward(10)  # Draw
    turtle.penup()
    turtle.forward(5)   # Gap
    turtle.pendown()

# Move to new position
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

# Loop to create a star pattern
print("Drawing a star:")
for point in range(5):
    turtle.forward(100)
    turtle.right(144)

input('Press enter to close')