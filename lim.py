import pygame

class LimClass(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

    def update(self,mov):
        self.x -= mov[0]
        self.y -= mov[1]
