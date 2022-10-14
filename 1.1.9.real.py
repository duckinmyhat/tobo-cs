import turtle as t 
#sets colors and shapes 
shape = ["arrow","turtle","circle","square","triangle","classic"]
color = ["magenta","indigo","orange red","yellow","medium turquoise","lime"]
tcolor = ["sky blue","firebrick","pale green","medium turquoise","deep pink","teal"]
color2 = ["red","orange","yellow","green","blue","indigo"]
t.pensize(50)
while True:
    for loop in range(len(shape)):
        t.speed(2)
        t.pensize(50)
        #makes first long line and stamps at end 
        t.shape(shape[loop])
        t.pencolor(color[loop])
        t.fillcolor(tcolor[loop])
        t.hideturtle()
        t.penup()
        t.goto(0,0)
        t.pendown()
        #idk if i want to show turtle
        #t.showturtle()
        t.left(360/len(shape))
        t.forward(50)
        t.stamp()
        #makes second shorter line
        t.hideturtle()
        t.penup()
        t.goto(0,0)
        #t.showturtle()
        t.pendown()
        #same color as turtle for short line
        t.pencolor(tcolor[loop])
        t.forward(15)

    x = -350
    r = -350
    t.speed(10)
    for m in range(len(color2)):
        #every other one is on the other side   
        if (m % 2) == 0:
            #curve start location
            t.shape(shape[m])
            t.pencolor(color2[m])
            t.pensize(10)
            t.hideturtle()
            t.penup()
            t.goto(x,0)
            t.setheading(90)
            t.showturtle()
            t.pendown()
            t.circle(r,180)
            #other half
            t.hideturtle()
            t.penup()
            t.goto(x,0)
            t.setheading(-90)
            t.showturtle()
            t.pendown()
            t.circle(-r,180)

        
        else:
            #curve start location fpm other side
            t.shape(shape[m])
            t.pencolor(color2[m])
            t.pensize(10)
            t.hideturtle()
            t.penup()
            t.goto(-x,0)
            t.setheading(90)
            t.showturtle()
            t.pendown()
            t.circle(-r,180)
            #other half
            t.hideturtle()
            t.penup()
            t.goto(-x,0)
            t.setheading(-90)
            t.showturtle()
            t.pendown()
            t.circle(r,180)
    
    
        x = x+50
        r += 50

   
    t.hideturtle()
    t.clear()

wn = t.Screen()
wn.mainloop()