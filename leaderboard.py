#  leaderboard.py -- Leaderboard module for Activity 1.2.2
import os

#-----module variables----
leader_scores = []
leader_names  = []
data_file_name  = ""

#-----module functions----

def load_leaderboard(file_name):
  '''Load leaderboard data from file'''
  global leader_scores, leader_names, data_file_name

  # Clear any preloaded data
  leader_scores.clear()
  leader_names.clear()
  
  # Create the file if it doesn't exist
  if not os.path.isfile(file_name):
    created_file = open(file_name, "w")
    created_file.write("5\nVince B\n")
    created_file.close()
  
  # Open file, read it all, close it:
  data_file_name = file_name
  data_file = open(data_file_name, "r")
  data = data_file.read()
  data_file.close()
  # Separate the data into a list by line, then convert any numbers to ints:
  data_list = data.splitlines()
  data_list = list(map(lambda d: int(d) if d.isdigit() else d, data_list))

  print("Loaded leaderboard data as list: ", data_list)
  
  # TODO 1: add scores from the data onto the corresponding list
  index = 0
  while index < len(data_list):
    leader_scores.append( data_list[index] )
    index = index + 2
  # TODO 2: add names from the data onto the corresponding list
  index = 1
  while index < len(data_list):
    leader_names.append( data_list[index] )
    index = index + 2
  print("Leader scores:", leader_scores)
  print("Leader name:", leader_names)
 
def update_leaderboard(player_score, player_name):
  '''Update the scores and names lists with a new player score and name at the correct position, if appropriate'''
  global leader_scores, leader_names, data_file_name

  print("New score and name:", player_score, player_name)
  
  # TODO 5: computer score's placement
  placement = 0
  index = 0
  while index < len(leader_scores):
    if leader_scores[index] > player_score:
      placement = placement + 1
    index = index + 1
  print("New score placement: ", placement)
  # TODO 6: insert the player name and score
  leader_scores.insert(placement, player_score )
  leader_names.insert(placement, player_name)
  
  # TODO 9: keep both lists at 5 elements only (top 5 players)
  if len(leader_scores) > 5:
    leader_scores.pop()
  if len(leader_names) > 5:
    leader_names.pop()
  # TODO 7: open the data file for writing
  data_out = open(data_file_name, "w")
  
  
  # TODO 8: write the leader lists into the file
   # TODO 8: write the leader lists into the file
  index = 0
  while index < len(leader_scores) :
    score = leader_scores[index]
    name  = leader_names[index]
    score_str = str(score)
    data_out.write( score_str + "\n" )
    data_out.write( name + "\n" )
    index = index + 1


  
  data_out.close()



def draw_leaderboard(writer_turtle, font_setup):
  '''Use writer_turtle to write the leaderboard on the screen'''
  global leader_scores, leader_names

  # clear turtle's drawings and move near the center of the screen
  writer_turtle.hideturtle()
  writer_turtle.penup()
  writer_turtle.goto(-75, 100)
  writer_turtle.write("High Scores:", font=font_setup)
  
  line_spacing = font_setup[1] * 1.2
  next_x = -50
  next_y = 100
  
  # iterate through the scores and write them
  index = 0
  while index < len(leader_scores):
    # move turtle down a line
    next_y = next_y - line_spacing
    writer_turtle.goto(next_x, next_y)
    # access score from list then write it on screen
    score = leader_scores[index]
    writer_turtle.write( str(score) , font=font_setup )
    # increment index
    index = index + 1
  
  next_x = 50
  next_y = 100
  
  # TODO 3: iterate through the names and write them
  index = 0
  while index < len(leader_names):
    # move turtle down a line
    next_y = next_y - line_spacing
    writer_turtle.goto(next_x, next_y)
    # access name from list then write it on screen
    name = leader_names[index]
    writer_turtle.write( str(name) , font=font_setup )
    # increment index
    index = index + 1
