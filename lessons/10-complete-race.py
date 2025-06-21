# Lesson 10: Complete Turtle Race
# Putting it all together - a full turtle racing game!

import turtle
from random import randint

# Set up the race track
turtle.speed(10)
turtle.penup()
turtle.goto(-140, 140)

print("Setting up the race track...")
for step in range(4):
    turtle.write(f"Lane {step + 1}", align='center')
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()

    # Draw dashed finish line
    for dash in range(15):
        turtle.forward(7)
        turtle.penup()
        turtle.forward(3)
        turtle.pendown()

    turtle.penup()
    turtle.backward(160)
    turtle.left(90)
    turtle.forward(40)

# Create racing turtles
print("Creating racing turtles...")

red = turtle.Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-160, 115)

blue = turtle.Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-160, 90)

green = turtle.Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-160, 65)

yellow = turtle.Turtle()
yellow.color('yellow')
yellow.shape('turtle')
yellow.penup()
yellow.goto(-160, 40)

# Start the race!
print("Ready... Set... GO!")
for turn in range(100):
    red.forward(randint(1, 5))
    blue.forward(randint(1, 5))
    green.forward(randint(1, 5))
    yellow.forward(randint(1, 5))

print("Race finished!")
input('Press enter to close')