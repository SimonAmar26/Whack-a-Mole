import turtle
import time
import random

# Function to set up the turtle tab 

wn = turtle.Screen()
wn.title("Whack a Mole")
wn.bgpic("rules.gif")
wn.setup(width=1200, height=750)
turtle.tracer(0,0)

# Function to set the background(s)

def BG_def(x,y) :
    print(0)
    global BGv, wn
    if x >= 0 :
        wn.bgpic('forest_BG.gif')
    else :
        wn.bgpic('desert_BG.gif')
    BGv = True

# Function to set a timer

def timer() :
    global t_remaining,t
    if t > 0 :
        timer_list[t-1].clear()
    timer_list[t] = turtle.Turtle()
    timer_list[t].hideturtle()
    timer_list[t].penup()
    timer_list[t].goto(0, 330)
    timer_list[t].write(f'The remaining time is {t_remaining}', align="center", font=("Arial", 40 ,"bold"))
    turtle.update()
    t_remaining -= 1
    t += 1
    if t_remaining >= 0 :
        wn.ontimer(timer, 1000)
    else:
        timer_list[t-1].clear()

# Function to display a text in the middle of the screen

def print_text(text, duration) :
    hello = turtle.Turtle()
    hello.hideturtle()
    hello.penup()
    hello.goto(0, 0)
    hello.write(text, align="center", font=("Arial", 50 ,"bold"))
    turtle.update()
    time.sleep(duration)
    hello.clear()

# Function to count the points

def counter() :
    global count_text, count,c
    if c > 0 :
        count_text[c-1].clear()
    count_text[c] = turtle.Turtle()
    count_text[c].hideturtle()
    count_text[c].penup()
    count_text[c].goto(0, 280)
    count_text[c].write(f'Your score: {count}', align="center", font=("Arial", 30, "bold"))
    c += 1

# Function to set random coordinates for the apparition of the yellow moles that are worth 1 point when hit 

def phase_1() :
    global i, coordinates
    t_app = random.randrange(200,1200)
    pos1[i] = random.randrange(0, len(coordinates))
    pos2[i] = coordinates.pop(pos1[i])
    x, y = pos2[i]
    mole_created[i] = turtle.Turtle()
    mole_created[i].shape("yellow_mole.gif")
    shape[i] = mole_created[i].shape()
    mole_created[i].penup()
    mole_created[i].goto(x,y)
    wn.update
    i += 1
    if i > 4 :
        disappear()
    wn.update
    if i < 100 :
        wn.ontimer(phase_1,t_app)

# Function to set random coordinates for the apparition of the red moles that are worth 3 points when hit 
def phase_2() :
    global i, coordinates
    t_app = random.randrange(2000,4000)
    pos1[i] = random.randrange(0, len(coordinates))
    pos2[i] = coordinates.pop(pos1[i])
    x, y = pos2[i]
    mole_created[i] = turtle.Turtle()
    mole_created[i].shape("red_mole.gif")
    shape[i] = mole_created[i].shape()
    mole_created[i].penup()
    mole_created[i].goto(x,y)
    wn.update
    i += 1
    if i > 4 :
        disappear()
    wn.update
    if i < 100 :
        wn.ontimer(phase_2,t_app)

# Function to set random coordinates for the apparition of the green moles that are worth 5 points when hit
def phase_3() :
    global i, coordinates
    t_app = random.randrange(7000,8000)
    pos1[i] = random.randrange(0, len(coordinates))
    pos2[i] = coordinates.pop(pos1[i])
    x, y = pos2[i]
    mole_created[i] = turtle.Turtle()
    mole_created[i].shape("green_mole.gif")
    shape[i] = mole_created[i].shape()
    mole_created[i].penup()
    mole_created[i].goto(x,y)
    wn.update
    i += 1
    if i > 4 :
        disappear()
    wn.update
    if i < 80 :
        wn.ontimer(phase_3,t_app)

# Function to detect the click of the player

def detect_click(x, y) :
    global i, count, total
    for zone in zones :
        if zone[0] < x < zone[2] and zone[3] > y > zone[1] :
            index_zone = zones.index(zone)
            position_mole = fixed_coordinates[index_zone]
            for a in range(i-5,i) :
                if pos2[a] == position_mole :
                    mole_created[a].hideturtle()
                    if shape[a] == 'yellow_mole.gif' :
                        count += 1
                    elif shape[a] == 'red_mole.gif' :
                        count += 3
                    elif shape[a] == 'green_mole.gif' :
                        count += 5

# Function to hide the mole after they appear

def disappear() :
    global total
    mole_created[i-4].hideturtle()
    coordinates.insert(pos1[i-4],pos2[i-4])
    total += 1
    wn.update

# Add the different images of yellow moles, red moles and green moles

turtle.addshape('yellow_mole.gif')
turtle.addshape('red_mole.gif')
turtle.addshape('green_mole.gif')

# All the variables needed as arguments for the different functions

i = 1
total = 0
count = 0
x1, y1 = 0, 0
t_remaining = 30
t = 0
old_count = 0
c = 0
mole_created = [None]*10**2
shape = [None]*10**2
pos2 = [None]*10**2
pos1 = [None]*10**2
count_text = [None]*10**4
timer_list = [None]*10**4
coordinates = [(-300,-250),(-100,-250),(100,-250),
               (300,-250),(-300,-150),(-100,-150),
               (100,-150),(300,-150),(-300,-50),
               (-100,-50),(100,-50),(300,-50)]

fixed_coordinates = [(-300,-250),(-100,-250),(100,-250),
               (300,-250),(-300,-150),(-100,-150),
               (100,-150),(300,-150),(-300,-50),
               (-100,-50),(100,-50),(300,-50)]

# Zones where the clicks are detected
# zone = left, bottom, right, top

zones = [(-350, -300, -250, -200),
        (-150, -300, -50, -200),
        (50, -300, 150, -200),
        (250, -300, 350, -200),
        (-350, -200, -250, -100),
        (-150, -200, -50, -100),
        (50, -200, 150, -100),
        (250, -200, 350, -100),
        (-350, -100, -250, 0),
        (-150, -100, -50, 0),
        (50, -100, 150, 0),
        (250, -100, 350, 0)]

# Set the background according to the choice of the player 

wn.bgpic("which.gif")
time.sleep(5)
BGv = False

# Start the game when the player choses the background

while BGv == False:
    wn.update()
    wn.onclick(BG_def)

# Start the game procedure

if BGv == True :
    print_text('Welcome to the Whack a Mole Game !', 4)
# launch the timer
    timer()
# launch the appearance of the yellow moles
    phase_1()
# launch the appearance of the red moles
    phase_2()
# launch the appearance of the green moles after one second
    wn.ontimer(phase_3,1000)

# Update the screen so it can update the score, detect the clicks, show the moles and the timer

while True :
    wn.update()
    wn.onclick(detect_click)
# change the point counter only if the user clicked on the mole
    if old_count != count :
        old_count = count
        counter()
# When the time is up stop the game and display "well played!"
    if t_remaining < 0 :
        i = 105
        hello = turtle.Turtle()
        hello.hideturtle()
        hello.penup()
        hello.goto(0, 0)
        hello.write('Well Played !', align="center", font=("Arial", 50 ,"bold"))
        turtle.update()
