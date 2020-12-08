from turtle import Turtle


class Paddle(Turtle):  # you can inherit only one class
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)
    def goup(self):
        y = self.ycor() + 20
        self.goto(self.xcor(),y)

    def godown(self):
        y = self.ycor() - 20
        self.goto(self.xcor(),y)
