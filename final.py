import pygame
import os

RESOLUTION = [1200,600]
AZUL = (0,0,255)
BLANCO = (255,255,255)
ROJO = (255,0,0)

pygame.init()
ventana = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("final")

imagen1 = pygame.image.load(os.path.join("IMG","FINAL1.png"))
imagen2 = pygame.image.load(os.path.join("IMG","FINAL2.png"))
audio = pygame.mixer.Sound(os.path.join("IMG","final.mp3"))

miFuente = pygame.font.SysFont("Times New Roman",20)
miFuente2 = pygame.font.SysFont("Times New Roman",30)
miFuente3 = pygame.font.SysFont("Times New Roman",60)

miTexto1 = miFuente.render("Finalmente al haber conseguido las gemas",0,BLANCO)
miTexto2 = miFuente.render("Yondu por fin pudo estar en calma y",0,BLANCO)
miTexto3 = miFuente.render("a su vez, pudo mirar nuevos horizontes",0,BLANCO)

miTexto4 = miFuente.render("dejando el planeta que habia conocido",0,BLANCO)
miTexto5 = miFuente.render("para retornar en el espacio exterior",0,BLANCO)
miTexto6 = miFuente.render("en busca de nuevas aventuras...",0,BLANCO)
miTexto7 = miFuente.render("lleno de expectativa y calma...",0,BLANCO)
miTexto8 = miFuente2.render("POR AHORA....",0,ROJO)
miTexto9 = miFuente3.render("FIN",0,AZUL)


def Cinematica3():
    audio.play()
    ventana.blit(imagen1,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)
    ventana.blit(miTexto1,(50,50))
    pygame.display.flip()
    pygame.time.wait(5000)
    ventana.blit(miTexto2,(50,70))
    pygame.display.flip()
    pygame.time.wait(5000)
    ventana.blit(miTexto3,(50,90))
    pygame.display.flip()
    pygame.time.wait(5000)

    #segunda cinematica
    ventana.blit(imagen2,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)
    ventana.blit(miTexto4,(50,50))
    pygame.display.flip()
    pygame.time.wait(5000)
    ventana.blit(miTexto5,(50,70))
    pygame.display.flip()
    pygame.time.wait(5000)
    ventana.blit(miTexto6,(50,90))
    pygame.display.flip()
    pygame.time.wait(5000)
    ventana.blit(miTexto7,(50,110))
    pygame.display.flip()
    pygame.time.wait(6000)
    ventana.blit(miTexto8,(50,160))
    pygame.display.flip()
    pygame.time.wait(3000)
    ventana.blit(miTexto9,(1000,500))
    pygame.display.flip()

fin = False


Cinematica3()
while not fin:
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True