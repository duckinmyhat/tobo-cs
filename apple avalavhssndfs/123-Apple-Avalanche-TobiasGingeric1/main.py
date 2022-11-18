#   a123_apple_1.py
import turtle as trtl
import time as tm
import random as rnd

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
letter_horizontal_offset = 16
letter_vertical_offset = 34

letter_list=[]
apple_list=[]
apple_letter=[]
drawer_list=[]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif") #set background to trees and sky

apple = trtl.Turtle()
apple.penup()
apple.goto(-150,125)

drawer=trtl.Turtle()
drawer.hideturtle()

#-----functions-----

def create_apples():
  global apple_list, apple_letter, drawer_list

  for i in range(rnd.randint(1,5)):
    # create the apple and initialize
    temp_turtle = trtl.Turtle()  
    temp_turtle.penup()
    temp_turtle.hideturtle()
    temp_turtle.shape(apple_image)
  
    # determine location of apple
    x = rnd.randint(-150, 150)
    y = rnd.randint(0,125)
    # place and show apple
    temp_turtle.goto(x,y)
    temp_turtle.showturtle()

    # add this turtle to the list of apple_list
    apple_list.append(temp_turtle)

    # create a turtle to draw the letter for this apple
    temp_drawer = trtl.Turtle()
    temp_drawer.hideturtle()
    temp_drawer.penup()
    temp_drawer.color("white")
    temp_drawer.goto(temp_turtle.xcor() - letter_horizontal_offset, temp_turtle.ycor() - letter_vertical_offset)
    temp_drawer.pendown()
    letter = letter_list.pop(rnd.randint(0, len(letter_list)-1))
    temp_drawer.write(letter, font=("Arial", 36, "bold"))

    #add  this drawer to the list
    drawer_list.append(temp_drawer)
  

    
    
    
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  #gove a leter and make said apple fall
def apple_fall(active_apple):
  #find index in letter list 
  for letter in letter_list:
    if letter == active_apple
    
  
# This function takes care of font and color.
def draw_an_A():
  drawer.color("white")
  drawer.penup()
  drawer.goto(apple.xcor() - letter_horizontal_offset, apple.ycor() - letter_vertical_offset)
  drawer.pendown()
  drawer.write("A", font=("Arial", 36, "bold")) 

def draw_a_letter():
  drawer.color("white")
  drawer.penup()
  drawer.goto(apple.xcor() - letter_horizontal_offset, apple.ycor() - letter_vertical_offset)
  drawer.pendown()
  letter = letter_list.pop(rnd.randint(0, len(letter_list)-1))
  drawer.write(letter, font=("Arial", 36, "bold"))

  print(letter_list)
  
  return letter
  
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters
  
#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
#for i in range(0, number_of_apples):
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.



#-----event handlers-----
def handle_a():
  if apple_letter == "a":
    apple_fall(apple)

def handle_b():
  if apple_letter == "b":
    apple_fall(apple)

def handle_c():
  if apple_letter == "c":
    apple_fall(apple)

def handle_d():
  if apple_letter == "d":
    apple_fall(apple)

def handle_e():
  if apple_letter == "e":
    apple_fall(apple)
    
  
#-----function calls-----
for i in range(97, 102):
  letter_list.append(chr(i))

#print(letter_list)

#draw_apple(apple)
create_apples()
#apple_letter = draw_a_letter()


wn.onkeypress(handle_a, "a")
wn.onkeypress(handle_b, "b")
wn.onkeypress(handle_c, "c")
wn.onkeypress(handle_d, "d")
wn.onkeypress(handle_e, "e")

wn.listen()
wn.mainloop()
