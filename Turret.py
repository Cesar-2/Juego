import pygame
import Constantes
from Bala import *


class Turret(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.imagenes = [pygame.transform.scale(pygame.image.load("Enemigo_torreta/TurretL.png"),(80,80)),pygame.transform.scale(pygame.image.load("Enemigo_torreta/TurretR.png"),(80,80))]
        self.image = self.imagenes[self.accion]
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]-16
        self.rect.y = posicion[1]-16
        self.direction = 0
        self.cooldown = 50


    def shoot(self):
        if self.direction == 1:
            bala = Bala([self.rect.x, self.rect.y],-20)
        if self.direction == 0:
            bala = Bala([self.rect.x, self.rect.y],+20)
        return bala

    def update(self, mov,posx):
        self.rect.x -= mov[0] 
        self.rect.y -= mov[1]
        if self.rect.x > posx:
            self.direction = 0
        if self.rect.x < posx:
            self.direction = 1
        if self.direction == 0: 
            self.accion = 0
        if self.direction == 1:
            self.accion = 1
        self.image=self.imagenes[self.accion]