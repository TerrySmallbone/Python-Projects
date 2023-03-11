from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ("arial", 80, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=180)
        self.write(arg=self.l_score, align=TEXT_ALIGNMENT, font=(FONT))
        self.goto(x=100, y=180)
        self.write(arg=self.r_score, align=TEXT_ALIGNMENT, font=(FONT))

    def l_point(self):
        self.l_score += 1
        self.refresh_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.refresh_scoreboard()