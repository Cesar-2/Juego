import pygame
import Constantes
import numpy as np

class Abeja(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.imagenesDerecha = [pygame.image.load("Enemigo_abeja/Abeja1_derecha.png"),pygame.image.load("Enemigo_abeja/Abeja2_derecha.png")]
        self.imagenesIzquierda = [pygame.image.load("Enemigo_abeja/Abeja1_izquierda.png"),pygame.image.load("Enemigo_abeja/Abeja2_izquierda.png")]
        self.image = self.imagenesIzquierda[self.accion]
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.direction = 0
        self.animacion = 0

    def update(self,mov,posicion):
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
        movimientox = int(x/np.sqrt(x**2+y**2)*5)
        movimientoy = int(y/np.sqrt(x**2+y**2)*5)
        self.rect.x += movimientox
        self.rect.y += movimientoy

