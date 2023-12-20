from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()

# screen.update()
# game_is_on = True
#
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for t in range( len(turtle_list)-1, 0, -1 ):
#         new_x = turtle_list[t-1].xcor()
#         new_y = turtle_list[t-1].ycor()
#         turtle_list[t].goto(new_x,new_y)
#     turtle_list[0].forward(20)
#


screen.exitonclick()
