# Imports: Random and Turtle
import turtle
from turtle import Turtle, Screen
from turtledemo.paint import changecolor
import random

# for the While Loop
race_on = False
# Var for the exitonclick
screen = Screen()

# Custom screen size
screen.setup(width=500, height=400)
# Input for the guess of the turtle
user_bet= screen.textinput(title="Make a bet", prompt="Whic turtle will win? Enter a color: ").lower()

# Lists: Colors, Y-Positions and the turtles that will be created
colors = ["red", "pink", "yellow", "green", "blue", "black"]
y_position = [-70, -40, -10, 20, 50, 80]
all_tutrles = []

# For Loop to create 6 turtles: Gives Shape, Color, Ups the pen, Position Turtule on the start line and append the turtles to the all_turtle list
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_tutrles.append(new_turtle)

# Activate the loop
if user_bet:
    race_on = True

while race_on:

    for turtle in all_tutrles:
        # When a turtle get to finish line
        if turtle.xcor() > 230:
            race_on = False
            winner_turtle = turtle.pencolor()
            # Promotes for Winning/Losing
            if winner_turtle == user_bet:
                print(f"You Won!, {winner_turtle} won!")
            else:
                print(f"You Lost!, {winner_turtle} won!")
        # Move the turtle forward from 0 to 10 steps by the random moudle
        rand_forward = random.randint(0,10)
        turtle.forward(rand_forward)

screen.exitonclick()