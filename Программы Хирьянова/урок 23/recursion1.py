from turtle import *

def go(length):
    """ Канторово множество """
    if length < 3:
        forward(length)
    else:
        go(length / 3)
        penup()
        forward(length / 3)
        pendown()
        go(length / 3)

go(300)
