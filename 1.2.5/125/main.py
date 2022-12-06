import turtle as t 

sprite = "notmario.gif" #file name of sprite
wn = t.Screen()
wn.addshape(sprite)
wn.bgpic("back.gif") #set background to game
t.shape(sprite)
t.penup()
t.goto(-490,-190)
