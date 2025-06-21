# Lesson 5: Writing Text with Turtle
# Learn how to write text and numbers with turtle

import turtle

turtle.speed(5)
turtle.penup()

# Write some text
turtle.goto(-100, 100)
turtle.write("Hello, Turtle!", align='left')

# Write text with different alignment
turtle.goto(0, 50)
turtle.write("Centered Text", align='center')

turtle.goto(100, 0)
turtle.write("Right Aligned", align='right')

# Write numbers in a pattern
turtle.goto(-150, -50)
for number in range(5):
    turtle.write(number, align='center')
    turtle.forward(50)

# Create a number line
turtle.goto(-100, -100)
for step in range(8):
    turtle.write(step * 10, align='center')
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.backward(30)
    turtle.left(90)
    turtle.forward(25)

input('Press enter to close')