from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  # setting screen dimensions
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]  # list of colours of our turtle
all_turtles = []
y_coordinate = 145  # y coordinate of the first turtle

for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")  # creating 6 turtles per each colour
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate)
    new_turtle.speed("fastest")
    y_coordinate -= 45  # changing y coordinate ready for next turtle
    all_turtles.append(new_turtle)  # adding turtle to the list of all turtles

if user_bet in colours:  # once user enters a bet, the race starts
    is_race_on = True
else:
    print("This turtle is not racing today.")

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:  # the game ends once a turtle reaches x coordinate 200
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won. The {winning_colour} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_colour} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)  # each turtle moves forward by random distance 0 - 10

screen.exitonclick()
