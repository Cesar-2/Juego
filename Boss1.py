import pygame
import Constantes

class Abeja(pygame.sprite.Sprite):
    def _init_(self, posicion):
        pygame.sprite.Sprite._init_(self)
        self.accion = 0
        self.imagenesDerecha = [pygame.image.load("Enemigo_abeja/Abeja1_derecha.png"),pygame.image.load("Enemigo_abeja/Abeja2_derecha.png")]
        self.imagenesIzquierda = [pygame.image.load("Enemigo_abeja/Abeja1_izquierda.png"),pygame.image.load("Enemigo_abeja/Abeja2_izquierda.png")]
        self.image = self.imagenes[self.accion]
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.direction = 0
        self.animacion = 0
        self.health = 1000

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
        self.image = self.imagenes[self.accion]