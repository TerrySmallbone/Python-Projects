from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.turn_up, key="Up")
screen.onkey(fun=snake.turn_down, key="Down")
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.scored()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        snake.reset_snake()
        scoreboard.reset_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            scoreboard.reset_score()


screen.exitonclick()
