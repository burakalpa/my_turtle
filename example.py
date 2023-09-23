import turtle
import random
import time


wn = turtle.Screen()
wn.title("Click the Turtle Game")
wn.bgcolor("white")
wn.setup(width=800, height=600)

player_turtle = turtle.Turtle()
player_turtle.shape("turtle")
player_turtle.color("green")
player_turtle.speed(10)
player_turtle.penup()
player_turtle.goto(0, 0)

score_turtle = turtle.Turtle()
score_turtle.speed(10)
score_turtle.color("black")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)

