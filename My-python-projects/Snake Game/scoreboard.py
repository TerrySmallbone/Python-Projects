from turtle import Turtle
import os

TEXT_ALIGNMENT = "center"
FONT = ("arial", 12, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open('../../OneDrive/Desktop/data.txt', mode="r") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.color("white")
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score: {self.high_score}",
                   move=False, align=TEXT_ALIGNMENT, font=(FONT))

    def scored(self):
        self.score += 1
        self.refresh_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('/Users/terry/OneDrive/Desktop/data.txt', mode="w") as file_high_score: # mode="a" means append
                file_high_score.write(str(self.high_score))
        self.score = 0
        self.refresh_scoreboard()


