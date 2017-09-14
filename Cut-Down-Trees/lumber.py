"""
file: lumber.py
language:python 3
author: pan7447@cs,rit,edu Parvathi Nair
author: dck1135@cs.rit.edu Darshan Kavathe
description: To generate trees on click on the window and then harvest the same and draw logs
precondition: Turtle is at coordinates(0,0),facing east, pendown
postcondition: Turtle is at coordinates(0,0),facing east, penup
"""

import turtle
import random
import yard

ObjYard = yard.LumberYard() #create and assign the object 'LumberYard'
WINDOW_WIDTH = 400  # global variable to set the dimensions of the window
WINDOW_HEIGHT = 400  # global variable to set the dimensions of the window
MARGIN = 50  # global variable to set a distance from the bottom and top border of the window


def init():
    """
    Initialize for drawing.  (-200, -200) is in the lower left and (200, 200) is in the upper right.

    precondition: Turtle is at coordinates(0,0),facing east, pendown
    postcondition: Turtle is at coordinates(0,0),facing east, penup
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.speed(6)
    turtle.setheading(0)
    turtle.title('lumber')


def bottom_Division():
    """
    Draws division line in the bottom (horizontal line) and two buttons - 1. harvest and sort and 2. harvest unsorted

    precondition: Turtle is at coordinates(0,0),facing east, penup
    postcondition: Turtle is at coordinates(0,-150),facing east, penup
    :return: None
    """
    turtle.setheading(270)
    turtle.forward(WINDOW_HEIGHT / 2 - MARGIN)
    turtle.down()
    turtle.left(90)
    turtle.forward(WINDOW_WIDTH / 2)
    turtle.penup()
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(WINDOW_WIDTH)
    turtle.up()
    turtle.setheading(0)
    turtle.forward(WINDOW_WIDTH / 4)
    turtle.right(90)
    turtle.forward(MARGIN / 2)
    turtle.down()
    turtle.left(90)
    turtle.write("harvest and sort", False, align="center", font=("Arial", 12, "normal"))
    turtle.up()
    turtle.forward(WINDOW_WIDTH / 2)
    turtle.down()
    turtle.write("harvest unsorted", False, align="center", font=("Arial", 12, "normal"))
    turtle.up()
    turtle.setheading(90)
    turtle.forward(MARGIN / 2)
    turtle.setheading(180)
    turtle.forward(WINDOW_WIDTH / 4)
    turtle.setheading(0)


def doclick(x, y):
    """
    sets the position of the turtle to clicked position, performs the specified action depending on which section of the window the user clicks

    precondition: Turtle is at relative 0,0 (wherever the user clicks),facing east, penup
    postcondition: Turtle is at relative 0,0 (wherever the user clicks),facing east, penup
    :return: None

    """
    turtle.goto(x, y)
    if y > (-WINDOW_HEIGHT / 2 + MARGIN) and (y < WINDOW_HEIGHT / 2 - MARGIN): #Checks the section of window where the user clicks
        draw_tree()
    else:
        if x > 0:
            unsort_harvest()
        else:
            sort_harvest()


def draw_trunk():
    """
    draws trunk with random length and checks if it crosses margin
    uses add log to store the length of the trunks

    :return: trunkLength(length of the trunk)
    precondition: Turtle is at relative (0,0),facing east, penup
    postcondition: Turtle is at relative (0,trunkLength),facing east, penup
    trunkLength is a random value created using randint function

    """
    trunkLength = random.randint(50, 250)
    y = turtle.ycor()
    if (trunkLength + y) > (WINDOW_HEIGHT / 2 - MARGIN):
        trunkLength = WINDOW_HEIGHT / 2 - MARGIN - y
    turtle.pendown()
    turtle.left(90)
    turtle.forward(trunkLength)
    turtle.right(90)
    turtle.penup()
    ObjYard.addLog(trunkLength)
    return trunkLength


def draw_pine():
    """
    draws the pine tree

    precondition: Turtle is at relative (0,0),facing east, penup
    postcondition: Turtle is at relative (0,0),facing east, penup
    :return: None
    """
    backToPosition = draw_trunk()
    length = 30
    turtle.setheading(180)
    turtle.forward(length / 2)
    turtle.setheading(0)
    turtle.pendown()
    for _ in range(3):
        turtle.forward(length)
        turtle.left(360 / 3)
    turtle.forward(length / 2)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(backToPosition)
    turtle.setheading(0)


def draw_maple():
    """
    draws the maple tree

    precondition: Turtle is at relative (0,0),facing east, penup
    postcondition: Turtle is at relative (0,0),facing east, penup
    :return: None
    """
    backToPosition = draw_trunk()
    radius = 15
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(backToPosition)
    turtle.setheading(0)


def draw_square():
    """
    draws the square tree

    precondition: Turtle is at relative (0,0),facing east, penup
    postcondition: Turtle is at relative (0,0),facing east, penup
    :return: None
    """
    backToPosition = draw_trunk() #backToPosition variable gets the trunkLength from draw_trunk function
    length = 30
    turtle.setheading(180)
    turtle.forward(length / 2)
    turtle.setheading(0)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(length)
        turtle.left(360 / 4)
    turtle.penup()
    turtle.forward(length / 2)
    # turtle is set to the position on the window where the user clicked
    turtle.setheading(270)
    turtle.forward(backToPosition)
    turtle.setheading(0)


def draw_pile(logs, n):
    """
    draws the logs after harvest

    precondition: Turtle is at relative (0,0),facing east, pendown
    postcondition: Turtle is at relative (0,0),facing east, penup
    """
    logHeight = 10 #Given width of the log


    for i in range(n):
        turtle.pendown()
        turtle.forward(logs[i] / 2)
        turtle.left(90)
        turtle.forward(logHeight)
        turtle.left(90)
        turtle.forward(logs[i])
        turtle.left(90)
        turtle.forward(logHeight)
        turtle.left(90)
        turtle.forward(logs[i] / 2)
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(logHeight)
        turtle.setheading(0)
    turtle.penup()
    turtle.right(90)
    turtle.forward(n * logHeight)
    turtle.setheading(0)


def print_total_length(logs, n):
    """
    prints the total length in the console

    :param logs: contains the list of length of all the trunks, to be drawn after harvest
    :param n: represents the total number of trunks harvested
    :return: None

    """
    totalLength = sum(logs)
    print(totalLength)


def draw_tree():
    """
    here the type of tree is randomly decided and respective functions are called

    precondition: Turtle is at relative (0,0),facing east, penup
    postcondition: Turtle is at relative (0,0),facing east, penup
    :return:
    """
    tree_type = random.randint(1, 3)

    if tree_type == 1:
        draw_maple()
    elif tree_type == 2:
        draw_pine()
    else:
        draw_square()
    turtle.penup()


def unsort_harvest():
    """
    takes the list of the length of all trunks, calls the darw_pile function to draw the logs
    and calls the print_total_length function to print the total length of all the trunks kept together

    precondition: Turtle is at coordinates(0,0),facing east, pendown
    postcondition: Turtle is at coordinates(0,0),facing east, penup
    :return:
    """
    turtle.reset()
    logs = ObjYard.allLogs()
    n = len(logs)
    draw_pile(logs, n)
    print_total_length(logs, n)
    turtle.exitonclick()


def sort_harvest():
    """
    takes the list of the length of all trunks, sorts the list, calls the darw_pile function to draw the logs
    and calls the print_total_length function to print the total length of all the trunks kept together

    precondition: Turtle is at coordinates(0,0),facing east, pendown
    postcondition: Turtle is at coordinates(0,0),facing east, penup
    :return:
    """
    turtle.reset()
    log = ObjYard.allLogs()
    logs = sorted(log, reverse=True)
    n = len(logs)
    draw_pile(logs, n)
    print_total_length(logs, n)
    turtle.exitonclick()


def main():
    """
    main function , return type none

    precondition: Turtle is at coordinates(0,0),facing east, pendown
    postcondition: Turtle is at coordinates(0,0),facing east, penup
    :return : None
    """
    init()
    bottom_Division()
    turtle.onscreenclick(fun=doclick)
    turtle.mainloop()


if __name__ == '__main__':
    main()