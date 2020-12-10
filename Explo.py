import pygame
import Constantes

BOOM1 = pygame.image.load("explosion1.png")
BOOM2 = pygame.image.load("explosion2.png")
BOOM3 = pygame.image.load("explosion3.png")
BOOM4 = pygame.image.load("explosion4.png")
BOOM5 = pygame.image.load("explosion5.png")
BOOM6 = pygame.image.load("explosion6.png")
BOOM7 = pygame.image.load("explosion7.png")

class Explo(pygame.sprite.Sprite):
    def __init__(self,posicion) :
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.imagenes = [BOOM1,BOOM2,BOOM3,BOOM4,BOOM5,BOOM6,BOOM7]
        self.image = self.imagenes[self.accion]
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.animacion = 0
        self.terminar = False
    
    def update(self,mov) :
        self.rect.x -= mov[0]
        self.rect.y -= mov[1]
        if self.animacion == 1:
            if self.accion != 6:
                self.accion += 1
            else:
                self.terminar = True
            self.animacion = 0
        else:
            self.animacion += 1
        self.image = self.imagenes[self.accion]