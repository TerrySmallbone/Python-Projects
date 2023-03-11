# from colorgram import extract
#
# # Extract 10 colors from an image.
# colors = extract('20_001.jpg', 10)
#
# # Convert into list of rgb tuples #
# rgb_colours = []
# for colour in colors:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour
from turtle import Turtle, Screen
import random

terry = Turtle()
screen = Screen()
colour_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83),
 (109, 67, 85)]

screen.colormode(255)
terry.penup()
terry.pensize(10)
terry.speed(10)
terry.hideturtle()
colour_num = 0

def one_row():
    for dots in range(10):
        global colour_list
        global colour_num
        terry.pencolor(colour_list[colour_num])
        ### --- Use following for the 8 colours repeating ---###
        # terry.dot(20, colour_list[colour_num])
        # colour_num += 1
        # if colour_num > 7:
        #     colour_num = 0
        ###--- Or use following for random colors ---###
        terry.dot(20, random.choice(colour_list))
        terry.forward(40)

def up_row():
    terry.left(90)
    terry.forward(40)
    terry.left(90)
    terry.forward(400)
    terry.right(180)

terry.bk(200)
terry.right(90)
terry.forward(200)
terry.left(90)
for _ in range(10):
    one_row()
    up_row()




screen.exitonclick()
