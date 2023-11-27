from turtle import *

T = Turtle()
T.screen.title("Whack a Mole")
T.screen.bgpic("/Users/simonamar-roisenberg/Desktop/Computional Thinking/BG.gif")
T.screensize(canvwidth=500, canvheight=300,
                  bg="black")
T.color('red')
T.fillcolor('yellow')
while True:
    T.begin_fill()
    T.forward(200)
    T.left(170)
    if abs(T.pos()) < 1:
        break

T.screen.mainloop()
