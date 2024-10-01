# Imports the moudles
import turtle
from turtle import Turtle, Screen

draw_turtle = Turtle(shape="turtle")
screen = Screen()

# The functions to move the turtle
def move_forwards():
    draw_turtle.forward(10)
def move_backwards():
    draw_turtle.backward(10)
def move_left():
    draw_turtle.left(10)
def move_right():
    draw_turtle.right(10)
def clear():
    """Clears the screen and move the turtle to the strart position"""
    draw_turtle.penup()
    draw_turtle.home()
    draw_turtle.clear()
    draw_turtle.pendown()

screen.listen()
# Moves 'draw_turtle' with the function with using the 'key'
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
