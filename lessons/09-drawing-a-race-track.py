# Lesson 9: Drawing a Race Track
# Learn how to create a race track with finish lines

import turtle

turtle.speed(10)
turtle.penup()

# Start position for the track
turtle.goto(-140, 140)

# Draw the race track with numbered lanes
print("Drawing race track...")
for lane in range(4):
    # Write the lane number
    turtle.write(f"Lane {lane + 1}", align='center')

    # Move down and start drawing the lane
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()

    # Draw dashed finish line
    for dash in range(15):
        turtle.forward(7)  # Draw dash
        turtle.penup()
        turtle.forward(3)  # Gap
        turtle.pendown()

    # Move back to start of lane and prepare for next lane
    turtle.penup()
    turtle.backward(160)  # Go back to start
    turtle.left(90)  # Face right again
    turtle.forward(40)  # Move to next lane position

print("Race track complete!")
input('Press enter to close')