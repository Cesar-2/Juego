import pygame
import Constantes

ROBOT1 = pygame.image.load("Enemigo_Robot/Robot1.png")
ROBOT2 = pygame.image.load("Enemigo_Robot/Robot2.png")
ROBOT3 = pygame.image.load("Enemigo_Robot/Robot3.png")

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
        self.voltear = 10
        self.velx = vel

    
    def update(self, mov):
        self.rect.x -= mov[0] + self.velx
        self.rect.y -= mov[1] - Constantes.gravedad 
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
        else:
            self.voltear -= 1
        self.image = self.imagenes[self.accion]