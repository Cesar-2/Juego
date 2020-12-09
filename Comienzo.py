import pygame
#from pygame.locals import *
import os
import sys

RESOLUTION = [1200,600]
AZUL = (0,0,255)
BLANCO = (255,255,255)
pygame.init()
ventana = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("JUEGO")
fondo = pygame.image.load(os.path.join("IMG","Comienzo.png"))
audio = pygame.mixer.Sound(os.path.join("IMG","audio.mp3"))

miFuente = pygame.font.SysFont("Times New Roman",20)
miFuente2 = pygame.font.SysFont("Times New Roman",30)
miTexto1 = miFuente.render("En busca de las gemas del poder, llega Yondu a un planeta",0,BLANCO)
miTexto2 = miFuente.render("que jamás había conocido, y con tanta suerte que allí encuentra",0,BLANCO) 
miTexto3 = miFuente.render("lo que tanto ha estado buscando, pero, con lo que él no contaba",0,BLANCO) 
miTexto4 = miFuente.render("era con una compañia inesperada... los cuales eran los guardianes",0,BLANCO)
miTexto5 = miFuente2.render("AQUI COMIENZA SU AVENTURA!!!",0,BLANCO)
 
#fin = False
def Cinematica1():
    '''audio.play()
    ventana.blit(fondo,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)
    ventana.blit(miTexto1,(665,20))
    pygame.display.flip()
    pygame.time.wait(3000)
    ventana.blit(miTexto2,(665,40))
    pygame.display.flip()
    pygame.time.wait(3000)
    ventana.blit(miTexto3,(665,60))
    pygame.display.flip()
    pygame.time.wait(3000)
    ventana.blit(miTexto4,(665,80))
    pygame.display.flip()
    pygame.time.wait(7000)
    ventana.blit(miTexto5,(665,130))
    pygame.display.flip()
    pygame.time.wait(10000)
    audio.stop()'''
    pass
    
    
    #pygame.display.update()