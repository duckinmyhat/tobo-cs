# Import turtle module
import turtle as t 

# Set sprite and background image
sprite = "/Users/tobias/Documents/GitHub/tobo-cs/1.2.5/125/notmario.gif" #file name of sprite
wn = t.Screen()
wn.addshape(sprite)
wn.bgpic("/Users/tobias/Documents/GitHub/tobo-cs/1.2.5/125/back.gif") #set background to game

# Set turtle shape to sprite
t.shape(sprite)
t.penup()

# Set starting position for sprite
t.goto(-490,-190)

# Create spike turtle
spike = t.Turtle()
spike.shape("square")
spike.color("red")

# Move spike to desired position
spike.goto(-100, -200)

# Create pit turtle
pit = t.Turtle()
pit.shape("circle")
pit.color("blue")

# Move pit to desired position
pit.goto(100, -200)

# Define movement functions
def move_forward():
  # Move sprite forward 10 pixels
  t.forward(10)


def move_backward():
  # Move sprite backward 10 pixels
  t.backward(10)



def jump():
  # Move sprite upward 25 pixels
  print(t.pos())
  t.goto((t.pos()) + (0,25))
  # Move sprite forward 30 pixels
  t.forward(30)
  # Return sprite to original position
  t.goto((t.pos()) - (0,25))



# Bind the movement functions to the WASD keys
wn.onkeypress(move_forward, "d")
wn.onkeypress(move_backward, "a")
wn.onkeypress(jump, "w")

# Start listening for key events
wn.listen()


# Define function to perform collision detection
def collision_detection():
  # Check if sprite is colliding with a spike
  if t.distance(spike) < 20:
    # Move sprite to position just beyond the spike
    t.goto(spike.x + 30, t.y)

  # Check if sprite is colliding with a pit
  if t.distance(pit) < 20:
    # Move sprite to position just beyond the pit
    t.goto(pit.x - 30, t.y)

# Run collision detection every 100 milliseconds
wn.ontimer(collision_detection, 100)

wn.mainloop()

