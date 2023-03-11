from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

speed = 0.05
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_hit()
        speed -= .005

    # detect paddle miss
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.r_point()
        speed = .05

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.l_point()
        speed = .05

screen.exitonclick()


