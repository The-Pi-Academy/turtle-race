# Lesson 7: Multiple Turtles
# Learn how to create and control multiple turtles

import turtle

# Set up the screen
turtle.speed(8)

# Create multiple turtle objects
red_turtle = turtle.Turtle()
blue_turtle = turtle.Turtle()
green_turtle = turtle.Turtle()

# Set up the red turtle
red_turtle.color('red')
red_turtle.shape('turtle')
red_turtle.penup()
red_turtle.goto(-100, 100)
red_turtle.pendown()

# Set up the blue turtle
blue_turtle.color('blue')
blue_turtle.shape('turtle')
blue_turtle.penup()
blue_turtle.goto(-100, 0)
blue_turtle.pendown()

# Set up the green turtle
green_turtle.color('green')
green_turtle.shape('turtle')
green_turtle.penup()
green_turtle.goto(-100, -100)
green_turtle.pendown()

# Make each turtle draw something different
print("Red turtle drawing a square...")
for side in range(4):
    red_turtle.forward(50)
    red_turtle.right(90)

print("Blue turtle drawing a triangle...")
for side in range(3):
    blue_turtle.forward(60)
    blue_turtle.right(120)

print("Green turtle drawing a circle...")
green_turtle.circle(30)

input('Press enter to close')