from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
if r_paddle.ycor() < 380:
    screen.onkeypress(r_paddle.go_up, 'Up')
if r_paddle.ycor() > -380:
    screen.onkeypress(r_paddle.go_down, 'Down')
if l_paddle.ycor() < 380:
    screen.onkeypress(l_paddle.go_up, 'w')
if l_paddle.ycor() > -380:
    screen.onkeypress(l_paddle.go_down, 's')

game_in_play = True
while game_in_play:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect right side miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    #Detect a miss on the left
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()