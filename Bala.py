import pygame
import pygame
import Constantes


class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion, vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Bala.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.velx = vel

    def update(self, mov):
        self.rect.x -= mov[0] + self.velx
        self.rect.y -= mov[1]
