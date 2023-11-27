import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Whack-a-Mole Game Background")
wn.bgcolor("green")
wn.setup(width=800, height=800)  # Increase the width to provide more space

# Create a 3x4 grid of holes where moles can appear
holes = []

for row in range(3):
    for col in range(4):
        hole = turtle.Turtle()
        hole.shape("circle")
        hole.color("white")
        hole.shapesize(3)  # Make the circles larger
        hole.penup()
        x = col * 150 - 225  # Adjusted starting position for centering
        y = row * 150 - 150
        hole.goto(x, y)
        holes.append(hole)

# Main game loop (you can add your mole logic here)
while True:
    # Your game logic goes here
    pass

# Close the window when clicked
wn.exitonclick()
