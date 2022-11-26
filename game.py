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


pygame.init()




screen = pygame.display.set_mode((BG_WIDTH , BG_HEIGHT))
clock = pygame.time.Clock()            #get a pygame clock object
item = pygame.image.load('pics/Michigan_Wolverines_Block_M.png').convert()
background = pygame.image.load('pics/football.png').convert()
screen.blit(background, (0, 0))
objects = []
p = GameObject(item, 106, 20)


x_coords = np.random.randint(0, BG_WIDTH - IMG_WIDTH, (10))
y_coords = np.random.randint(0, BG_HEIGHT - IMG_HEIGHT, (10))
idx = 0
time_records = [time.time()]

while True:
    if p.is_clicked():
        idx += 1
        time_records.append(time.time())
    if idx == 10:
        print(time_records)
        sys.exit()


    screen.blit(background, (0, 0))
    p.set_coords(x_coords[idx], y_coords[idx])
    screen.blit(p.image, p.pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(time_records)
            sys.exit()




    pygame.display.update()
    clock.tick(60)


