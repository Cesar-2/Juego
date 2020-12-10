import pygame
from Bala import *
widht = 800
height = 600
velocidad = 10
velocidadSalto = 28
gravedad = 4

class Jugador(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        self.hoja = pygame.image.load("Sprites.png")
        self.contador=0
        self.bandera=False
        self.velocidadX=0
        self.velocidadY=0
        self.hoja.set_clip(pygame.Rect(10*2, 5*2, 37*2, 46*2))
        self.imagen = self.hoja.subsurface(self.hoja.get_clip())
        self.rect = self.imagen.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.figura = 0
        self.gemas = 0
        self.escalar = False
        self.contGravedad = 1
        self.gravedad = True
        self.escalando = False
        self.bajar = False
        self.bajando = False
        self.derecha = True
        self.izquierda = False
        self.salto = False
        self.estados_der = {0: (9*2, 56*2, 37*2, 46*2), 1: (64*2, 55*2, 32*2, 47*2), 2: (112*2, 56*2, 35*2, 46*2), 3: (159*2, 56*2, 38*2, 46*2), 4: (212*2, 56*2, 36*2, 46*2), 5: (268*2, 55*2, 32*2, 47*2), 6: (316*2, 56*2, 35*2, 46*2), 7: (363*2, 56*2, 40*2, 46*2)}
        self.estados_izq = {0: (6*2, 107*2, 37*2, 46*2), 1: (58*2, 106*2, 32*2, 47*2), 2: (109*2, 107*2, 35*2, 46*2), 3: (161*2, 107*2, 38*2, 46*2), 4: (212*2, 107*2, 36*2, 46*2), 5: (262*2, 106*2, 32*2, 47*2), 6: (313*2, 107*2, 35*2, 46*2), 7: (363*2, 107*2, 40*2, 46*2)}
        self.estados_quietos = {0: (209*2, 5*2, 37*2, 46*2), 1: (10*2, 5*2, 37*2, 46*2)} # 0: Izquierda, 1: Derecha
        self.estados_escaleras = {0: (13*2 ,159*2 ,25*2 ,52*2), 1: (64*2 ,160*2, 25*2, 49*2), 2: (116*2 ,160*2 ,25*2, 49*2), 3: (167*2 ,159*2, 26*2, 52*2), 4: (116*2 ,160*2 ,25*2, 49*2), 5: (64*2 ,160*2, 25*2, 49*2)}
        self.estados_saltos = {0: (226,6,70,95), 1: (312*2, 5*2, 35*2, 46*2)} #0: Derecha, 1: Izquierda
        self.max_health = 100
        self.health = 100

    def shoot(self):
        if self.derecha:
            bala = Bala([self.rect.x, self.rect.y],-20)
        if self.izquierda:
            bala = Bala([self.rect.x, self.rect.y],+20)
        return bala
    
    def get_figura(self,estados):
        self.figura += 1
        if self.figura > (len(estados) - 1):
            self.figura = 0
        return estados [self.figura]

    def corte (self,rect_cortado):
        if type(rect_cortado) is dict:
            self.hoja.set_clip(pygame.Rect(self.get_figura(rect_cortado)))
        else:
            self.hoja.set_clip(pygame.Rect(rect_cortado))
        return rect_cortado

    def actualizacion(self,direccion):
        if direccion == 'izq':
            self.corte(self.estados_izq)
        if direccion == 'der':
            self.corte(self.estados_der)
        if direccion == 'arriba':
            self.corte(self.estados_escaleras)
        if direccion == 'abajo':
            self.corte(self.estados_escaleras)
        if direccion == 'quieto_izq':
            self.corte(self.estados_quietos[0])
        if direccion == 'quieto_der':
            self.corte(self.estados_quietos[1])
        if direccion == 'salto':
            if self.derecha :
                self.corte(self.estados_saltos[0])
            elif self.izquierda :
                self.corte(self.estados_saltos[1])
        self.imagen = self.hoja.subsurface(self.hoja.get_clip())

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.rect.x-20, self.rect.y + 100 + 10, 100, 10))
        pygame.draw.rect(window, (0,255,0), (self.rect.x-20, self.rect.y + 100 + 10, 100 * (self.health/self.max_health), 10))

    def evento(self,event):
        jDesplazamientoX = 0
        jDesplazamientoY = gravedad * self.contGravedad
        self.contGravedad+=1
        self.actualizacion('')
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.derecha = False
                self.izquierda = True
                if not self.salto :
                    self.actualizacion('izq')
                else:
                    self.actualizacion ('salto')
                jDesplazamientoX = -(velocidad)
                
            if event.key == pygame.K_RIGHT:
                self.derecha = True
                self.izquierda = False
                if not self.salto :
                    self.actualizacion('der')
                else:
                    self.actualizacion ('salto')
                jDesplazamientoX = velocidad

            if event.key == pygame.K_UP:
                if self.escalar :
                    self.actualizacion('arriba')
                    jDesplazamientoY = -velocidad
                    self.escalando = True
                    self.contGravedad = 0

            if event.key == pygame.K_DOWN:
                if self.escalar :
                    self.actualizacion('abajo')
                    jDesplazamientoY = velocidad
                    self.escalando = True
                    self.contGravedad = 0
                    if self.bajar:
                        self.bajando = True

            if event.key == pygame.K_LCTRL:
                if not self.salto:
                    self.salto = True
                    self.actualizacion ('salto')
                    self.contGravedad = -7
                    jDesplazamientoY = -28
                 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if not self.salto :
                    self.actualizacion('quieto_izq')
                else:
                    self.actualizacion('salto')
                self.velocidadX = 0

            if event.key == pygame.K_RIGHT:
                if not self.salto :
                    self.actualizacion('quieto_der')
                else:
                    self.actualizacion('salto')
                self.velocidadX = 0

        return [jDesplazamientoX, jDesplazamientoY]
