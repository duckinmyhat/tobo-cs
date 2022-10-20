# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trt
import random as rnd 

#-----game configuration----
turtke_color = 'yellow'
turtle_shape = 'turtle'
turtle_size = 5
score = 0

wn = trt.Screen()
wn.setup(height = 1.0, width = 1.0)
#-----initialize turtle-----
wack_me = trt.Turtle()
wack_me.turtlesize(turtle_size)
wack_me.shape(turtle_shape)
wack_me.color(turtke_color)
wack_me.penup()


#-----game functions--------
def update_score():
    global score #golabal svore 
    score += 1 #incrase score by 1
    print(score)

def wack_me_clicked(xpos, yPos):
    #tutke mouse click event handler 
    #print("you clicked the turtle, you turtle cliker!")
    change_position()
    update_score()



def change_position():
    #new xy cordenets
    new_x_pos = rnd.randint(-200,200)
    new_Y_pos = rnd.randint(-150,150)

    #move turt
    wack_me.goto(new_x_pos, new_Y_pos)
#-----events----------------
wack_me.onclick(wack_me_clicked)

wn.mainloop()