"""
file: myname.py
language:python 3
author: pan7447@cs,rit,edu Parvathi Nair
description: To render my name 'PARVATHI'
precondition: Turtle is at coordinates(0,0) facing east
postcondition: Turtle is at coordinates(-360,0) facing east
"""

import turtle
import math

SPACE = 60      #global variable used to orient the starting point after each alphabet

def InitialAndFinalPosition():
    """
    set the initital position
    """
    turtle.penup()
    turtle.setpos(-360, 0)

def spacing():
    """
    used to provide space betweeen 2 adjacent aphabets
    """
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(SPACE)
    turtle.pendown()

def drawP():
    """
    draws the alphabet P
    """
    spacing()
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.circle(20,180)
    turtle.setheading(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(80)
    turtle.setheading(0)

def drawA():
    """
    draws the alphabet A
    """
    spacing()
    turtle.left(76)
    turtle.forward(math.hypot(20,80))   #uses the hypot fucntion to find the hypotenuse
    turtle.setheading(284)
    turtle.forward(math.hypot(20, 80))  #uses the hypot fucntion to find the hypotenuse
    turtle.left(180)
    turtle.forward(math.hypot(20,80)/2) #uses the hypot fucntion to find the hypotenuse
    turtle.setheading(180)
    turtle.forward(20)
    turtle.penup();
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(40)

def drawR():
    """
    draws the alphabet R
    """
    spacing()
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.circle(20, 180)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(63.4)
    turtle.forward(math.hypot(40, 20))  #uses the hypot fucntion to find the hypotenuse
    turtle.setheading(180)
    turtle.penup()
    turtle.forward(40)

def drawV():
    """
    draws the alphabet V
    """
    spacing()
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(76)
    turtle.forward(math.hypot(80, 20)) #uses the hypot fucntion to find the hypotenuse
    turtle.left(180)
    turtle.forward(math.hypot(80, 20)) #uses the hypot fucntion to find the hypotenuse
    turtle.setheading(104)
    turtle.forward(math.hypot(80, 20)) #uses the hypot fucntion to find the hypotenuse
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(80)
    turtle.setheading(0)

def drawT():
    """
    draws the alphabet T
    """
    spacing()
    turtle.penup()
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(40)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(80)

def drawH():
    """
    draws the alphabetH
    """
    spacing()
    turtle.setheading(90)
    turtle.forward(80)
    turtle.setheading(270)
    turtle.forward(40)
    turtle.setheading(0)
    turtle.forward(40)
    turtle.setheading(90)
    turtle.forward(40)
    turtle.setheading(270)
    turtle.forward(80)
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(40)

def drawI():
    """
    draws the alphabet I
    """
    spacing()
    turtle.forward(40)
    turtle.setheading(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(40)
    turtle.setheading(270)
    turtle.penup()
    turtle.forward(80)

def main():
    """this is the main method
    """
    InitialAndFinalPosition()
    drawP()
    drawA()
    drawR()
    drawV()
    drawA()
    drawT()
    drawH()
    drawI()
    InitialAndFinalPosition()
    turtle.hideturtle()                 #hides the turtle after drawing
    turtle.mainloop()                   #waits for the user to exit the window

if __name__ == '__main__':
    main()


