from turtle import *
from time import sleep
lag = 0
def branch(length, level):
    if not level:
        return

    forward(length)
    sleep(lag)
    left(45)
    branch(.9*length, level-1)
    right(90)

    branch(.9*length, level-1)
    left(45)
    backward(length)
    sleep(lag)
    return

left(90)
branch(100, 25)
