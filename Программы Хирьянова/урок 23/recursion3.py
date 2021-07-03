from turtle import *

def levi_curve(length, depth):
    """ Кривая Леви """
    if depth == 0:
        forward(length)
    else:
        left(45)
        levi_curve(length / 2 ** 0.5, depth - 1)
        right(90)
        levi_curve(length / 2 ** 0.5, depth - 1)
        left(45)

speed(100)
for level in range(10):
    goto(0, 0)
    hexcolor = hex(250 - level*25)[2:].zfill(2)
    color("#FF" + hexcolor*2)
    levi_curve(100, level)
