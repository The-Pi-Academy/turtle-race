# Lesson 2: Pen Control and Speed
# Learn how to control the pen and turtle speed

import turtle

# Set turtle speed (1-10, or 0 for fastest)
turtle.speed(5)

# Draw a line
turtle.forward(100)

# Lift the pen up (no drawing)
turtle.penup()
turtle.forward(50)

# Put the pen down (start drawing again)
turtle.pendown()
turtle.forward(100)

# Try different speeds
turtle.speed(1)  # Slowest
turtle.right(90)
turtle.forward(50)

turtle.speed(10)  # Fast
turtle.right(90)
turtle.forward(50)

input('Press enter to close')