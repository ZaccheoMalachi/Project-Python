from turtle import *
def drawcircle(size:float=2.5,quality:int=2,color:str='white'):
    speed(0)
    fillcolor(color)
    begin_fill()
    for i in range(180):
        forward(size)
        left(quality)
    end_fill()
def drawhalfcircle(size:float=2.5,quality:int=-2,color:str='white'):
    right(90)
    speed(0)
    fillcolor(color)
    begin_fill()
    for i in range(90):
        forward(size)
        left(quality)
    end_fill()
def moveto():
    penup()
    goto(50,-118)
    pendown()