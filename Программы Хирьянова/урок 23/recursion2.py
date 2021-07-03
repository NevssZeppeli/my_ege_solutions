from turtle import *

def go_snowy(length):
    """ Кривая Коха """
    if length < 20:
        forward(length)
    else:
        go_snowy(length / 3)
        left(60)
        go_snowy(length / 3)
        right(120)
        go_snowy(length / 3)
        left(60)
        go_snowy(length / 3)

speed(100)

for side in range(3):
    go(200)
    right(120)
