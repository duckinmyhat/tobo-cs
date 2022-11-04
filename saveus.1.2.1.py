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

# Add this function to your game code

# manages the leaderboard for top 5 scorers
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

wn = trt.Screen()
wn.setup(height = game_height + 20, width = game_width + 20)

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
  counter.clear()
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
    
def update_score():
  global score # includes the global score
  score += 1 # increments the score by 1

  score_writer.clear()
  score_writer.pendown()
  score_writer.write(score, font=font_setup)
  # print(score) # prints the score

def whack_me_clicked(xpos, ypos):
  # Turtle mouse click event handler
  update_score()
  change_position()
  
  # print("You clicked the turtle, you turtle clicker!")
  

def change_position():
  # generate new x, y coordinates for the turtle_color
  new_x_pos = rnd.randint(-game_width/2, game_width/2)
  new_y_pos = rnd.randint(-game_height/2, game_height/2)

  # move the turtle to the new coords
  whack_me.goto(new_x_pos, new_y_pos)

def draw_board():
  boxer.goto(game_width/2, game_height/2)
  boxer.pendown()
  boxer.setheading(180)
  
  for i in range(2):  
    boxer.forward(game_width)
    boxer.left(90)
    boxer.forward(game_height)
    boxer.left(90)

  boxer.penup()
#-----events----------------
draw_board()
whack_me.onclick(whack_me_clicked)
wn.ontimer(countdown, counter_interval) 

wn.mainloop()
