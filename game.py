import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Object import GameObject
import numpy as np
import time
import sys
BG_WIDTH = 1072
BG_HEIGHT = 504
IMG_WIDTH = 106
IMG_HEIGHT = 76
NUM_ITEMS = 5



pygame.init()




screen = pygame.display.set_mode((BG_WIDTH , BG_HEIGHT))
clock = pygame.time.Clock()            #get a pygame clock object
item = pygame.image.load('pics/Michigan_Wolverines_Block_M.png').convert()
background = pygame.image.load('pics/football.png').convert()
final = GameObject(pygame.Surface((IMG_WIDTH*2, IMG_HEIGHT*2)), 106*2, 20)
screen.blit(background, (0, 0))
objects = []
p = GameObject(item, 106, 20)


x_coords = np.random.randint(0, BG_WIDTH - IMG_WIDTH, (NUM_ITEMS))
y_coords = np.random.randint(0, BG_HEIGHT - IMG_HEIGHT, (NUM_ITEMS))
idx = 0

iter = 0
while True:



    if p.is_clicked():
        print("clicked")
        idx += 1
    # if final.is_clicked():
    #     print("Memory")
    #     idx += 1
    if idx == NUM_ITEMS:
        print("End iter " + str(iter))
        iter += 1
        idx = 0
        if iter == 5:
            p = final



    screen.blit(background, (0, 0))

    p.set_coords(x_coords[idx], y_coords[idx])
    screen.blit(p.image, p.pos)
    if iter == 5:
        screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or iter == 6:
            print("Sucess")
            sys.exit()

    pygame.display.update()
    clock.tick(60)


