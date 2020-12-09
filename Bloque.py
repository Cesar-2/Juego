import pygame
import Constantes

class Bloque(pygame.sprite.Sprite):
    def __init__(self,posicion,image) :
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]


    def update(self,mov) :
        self.rect.x -= mov[0]
        self.rect.y -= mov[1]
