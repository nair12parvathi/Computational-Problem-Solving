"""
file: antenna.py
language:python 3
author: pan7447@cs,rit,edu Parvathi Nair
author: dck1135@cs.rit.edu Darshan Kavathe
description: To generate fractals in 3 different ways
precondition: Turtle is at coordinates(0,0),facing east, pendown
postcondition: Turtle is at coordinates(0,0),facing east, penup
"""
import turtle
import math

WINDOW_WIDTH=500 # global variable to set the dimensions of the window
WINDOW_HEIGHT=500 # global variable to set the dimensions of the window


def init():
    """
    Initialize the window to (1000, 1000) .

    precondition: Turtle is at coordinates(0,0),facing east, pendown
    postcondition: Turtle is at coordinates(0,0),facing east, penup
    :return: None
    """
    turtle.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, startx=None, starty=None)  # sets window size

    turtle.up()
    turtle.speed(6)
    turtle.title('antenna')



def square(side):
    """
    Draws the base square function .
    precondition: Turtle is at relative 0,facing east, pendown
    postcondition: Turtle is at relative 0,facing east, penup
    :return: None
    """

    turtle.penup()
    turtle.left(180)
    turtle.forward(math.sqrt(2)*side/2)
    turtle.right(135)
    turtle.pendown()
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.penup()
    turtle.right(45)
    turtle.forward(math.sqrt(2)*side/2)


def base(side):
    """
    Draws the base fractal which includes 5 squares .
    precondition: Turtle is at relative 0,facing east, pendown
    postcondition: Turtle is at relative 0,facing east, penup
    :return: None
    """

    square(side)
    turtle.left(180)
    turtle.forward(math.sqrt(2)*side)
    turtle.right(180)
    square(side)
    turtle.forward(math.sqrt(2) * side*2)
    square(side)
    turtle.backward(math.sqrt(2) * side)
    turtle.left(90)
    turtle.forward(math.sqrt(2) * side)
    turtle.right(90)
    square(side)
    turtle.right(90)
    turtle.forward(math.sqrt(2) * side*2)
    turtle.left(90)
    square(side)
    turtle.left(90)
    turtle.forward(math.sqrt(2) * side)
    turtle.right(90)


def antenna(level,side):
    """
    Recursive function which draws antenna using sequence of squares .
    precondition: Turtle is at relative 0,facing east, pendown
    postcondition: Turtle is at relative 0,facing east, penup
    :return: None
    """

    if level==1:
        base(side)
    elif level>0:
        turtle.penup()
        turtle.forward(math.pow(3, level-1) * math.sqrt(2) * side)
        antenna(level-1,side)
        turtle.backward(math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.backward(math.pow(3, level-1) * math.sqrt(2) * side)
        antenna(level - 1, side)
        turtle.forward(math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.left(90)
        turtle.forward(math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.right(90)
        antenna(level - 1, side)
        turtle.right(90)
        turtle.forward(math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.forward(math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.left(90)
        antenna(level - 1, side)
        turtle.left(90)
        turtle.forward(math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.right(90)
        antenna(level - 1, side)

def edge(size,level):
    """
    Recursive function which draws antenna using perimeter without gaps .
    precondition: Turtle is at relative 0,facing east, pendown
    postcondition: Turtle is at relative 0,facing east, penup
     :return: None
                  """
    if level == 0:
        turtle.pendown()
        turtle.forward(size)
        return

    edge(size,level-1)
    turtle.left(90)
    edge(size-size/10,level-1)
    turtle.right(90)
    edge(size, level - 1)
    turtle.right(90)
    edge(size-size/10, level - 1)
    turtle.left(90)
    edge(size, level - 1)


def single(size,level):
    """
    Recursive function which draws antenna using perimeter with gaps .
    precondition: Turtle is at relative 0,facing east, pendown
    postcondition: Turtle is at relative 0,facing east, penup
    :return: None
    """

    if level == 0:
        turtle.pendown()
        turtle.forward(size)
        return

    edge(size,level-1)
    turtle.left(90)
    edge(size,level-1)
    turtle.right(90)
    edge(size, level - 1)
    turtle.right(90)
    edge(size, level - 1)
    turtle.left(90)
    edge(size, level - 1)



def main():
    """
        Main function which takes user inputs for which type of antenna to be drawn, size of the square and level/depth
        precondition: Turtle is at relative 0,facing east, pendown
        postcondition: Turtle is at relative 0,facing east, penup
        :return: None
        """

    response=int(input("Enter 1 for sequence of squares,  2 for single line and 3 for perimeter type with gaps"))
    if(response==1):
        side=int(input("Enter side"))
        level=int(input("Enter level"))
        init()
        antenna(level,side)


    elif(response==2):
        size = int(input("Enter size"))
        level = int(input("Enter level"))
        init()
        turtle.left(45)
        for _ in range(4):
            single(size, level)
            turtle.left(90)
        turtle.right(45)




    else:
        size = int(input("Enter size"))
        level = int(input("Enter level"))
        init()
        turtle.left(45)
        for _ in range(4):
            edge(size, level)
            turtle.left(90)
        turtle.right(45)




    turtle.mainloop()


if __name__ == '__main__':
    main()