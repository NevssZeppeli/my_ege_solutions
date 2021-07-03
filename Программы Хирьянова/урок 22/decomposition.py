from turtle import *

def init():
    shape('turtle')
    color('red', 'yellow')
    width(3)
    speed(100)
    penup()

def star(length):
    begin_fill()
    pendown()
    for edge in range(5):
        forward(length)
        right(2 * 360 / 5)
    penup()
    end_fill()

init()
for size in 100, 50, 70, 40 сса