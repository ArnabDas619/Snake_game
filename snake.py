from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for snake_seg in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=snake_seg * 20, y=0)
            self.segments.append(new_segment)

    def move(self):
        for snake_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_seg - 1].xcor()
            new_y = self.segments[snake_seg - 1].ycor()
            self.segments[snake_seg].goto(new_x, new_y)
        self.segments[0].forward(20)
