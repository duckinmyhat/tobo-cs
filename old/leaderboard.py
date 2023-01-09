# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# return names in the leaderboard file
def get_names(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  names = []
  for line in leaderboard_file:
    leader_name = ""
    index = 0

    # read the leader name from the line (format is "leader_name,leader_score")
    while (line[index] != ","):
      leader_name = leader_name + line[index] 
      index = index + 1
        
    # add the player name to the names list
    names.append(leader_name)

  leaderboard_file.close()

  return names  # return the names list

  
# return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this

  scores = []
  for line in leaderboard_file:
    leader_score = ""    
    index = 0

    # index beyond the comma, skipping the player's name
    while (line[index] != ","):
      index = index + 1

    # get the score
    while (index < len(line)):
      leader_score = leader_score + line[index] 
      index = index + 1

    # add the player score to the scores list
    scores.append(int(leader_score))
   
  leaderboard_file.close()

  return scores  # return the scores


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):

  index = 0
  # loop through all the scores in the existing leaderboard list
  for score in leader_scores:
    # check if this is the position to insert new score at
    if (player_score > score):
      break
    else:
      index = index + 1
  
  # insert new player and score
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)

  # keep both lists at 5 elements only (top 5 players)
  leader_names = leader_names[:5]
  leader_scores = leader_scores[:5]
  
  # store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
 
  # loop through all the leaderboard elements and write them to the the file
  for index in range(len(leader_names)):
     leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")

  leaderboard_file.close()
  

# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  for index in range(len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.down()
  
  # show player's score and rank
  if high_scorer:
    turtle_object.write("Congratulations! Your score of " + str(player_score) + " has made it to the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Your score of " + str(player_score) + " did not make it to the leaderboard this time.", font=font_setup)
  
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.down()
  
  # assign a medal based on the score
  if player_score >= gold_score:
    turtle_object.write("Medal: Gold", font=font_setup)
  elif player_score >= silver_score:
    turtle_object.write("Medal: Silver", font=font_setup)
  elif player_score >= bronze_score:
    turtle_object.write("Medal: Bronze", font=font_setup)
  else:
    turtle_object.write("Medal: No medal awarded", font=font_setup)
