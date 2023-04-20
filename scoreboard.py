from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0, 260)
        self.score = 0
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def game_winner(self):
        self.clear()
        self.goto(0, 0)
        self.write("NEXT ROUND", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.clear()

    def display_score(self):
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score = self.score + 1
        self.clear()
        self.display_score()
