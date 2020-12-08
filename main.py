from turtle import Turtle, Screen
from scoreboard import ScoreBoard
#removes animations, but to see anything force update using a while loop
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.tracer(0)

game = True
tim = Turtle()

#making the screen where the game will be played
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")

ball = Ball()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.goup, "d")
screen.onkey(l_paddle.godown, "a") #when you refer to a function is a class do not put parantheses
screen.onkey(r_paddle.goup, "Right")
screen.onkey(r_paddle.godown, "Left")
score = ScoreBoard()
score.update()
while game == True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collision with r_paddle, using the distance function built into python
    if ball.distance(r_paddle) < 70 and ball.xcor() >320:
        ball.bouncepaddle()

    if ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.bouncepaddle()
    #Detect if the ball is out of bounds to award points
    if ball.xcor() > 400 :
        ball.reset_position()
        score.score1 += 1
        score.update()
    elif ball.xcor() < -400:
        ball.reset_position()
        score.score2 +=1
        score.update()

screen.exitonclick()
