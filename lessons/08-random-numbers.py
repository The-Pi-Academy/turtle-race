# Lesson 8: Random Numbers
# Learn how to use random numbers to create unpredictable movement

import turtle
from random import randint

turtle.speed(10)

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.color('purple')
my_turtle.shape('turtle')

# Move randomly
print("Moving randomly...")
for step in range(20):
    # Random distance between 10 and 50
    distance = randint(10, 50)
    my_turtle.forward(distance)

    # Random turn between 0 and 360 degrees
    angle = randint(0, 360)
    my_turtle.right(angle)

# Reset position
my_turtle.penup()
my_turtle.goto(0, -100)
my_turtle.pendown()

# Random colors
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

print("Drawing with random colors...")
for step in range(10):
    # Pick a random color
    random_color = colors[randint(0, len(colors) - 1)]
    my_turtle.color(random_color)

    # Move a random distance
    my_turtle.forward(randint(20, 40))
    my_turtle.right(randint(60, 120))

input('Press enter to close')