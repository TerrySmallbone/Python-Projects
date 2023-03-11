from turtle import Turtle
TEXT_ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.goto(x=-210, y=260)
        self.write(arg=f"Level: {self.current_score}", align=TEXT_ALIGNMENT, font=FONT)

    def add_point(self):
        self.current_score += 1
        self.refresh_scoreboard()

    def game_over(self):
        # new_turtle = Turtle()
        # new_turtle.penup()
        # new_turtle.hideturtle()
        # new_turtle.color("black")
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", align=TEXT_ALIGNMENT, font=FONT)

