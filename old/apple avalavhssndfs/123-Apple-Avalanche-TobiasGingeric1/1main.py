#   a123_apple_1.py
import turtle as trtl
import time as tm
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")#set bakgorung gif

apple = trtl.Turtle()

drawer=trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()


def apple_fall(active_apple):
  active_apple.penup()
  screen_dim = wn.screensize()
  ground_cor = screen_dim[1]//2
  #fall_distance = ground_cor - active_apple.ycor()
  
  active_apple.goto(active_apple.xcor() ,-ground_cor)
  drawer.clear()
# This function takes care of font and color.
def draw_an_A():
  drawer.hideturtle()
  drawer.color("white")
  drawer.penup()
  drawer.goto(apple.xcor()-16, apple.ycor()-36)
  drawer.pendown()
  drawer.write("A", font=("Arial", 35, "bold")) 
  drawer.hideturtle()

#-----event handlers-----
def key_press_handler():
  apple_fall(apple)
  
#-----function calls-----
draw_apple(apple)
draw_an_A()

wn.onkeypress(key_press_handler, "a")

wn.listen()
wn.mainloop()