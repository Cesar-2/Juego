import pygame
import Constantes
import numpy as np
from Abeja import *

class BossFinal(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.image = pygame.image.load("Panal.png")
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.animacion = 0
        self.max_health = 1000
        self.health = 1000

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.rect.x-20, self.rect.y + 100 + 10, 100, 10))
        pygame.draw.rect(window, (0,255,0), (self.rect.x-20, self.rect.y + 100 + 10, 100 * (self.health/self.max_health), 10))

    def update(self,mov):
        self.rect.x -= mov[0]
        self.rect.y -= mov[1]

    def crear_abeja(self):
        abeja = Abeja(self.rect)
        return abeja