import turtle as t 
import random as rnd

path= 5 
l = path * 2




t.left(90)
for p in range (17):

    if (l > 15):
        door = rnd.randint(path, l)
        first = l - door
        t.forward(first)
        t.penup()
        t.forward(5)
        t.pendown()
        second = l - first - 5
        if (second > 10):
            wall = rnd.randint(0, second-5)
            t.forward(wall)
            t.left(90)
            t.forward(path*2)
            t.back(path*2)
            t.right(90)
            t.forward(second - wall)
        else:
            t.forward(second)   
    else: 
        t.forward(l)

    t.left(90)
    l += path



wn = t.Screen()
wn.mainloop()
    