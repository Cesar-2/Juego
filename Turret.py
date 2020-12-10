import pygame
import Constantes

class Turret(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.imagenes = [pygame.image.load("Bala.png")]
        self.image = pygame.image.load("Bala.png")
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]

    def update(self, mov):
        self.rect.x -= mov[0] 
        self.rect.y -= mov[1]
