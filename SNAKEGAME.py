import pygame as pg
from time import sleep
pg.init()
fps=15
clock=pg.time.Clock()
color=(25,255,50)
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
size=5
fontstyle=pg.font.Font('DotGothic16-Regular.ttf',60)
# fontstyle=pg.font.SysFont(None,50)
def displaymessage(msg,color):
    msg=fontstyle.render(msg,True,color)
    game.blit(msg,[width/2-150,height/2-75])
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
            ded=True
    if x<=0 or x>=width or y<=0 or y>=height:
        ded=True
    x+=changeX
    y+=changeY
    game.fill(black)
    pg.draw.rect(game,color,[x,y,size,size])
    pg.display.update()
    clock.tick(fps)
displaymessage('GAME OVER!!!',rEd)
pg.display.update()
sleep(4)
pg.quit()