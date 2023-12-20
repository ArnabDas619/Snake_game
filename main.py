from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
turtle_list = []
for i in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(x=i * -20, y=0)
    turtle_list.append(new_turtle)

screen.exitonclick()
