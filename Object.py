import pygame
from pygame.locals import *
from pygame.sprite import Sprite


class GameObject(Sprite):
    def __init__(self, image, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = image
        # self.rect = self.image.get_rect()
        self.pos = image.get_rect()


    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.pos.collidepoint(pygame.mouse.get_pos())


    def set_coords(self, x, y):
        self.pos.right = x
        self.pos.top = y
