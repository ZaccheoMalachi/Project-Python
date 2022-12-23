from turtle import *
pensize(5)
pencolor('cyan')
speed(0)
for i in range(8    ):
    forward(120)
    for i in range(3):
        backward(30)
        left(45)
        forward(30)
        backward(30)
        right(90)
        forward(30)
        backward(30)
        left(45)
    backward(30)
    left(45)