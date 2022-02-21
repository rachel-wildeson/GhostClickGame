#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:22:34 2021

@author: rachelwildeson
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 16, 2021

@author: Rachel Wildeson

DEAR USER, 
    The object of the game is to click the ghost that drifts into view in the screen.
    If you are able to *click* the ghost in time before it disappears behind the red square, You Win!
    To play the game, click the green arrow in the top menu box of the screen. A popup window will appear with the game. 

"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
#turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True
x = 300

ghostSmallOne = turtle.Turtle(shape="circle")
ghostImgSmallOne = "ghostsmallone.gif" 
panel.addshape(ghostImgSmallOne) 
ghostSmallOne.shape(ghostImgSmallOne) 

ghosts = [ghostSmallOne]
# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!

def ghostPath(turt, leftAngle=10, distance =500, rightAngle=195):
    ''' Sends ghost diagnally along screen and the path goes back and forth '''    
    for i in range (2):
      turt.left(leftAngle)
      turt.forward(distance)
      turt.right(rightAngle)
      turt.forward(distance)
      for i in range (1):
          turt.left(-leftAngle)
          turt.forward(-distance)
          turt.right(-rightAngle)
          turt.forward(-distance)

def youWin (x,y):
    '''Prints You Win in the Command Line '''   
    print("You Win!")
        
# ================ ANIMATION LOOP =========================
   
square = turtle.Turtle(shape='square')
square.hideturtle()
square.goto(300,0)
square.showturtle()
square.down()
square.color('red')
square.shapesize(30)

ghosts[0].hideturtle()
ghosts[0].up()
ghosts[0].goto(-275,-50)
ghosts[0].showturtle()

ghosts[0].onclick(youWin)
while running:
  ghostPath(ghosts[0])
  

    # call functions and conditional statement to stop loop (if desired) 
      
    #panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup
