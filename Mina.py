import pygame
import Constantes

class Mina(pygame.sprite.Sprite):
    def __init__(self,posicion) :
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.imagenes = [pygame.image.load("Mina/Mina1.png"),pygame.image.load("Mina/Mina2.png"),pygame.image.load("Mina/Mina3.png"),pygame.image.load("Mina/Mina4.png"),
        pygame.image.load("Mina/Mina3.png"),pygame.image.load("Mina/Mina2.png")]
        self.image = imagenes[accion]
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.animacion = 0


    def update(self,mov) :
        self.rect.x -= mov[0]
        self.rect.y -= mov[1]
        if self.animacion == 3:
            if self.accion == 6:
                self.accion = 0
            else:
                self.accion += 1
            self.animacion = 0
        else:
            self.animacion += 1
        self.image = self.imagenes[accion]
