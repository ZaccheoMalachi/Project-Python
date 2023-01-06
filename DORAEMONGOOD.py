from turtle import *
from time import sleep
setup(750,750)
shape('turtle')
def drawCircle(size,isfilled):
    if isfilled:
        begin_fill()
    setheading(180)
    circle(size)
    if isfilled:
        end_fill()
def drawRec(length,wide,isfilled):
    if isfilled:
        begin_fill()
    for i in range(2):
        forward(length)
        right(90)
        forward(wide)
        right(90)
    if isfilled:
        end_fill()
def drawHead():
    color('cyan','cyan')
    penup()
    goto(0,100)
    pendown()
    drawCircle(75,True)
    color('white','white')
    penup()
    goto(0,72)
    drawCircle(60,True)
drawHead()
sleep(5)