import pygame
import os

RESOLUTION = [1200,600]
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)

pygame.init()
ventana = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("nudo")

imagen1 = pygame.image.load(os.path.join("IMG","gema2.png"))
imagen2 = pygame.image.load(os.path.join("IMG","portal3.png"))

audio1 = pygame.mixer.Sound(os.path.join("IMG","laser.mp3"))
audio2 = pygame.mixer.Sound(os.path.join("IMG","nudo.mp3"))

miFuente = pygame.font.SysFont("Times New Roman",20)
miFuente2 = pygame.font.SysFont("Times New Roman",30)

miTexto1 = miFuente.render("Al derrotar a los Nurxianos, Yondu obtuvo una gema",0,BLANCO,NEGRO)
miTexto2 = miFuente.render("unica del cual, pensó que habia culminado su mision...",0,BLANCO,NEGRO)
miTexto3 = miFuente.render("pero de la nada sin previo aviso un",0,BLANCO,NEGRO)
miTexto4 = miFuente.render("un disparo sale de la nada en direccion a él",0,BLANCO,NEGRO)
#miTexto5 = miFuente.render("a él.",0,BLANCO,NEGRO)
miTexto5 = miFuente.render("En ese momento se dio cuenta que su",0,BLANCO)
miTexto6 = miFuente.render("aventura no termina y puede divisar como",0,BLANCO)
miTexto7 = miFuente.render("a lo lejos se ve un portal del cual es activado",0,BLANCO)
miTexto8 = miFuente.render("por la gema que escondía Norza",0,BLANCO)

fin = False
def Cinematica2():
    
    ventana.blit(imagen1,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)
    audio2.play()
    ventana.blit(miTexto1,(50,50))
    pygame.display.flip()
    pygame.time.wait(6000)
    ventana.blit(miTexto2,(50,70))
    pygame.display.flip()
    pygame.time.wait(6000)
    ventana.blit(miTexto3,(50,90))
    pygame.display.flip()
    pygame.time.wait(6000)
    ventana.blit(miTexto4,(50,110))
    pygame.display.flip()
    pygame.time.wait(1500)
    audio1.play()
    pygame.time.wait(1500)

    #segunda cinematica
    ventana.blit(imagen2,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)
    ventana.blit(miTexto5,(430,460))
    pygame.display.flip()
    pygame.time.wait(6000)
    ventana.blit(miTexto6,(430,480))
    pygame.display.flip()
    pygame.time.wait(6000)
    ventana.blit(miTexto7,(430,500))
    pygame.display.flip()
    pygame.time.wait(6000)
    ventana.blit(miTexto8,(430,520))
    pygame.display.flip()
    pygame.time.wait(6000)
    audio2.stop()
    