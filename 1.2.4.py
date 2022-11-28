import turtle as t 

x = 0
t.left(90)
for p in range (17):
    #t.forward(x)
    

    x += 5
    if (x > 5):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(x-10)
    else:
        t.forward(10+x)
    t.left(90)

wn = t.Screen()
wn.mainloop()
    