import pygame
import Constantes

class Escalera(pygame.sprite.Sprite):
    def __init__(self,posicion,image,bajar):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.bajar = bajar

    def update(self,mov) :
        self.rect.x -= mov[0]
        self.rect.y -= mov[1]
