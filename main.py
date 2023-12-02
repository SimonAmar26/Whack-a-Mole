import turtle
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Whack-a-Mole Game")
wn.bgpic("forest_BG.gif")
wn.setup(width=1100, height=700)  # Increase the width to provide more space
turtle.tracer(0,0)

# Make the mole appear on the holes
def appear_mole():
    pos = random.choice(coordinates)
    mole = turtle.Turtle()
    mole.shape("circle")
    mole.color("blue")
    mole.shapesize(3)
    mole.penup()
    mole.goto(pos)
    moles.append(mole)
    turtle.ontimer(appear_mole, 1000)

coordinates = [(-300,-250),(-100,-250),(100,-250),(300,-250),(-300,-150),(-100,-150),(100,-150),(300,-150),(-300,-50),(-100,-50),(100,-50),(300,-50)]
moles = []

appear_mole()

# Create a 3x4 grid of holes where moles can appear
holes = []

for row in range(3):
    for col in range(4):
        hole = turtle.Turtle()
        hole.shape("circle")
        hole.color("white")
        hole.shapesize(1)  # Make the circles larger
        hole.penup()
        x = col * 200 - 300  # Adjusted starting position for centering
        y = row * 100 - 250
        hole.goto(x, y)
        holes.append(hole)

# Main game loop (you can add your mole logic here)
while True:
    # Your game logic goes here
    wn.update()

# Close the window when clicked
wn.exitonclick()
