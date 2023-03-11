from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Betting time", prompt="Which coloured Turtle do you think will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtles = []

if user_bet:
    race_on = True

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230.00, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The winning colour was {winning_colour}")
            else:
                print(f"You've lost! The winning colour was {winning_colour}")

        turtle.forward(random.randint(0, 10))



screen.exitonclick()


