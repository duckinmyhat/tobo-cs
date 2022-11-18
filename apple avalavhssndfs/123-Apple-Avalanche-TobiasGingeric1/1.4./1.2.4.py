import turtle as t 
x = 100
t.right(90)
for p in range (17):
    t.forward(x)
    t.right(90)
    x -= 5


wn = t.Screen()
wn.mainloop()
    