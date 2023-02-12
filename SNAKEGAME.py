import pygame as pg
from time import sleep
pg.init()
color=(25,255,50)
game=pg.display.set_mode((1000,800))
pg.display.set_caption('GUD GEM')
gemicon=pg.image.load('SNIKGAME.jpg')
pg.display.set_icon(gemicon)
ded=False
while not ded:
    for event in pg.event.get():
        # print(event)
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_w:
                print('up')
        if event.type==pg.QUIT:
            ded=True
    pg.draw.circle(game,color,[500,400],5)
    pg.display.update()
pg.quit()