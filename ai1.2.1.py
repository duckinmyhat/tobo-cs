#-----import statements-----
import turtle as trt
import random as rnd
import leaderboard as lb


#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#name call

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input('what is your name\n')
wn = trt.Screen()

# Add this function to your game code

# manages the leaderboard for top 5 scorers

spot = trt.Turtle()
spot.hideturtle()


def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)



#-----game configuration----
turtle_color = 'pink'
turtle_shape = 'turtle'
turtle_size = 5
score = 0

game_height = 300
game_width = 400
score_height = 20
score_width = 50
score_x = game_width/2 - 0.5 * score_width - 20
score_y = game_height/2 - 0.5 * score_height - 25
time_x = -game_width/2 - 0.5 * score_width + 40
time_y = game_height/2 - 0.5 * score_height  - 25
#-----initialize turtles-----
whack_me = trt.Turtle()
whack_me.turtlesize(turtle_size)
whack_me.shape(turtle_shape)
whack_me.color(turtle_color)
whack_me.penup()

score_writer = trt.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(score_x, score_y)

counter =  trt.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(time_x,time_y)

boxer = trt.Turtle()
boxer.hideturtle()
boxer.penup()

#-----countdown writer-----

#-----game functions--------
def countdown():
  global timer, timer_up
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    whack_me.hideturtle()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    counter.hideturtle()
  counter.clear()
    
def update_score():
  global score # includes the global score
  score += 1 # increments the score by 1

  score_writer.clear()
  score_writer.write(score, font=font_setup)
  # print(score) # prints the score

def whack_me_clicked(xpos, ypos):
  # Turtle mouse click event handler
  update_score()
  change_position()
  
  # print("You clicked the turtle, you turtle clicker!")
  

def change_position():
  # generate new x, y coordinates for the turtle_color
  new_x_pos = rnd.randint(-game_width/2 + turtle_size, game_width/2 - turtle_size)
  new_y_pos = rnd.randint(-game_height/2 + turtle_size, game_height/2 - turtle_size)

  if (new_x_pos > -turtle_size and new_x_pos < turtle_size) and (new_y_pos > -turtle_size and new_y_pos < turtle_size):
    change_position()
  else:
    whack_me.goto(new_x_pos, new_y_pos)

#-----events----------------
whack_me.onclick(whack_me_clicked)
wn.ontimer(countdown, counter_interval) 


#-----game start------------
countdown()

wn.mainloop()
