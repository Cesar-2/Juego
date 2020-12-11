import pygame
import Constantes
import os
from Mina import *

ROBOT1 = pygame.image.load(os.path.join("Enemigo_Robot_Volador","RobotV1.png"))
ROBOT2 = pygame.image.load(os.path.join("Enemigo_Robot_Volador","RobotV2.png"))
ROBOT3 = pygame.image.load(os.path.join("Enemigo_Robot_Volador","RobotV3.png"))

class Robot(pygame.sprite.Sprite):
    def __init__(self,posicion,vel) :
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.imagenes = [ROBOT1,ROBOT2,ROBOT3]
        self.image = self.imagenes[self.accion]
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.animacion = 0
        self.velx = vel
        self.cooldown = 50
        self.voltear = 10

    
    def update(self, mov):
        self.rect.x -= mov[0] + self.velx
        self.rect.y -= mov[1] 
        if self.animacion == 1:
            if self.accion != 2:
                self.accion += 1
            else:
                self.accion = 0
            self.animacion = 0
        else:
            self.animacion += 1

        if self.voltear == 0:
            self.velx = - self.velx
            self.voltear = 10
            
        self.image = self.imagenes[self.accion]

        if self.cooldown != 0:
            self.cooldown -= 1
            return None
        else:
            self.cooldown = 50
            return self.ponerMinas()

    def ponerMinas(self):

        mm = Mina([self.rect.x + (self.rect.width/2) , self.rect.y + (self.rect.height)])
        return mm