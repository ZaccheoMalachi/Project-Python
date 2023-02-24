import pygame as pg
from time import sleep
from random import randint
pg.init()
fps=16
snakelist=[]
snakelegth=4
clock=pg.time.Clock()
color=(25,255,50)
blue=(0,0,255)
purple=(148,0,211)
width=1000
height=800
black=(0,0,0)
rEd=(255,0,0)
game=pg.display.set_mode((width,height))
pg.display.set_caption('GUD GEM')
gemicon=pg.image.load('SNIKGAME.jpg')
pg.display.set_icon(gemicon)
ded=False
x=width/2
y=height/2
changeX=0
changeY=0
size=7
foodX=randint(0,width)
foodY=randint(0,height)
poisonX=randint(0,width)
poisonY=randint(0,height)
score=0
fontstyle=pg.font.Font('DotGothic16-Regular.ttf',60)
fontstyleSc=pg.font.Font('DotGothic16-Regular.ttf',40)
# fontstyle=pg.font.SysFont(None,50)
def displaymessage(msg,color,fontstyleUSE,x,y):
    msg=fontstyleUSE.render(msg,True,color)
    game.blit(msg,[x,y])
while not ded:
    for event in pg.event.get():
        # print(event)
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_w:
                changeY=-size
                changeX=0
            elif event.key==pg.K_a:
                changeX=-size
                changeY=0
            elif event.key==pg.K_s:
                changeY=+size
                changeX=0
            elif event.key==pg.K_d:
                changeX=+size
                changeY=0
        if event.type==pg.QUIT:
            pg.quit()
    if x<=0 or x>=width or y<=0 or y>=height:
        ded=True
    if x<=foodX+7 and x>=foodX-7 and y<=foodY+7 and y>=foodY-7:
        print('snik eat')
        score+=1
        snakelegth+=3
        foodX=randint(5,width-5)
        foodY=randint(5,height-5)
        poisonX=randint(5,width-5)
        poisonY=randint(5,height-5)
    if x<=poisonX+7 and x>=poisonX-7 and y<=poisonY+7 and y>=poisonY-7:
        print('snik poison')
        score-=1
        snakelegth-=3
        for i in range(3):
            if snakelegth<=3:
                ded=True
                break
            del snakelist[0]
        foodX=randint(5,width-5)
        foodY=randint(5,height-5)
        poisonX=randint(5,width-5)
        poisonY=randint(5,height-5)
        if score<0:
            ded=True
    x+=changeX
    y+=changeY
    game.fill(black)
    mscore='Score='+str(score)
    displaymessage(mscore,rEd,fontstyleSc,850,1)
    snakelist.append([x,y])
    if len(snakelist)>snakelegth:
        del snakelist[0]
    for i in snakelist:
        pg.draw.rect(game,color,[i[0],i[1],size,size])
    pg.draw.rect(game,blue,[foodX,foodY,size-2,size-2])
    pg.draw.rect(game,purple,[poisonX,poisonY,size-2,size-2])
    pg.display.update()
    clock.tick(fps)
displaymessage('GAME OVER!!!',rEd,fontstyle,width/2-150,height/2-75)
pg.display.update()
sleep(4)
pg.quit()