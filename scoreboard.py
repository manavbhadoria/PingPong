

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0


    def update(self):
        self.hideturtle()
        self.clear()
        self.penup()
        self.color("white")
        self.goto(0,240)
        self.write("Score\n",align="center",font=("Arial",18,"bold"))

        self.write(""+str(self.score1) + " : " +str(self.score2),align="center",font=("Arial",14,"bold"))

