import turtle as t 
import arcade

sprite = "/Users/tobias/Documents/GitHub/tobo-cs/1.2.5/125/notmario.gif" #file name of sprite
wn = t.Screen()
wn.addshape(sprite)
wn.bgpic("/Users/tobias/Documents/GitHub/tobo-cs/1.2.5/125/back.gif") #set background to game
t.shape(sprite)
t.penup()
t.goto(-490,-190)

class MainGame(arcade.Window):
  # Creating function to check button is pressed
      # or not
      def on_key_press(self, symbol,modifier):
    
          # Checking the button pressed
          # is up arrow key or not
          if symbol == arcade.key.UP:
              print("Upper arrow key is pressed")


# Calling MainGame class       
MainGame()
arcade.run()

wn.mainloop()
wn.mainloop()