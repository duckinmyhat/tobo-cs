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


wn.mainloop()
wn.mainloop()
