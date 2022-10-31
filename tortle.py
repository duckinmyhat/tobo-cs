# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random


#-----game configuration----
score = 0
timer = 30
timer_interval = 1000
timer_up = False

turtle_shape = "turtle"
turtle_size = 2
size_dec = 0.03
turtle_color = "green"

font_setup = ("Arial", 20, "normal")
bg_color = "red"


#-----initialize turtles-----
tortle = t.Turtle()
tortle.shape(turtle_shape)
tortle.turtlesize(turtle_size)
tortle.color(turtle_color)
tortle.penup()

score_writer = t.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(190, 160)

countdown = t.Turtle()
countdown.penup()
countdown.hideturtle()
countdown.goto(-190, 160)


#-----game functions--------
def tortle_clicked(x, y):
    if score == 0:
        start_game()
    global turtle_size
    turtle_size -= size_dec
    tortle.turtlesize(turtle_size)
    tortle.goto(random.randint(-200, 200), random.randint(-150, 150))
    update_score()
    score_writer.clear()
    score_writer.write(score, font=font_setup)


def update_score():
    global score
    score += 1

def update_time():
    global timer, timer_up
    countdown.clear()
    if timer <= 0:
        countdown.write("Time's Up", font=font_setup)
        timer_up = True
        tortle.hideturtle()
    else:
        countdown.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        countdown.getscreen().ontimer(update_time, timer_interval)

def start_game():
    update_time()

#-----events----------------
wn = t.Screen()
wn.bgcolor(bg_color)
tortle.onclick(tortle_clicked)
wn.mainloop()
