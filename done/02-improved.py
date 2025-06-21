# IMPROVED TURTLE RACE - Compare this to the original!
# This version shows better programming practices that make code easier to read and maintain

import random
import turtle

# IMPROVEMENT #1: Using a list to store many colors instead of creating separate variables
# Original had: red = turtle.Turtle(), blue = turtle.Turtle(), etc.
# This is much cleaner and lets us have as many racers as we want!
colors = [
    'blue', 'green', 'khaki', 'maroon', 'orange', 'peru',
    'pink', 'purple', 'red', 'salmon', 'yellow'
]

# IMPROVEMENT #2: Using variables to store important numbers
# This makes it easy to change the race setup without hunting through code
players = []  # List to store all our racing turtles
players_start = 220  # Y-coordinate where first turtle starts
players_step = 40  # How far apart each turtle lane is


# IMPROVEMENT #3: Using functions to organize code
# Instead of repeating turtle setup code, we write it once in a function
def create_turtle(color, start_position):
    """
  Creates a racing turtle with the given color at the starting position.
  This is much better than copying the same 7 lines of code over and over!
  """
    # Create a new turtle instance
    new_turtle = turtle.Turtle()
    new_turtle.color(color)
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.goto(-230, start_position)  # Start on the left side
    new_turtle.pendown()

    # IMPROVEMENT #4: Add some randomness to make turtles face different directions
    # This makes the race more interesting visually
    if random.randint(0, 1) == 1:
        new_turtle.left(360)  # Spin left
    else:
        new_turtle.right(360)  # Spin right

    # Add this turtle to our list of players
    players.append(new_turtle)


# IMPROVEMENT #5: Better race track with start AND finish line numbers
# Original only had numbers at the start - this shows progress better
print("Drawing improved race track...")
turtle.speed(10)
turtle.penup()
turtle.goto(-200, 250)

for step in range(20):
    # Write step number at START of each section
    turtle.write(step + 1, align='center')
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()

    # IMPROVEMENT #6: Longer dashed lines (30 dashes vs 15)
    # Makes the track look more professional
    for dash in range(30):
        turtle.forward(10)  # Longer dashes (10 vs 7)
        turtle.penup()
        turtle.forward(5)  # Bigger gaps (5 vs 3)
        turtle.pendown()

    turtle.penup()
    turtle.forward(20)  # Move to end of this section

    # IMPROVEMENT #7: Write step number at END too!
    # Now you can see progress from both sides
    turtle.pendown()
    turtle.write(step + 1, align='center')
    turtle.penup()

    # Move back to start the next lane
    turtle.backward(480)  # Go all the way back
    turtle.left(90)
    turtle.forward(20)  # Move down to next lane

# IMPROVEMENT #8: Random turtle order each race!
# Original always had red, blue, green, yellow in same order
# This shuffles the colors so each race is different
random.shuffle(colors)
print(f"Today's racers: {colors}")

# IMPROVEMENT #9: Using loops and math instead of hardcoded positions
# Original had: goto(-160, 100), goto(-160, 80), goto(-160, 60), goto(-160, 40)
# This calculates positions automatically based on how many turtles we have
for color in colors:
    # Calculate where this turtle should start
    start_y = players_start - len(players) * players_step
    create_turtle(color, start_y)

print(f"Created {len(players)} racing turtles!")

# IMPROVEMENT #10: More exciting race with variable speed
# Original: each turtle moved 1-5 steps
# New: each turtle moves 1-15 steps (more variation = more excitement!)
print("Ready... Set... GO!")
for turn in range(50):  # 50 turns instead of 100 (but turtles move faster)
    for player in players:
        # Each turtle moves a random amount between 1-15
        player.forward(random.randint(1, 15))

# IMPROVEMENT #11: Automatic winner detection!
# Original code didn't determine who won
# This finds the turtle that went the farthest
max_distance = 0
winner = None

for player in players:
    # Get the turtle's X position (how far right it went)
    current_position = player.pos()[0]  # pos() returns (x, y), we want x
    if current_position > max_distance:
        max_distance = current_position
        winner = player

# IMPROVEMENT #12: Winner celebration!
# Make the winning turtle do a victory spin
if winner:
    print(f"The winner is the {winner.pencolor()} turtle!")
    winner.right(1710)  # Spin around multiple times (1710 = 4.75 full rotations)
else:
    print("It's a tie!")

print("Race complete!")
input('Press enter to quit')

# SUMMARY OF IMPROVEMENTS:
# 1. Uses lists instead of separate variables for each turtle
# 2. Uses variables for important settings (easy to modify)
# 3. Uses functions to avoid repeating code
# 4. Adds visual variety with random turtle directions
# 5. Better race track with numbers on both ends
# 6. Longer, more professional-looking dashed lines
# 7. Shows progress markers on both sides of track
# 8. Random turtle order each race
# 9. Automatic positioning using math instead of hardcoded values
# 10. More exciting race with higher speed variation
# 11. Automatic winner detection
# 12. Winner celebration animation
#
# These improvements make the code:
# - Easier to read and understand
# - Easier to modify (want 20 turtles? Just add colors!)
# - More exciting to watch
# - More professional looking
# - Better organized with functions