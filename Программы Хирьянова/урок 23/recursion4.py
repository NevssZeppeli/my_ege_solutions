from turtle import *

def dragon_curve(length, depth, sign=+1):
    """ Кривая дракона """
    if depth == 0:
        forward(length)
    else:
        left(45*sign)
        dragon_curve(length / 2 ** 0.5, depth - 1, +1)
        right(90*sign)
        dragon_curve(length / 2 ** 0.5, depth - 1, -1)
        left(45*sign)

speed(100)
dragon_curve(100, 7)
