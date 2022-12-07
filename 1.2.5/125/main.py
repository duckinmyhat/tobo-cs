import turtle as t 

sprite = "/Users/tobias/Documents/GitHub/tobo-cs/1.2.5/125/notmario.gif" #file name of sprite
wn = t.Screen()
wn.addshape(sprite)
wn.bgpic("/Users/tobias/Documents/GitHub/tobo-cs/1.2.5/125/back.gif") #set background to game
t.shape(sprite)
t.penup()
t.goto(-490,-190)
import tkinter as tk

def key_handler(event=None):
    if event and event.keysym in ('s', 'p'):
        print('ok')

r = tk.Tk()
t = tk.Text()
t.pack()
r.bind('<Key>', key_handler)
r.mainloop()
wn.mainloop()