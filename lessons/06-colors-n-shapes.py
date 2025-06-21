# Lesson 6: Colors and Shapes
# Learn how to change turtle colors and shapes

import turtle

# Create a turtle and set its properties
my_turtle = turtle.Turtle()
my_turtle.speed(6)

# Change the turtle's color
my_turtle.color('red')
my_turtle.forward(100)

# Change to a different color
my_turtle.color('blue')
my_turtle.right(90)
my_turtle.forward(100)

# Change the turtle's shape
my_turtle.shape('turtle')
my_turtle.color('green')
my_turtle.right(90)
my_turtle.forward(100)

# Try different shapes
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']

my_turtle.penup()
my_turtle.goto(-200, 0)

for i in range(len(shapes)):
    my_turtle.shape(shapes[i])
    my_turtle.color(colors[i])
    my_turtle.stamp()  # Leave a stamp of the turtle
    my_turtle.forward(60)

input('Press enter to close')