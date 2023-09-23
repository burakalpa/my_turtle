import turtle
import random
import time

wn = turtle.Screen()
wn.title("Click the Turtle Game")
wn.bgcolor("light blue")



player_turtle = turtle.Turtle()
player_turtle.shape("turtle")
player_turtle.color("green")
player_turtle.speed(1)
player_turtle.penup()
player_turtle.goto(0, 0)


score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("black")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 350)

timer_turtle = turtle.Turtle()
timer_turtle.speed(0)
timer_turtle.color("black")
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(0, 330)

score = 0
time_limit = 15
def increase_score(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))


def on_click(x, y):
    if is_collision(player_turtle, x, y):
        increase_score(x, y)

def is_collision(turtle, x, y):
    distance = turtle.distance(x, y)
    return distance < 20

start_time = time.time()
end_time = start_time + time_limit

def update_timer():
    remaining_time = max(0, end_time - time.time())
    timer_turtle.clear()
    timer_turtle.write(f"Time Left: {int(remaining_time)}s", align="center", font=("Courier", 18, "normal"))
    if remaining_time == 0:
        wn.bye()


wn.onscreenclick(on_click)


while time.time() < end_time:
    player_turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
    wn.update()
    update_timer()


score_turtle.clear()
score_turtle.goto(0, 0)
score_turtle.write(f"Final Score: {score}", align="center", font=("Courier", 24, "normal"))



score_turtle.clear()
score_turtle.goto(0, 0)
score_turtle.write(f"Final Score: {score}", align="center", font=("Courier", 24, "normal"))

time.sleep(5)

