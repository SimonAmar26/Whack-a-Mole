import turtle
import time

from turtle import Screen, Turtle #Provides a background to place timer on

#Font of text

FONT1 = ("Times New Roman", 50, "normal")
FONT2 = ("Times New Roman", 65, "bold")

#Module for the countdown timer
def countdown_timer(given_time):
    screen.onclick(None) #Prevents click until countdown ends
    turtle.clear()
    if given_time > 0: #Seconds is greater than 0, reduction in seconds occur
        turtle.write(given_time, align="center", font=FONT1)
        screen.ontimer(lambda: countdown_timer(given_time - 1), 1000)
    else: #Seconds is equal to zero, Time's Up text appears
        turtle.write("Time's Up!", align="center", font=FONT2)
        screen.onclick(lambda x, y: countdown_timer(90))

turtle = Turtle()
turtle.hideturtle()
turtle.write("Time Starts!", align="center", font=FONT2)

screen = Screen()
screen.onclick(lambda x, y: countdown_timer(90))
screen.mainloop()


