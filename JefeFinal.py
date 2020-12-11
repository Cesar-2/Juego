import pygame
import Constantes
import numpy as np
from Bala import *


class JefeFinal(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.imagenesDerecha = [pygame.image.load("Ozarnus_Der/Kirby.png"), pygame.image.load("Ozarnus_Der/Kirby1.png"), pygame.image.load("Ozarnus_Der/Kirby2.png"), pygame.image.load(
            "Ozarnus_Der/Kirby3.png"), pygame.image.load("Ozarnus_Der/Kirby4.png"), pygame.image.load("Ozarnus_Der/Kirby5.png"), pygame.image.load("Ozarnus_Der/Kirby6.png"), pygame.image.load("Ozarnus_Der/Kirby7.png")]
        self.imagenesIzquierda = [pygame.image.load("Ozarnus_Izq/Kirby.png"), pygame.image.load("Ozarnus_Izq/Kirby1.png"), pygame.image.load("Ozarnus_Izq/Kirby2.png"), pygame.image.load(
            "Ozarnus_Izq/Kirby3.png"), pygame.image.load("Ozarnus_Izq/Kirby4.png"), pygame.image.load("Ozarnus_Izq/Kirby5.png"), pygame.image.load("Ozarnus_Izq/Kirby6.png"), pygame.image.load("Ozarnus_Izq/Kirby7.png")]
        self.image = self.imagenesIzquierda[self.accion]
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.max_health = 500
        self.health = 500
        self.direction = 0
        self.animacion = 0

    def shoot(self):
        if self.direction == 1:
            bala = Bala([self.rect.x, self.rect.y],-20)
        if self.direction == 0:
            bala = Bala([self.rect.x, self.rect.y],+20)
        return bala

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.rect.x-20, self.rect.y + 100 + 10, 100, 10))
        pygame.draw.rect(window, (0,255,0), (self.rect.x-20, self.rect.y + 100 + 10, 100 * (self.health/self.max_health), 10))
    
    def update(self, mov, posicion):
        self.rect.x -= mov[0]
        self.rect.y -= mov[1]
        if self.animacion == 1:
            if self.accion != 1:
                self.accion += 1
            else:
                self.accion = 0
            self.animacion = 0
        else:
            self.animacion += 1
        if self.rect.x > posicion[0]:
            self.direction = 0
        if self.rect.x < posicion[0]:
            self.direction = 1
        if self.direction == 0:
            self.image = self.imagenesIzquierda[self.accion]
        if self.direction == 1:
            self.image = self.imagenesDerecha[self.accion]
        x = posicion[0]-self.rect.x
        y = posicion[1]-self.rect.y
        movimientox = int(x/np.sqrt(x**2+y**2)*2)
        movimientoy = int(y/np.sqrt(x**2+y**2)*2)
        self.rect.x += movimientox
        self.rect.y += movimientoy
