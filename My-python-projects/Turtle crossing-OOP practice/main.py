import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(fun=player.move, key="Up")
cars = CarManager()


car_increment = 0
game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()

    car_increment += 1
    if car_increment == 6:
        car_increment = 0
        cars.new_car()
    cars.move()

    for vehicle in range(len(cars.all_cars)):
        car = cars.all_cars[vehicle -1]
        if player.distance(car) < 20:
            scoreboard.game_over()
            time.sleep(5)
            game_is_on = False

    if player.ycor() == 270:
        player.reset_position()
        cars.level_up()
        scoreboard.add_point()
        cars.new_car()



# todo 1 Create a turtle player that starts at the bottom of the screen and
#  listen for the "Up" keypress to move the turtle north.
#  If you get stuck, check the video walkthrough in Step 3.

# todo 2 Create cars that are 20px high by 40px wide that are randomly generated
#  along the y-axis and move to the left edge of the screen.
#  No cars should be generated in the top and bottom 50px of the screen
#  (think of it as a safe zone for our little turtle).
#  Hint: generate a new car only every 6th time the game loop runs.
#  If you get stuck, check the video walkthrough in Step 4.

# todo 3 Detect when the turtle player collides with a car and stop the game if this happens.
#  you get stuck, check the video walkthrough in Step 5.

# todo 4 Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
#  When this happens, return the turtle to the starting position and increase the speed of the cars.
#  Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.
#  If you get stuck, check the video walkthrough in Step 6.

# todo 5 Create a scoreboard that keeps track of which level the user is on. Every time the turtle
#  player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER
#  should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.


