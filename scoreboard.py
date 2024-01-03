import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        turtle.clear()
        turtle.hideturtle()
        turtle.color("white")
        turtle.penup()
        turtle.goto(0, 260)
        self.print_score()

    def update_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        turtle.clear()
        turtle.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)
    def game_over(self):
        turtle.goto(0,0)
        turtle.clear()
        turtle.write(f"Game Over Score \n Score : {self.score} ", align=ALIGNMENT, font=FONT)


