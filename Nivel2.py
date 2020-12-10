import pygame
from Constantes import *
import base64
import json
import csv
import gzip
from Jugador import *
from nudo import *
from Escalera import *
from Bloque import *
from Gema import *
import sys
from pygame.locals import*
from Nivel1 import *

width=100
height=720
black = (0,0,0)
blue = (0, 0, 255)
white = (255,255,255)
red = (180,0,0)
green = (0,180,0)

backgroundColor = (205,69,159)

redSelected = (255,0,0)
greenSelected = (0,255,0)

screen = pygame.display.set_mode((widht, height))

def uploadMap(name):

    global mapWidth,mapHeight,tileHeight,tileWidth,matrizMap

    f = open(name+".json", "r")
    data = json.load(f)
    f.close()

    tileWidth=data["tilewidth"]
    tileHeight=data["tileheight"]

    mapWidth=data["width"]
    mapHeight=data["height"]

    #obtener mapa
    for item in data["layers"]:
        mapa=item["data"]

    #print (mapa)

    for i in range(0, len(mapa), mapWidth):
        matrizMap.append(mapa[i:i+mapWidth])
    #for i in range(mapHeight):
    #    print (matrizMap[i])

def arrayTileset(img):
    x=0
    y=0

    hojaTiles=[]

    for i in range(8):
        for h in range(8):
            imagen=cut(img,(x,y,64,64))
            hojaTiles.append(imagen)
            x+=64
        x=0
        y+=64

    return hojaTiles

def cut (img, rectangle):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(img,(0,0), rect)
    return image

def nivel2():
    #pygame.quit()
    screen = pygame.display.set_mode((1200, 1000))
    Cinematica2()
    pygame.display.set_caption("sprite")
    reloj = pygame.time.Clock()
    game_over = False
    jugador = Jugador([600, 300])
    desplazamientoX = 0 #-100
    desplazamientoY = 0 #-1400
    jugador.gemas=0
    #inicializamos pygame
    pygame.init()
    #imagen = pygame.image.load("fondo.png")
    #screen.blit(imagen ,(0,0))
    pygame.display.set_caption("Mapa")
    clock = pygame.time.Clock()
    img = pygame.image.load("juego.png")
    uploadMap("mapa2")
    hoja = arrayTileset(img)

    #Cargar las imagenes de los Sprites
    Bloque1 = img.subsurface(0,0,64,64)
    Bloque2 = img.subsurface(64,0,64,64)
    Bloque3 = img.subsurface(128,0,64,64)
    #BloqueL = img.subsurface(384,448,64,64)
    Caja = img.subsurface(384,0,64,64)
    Escalera1 = img.subsurface(256,320,64,64)
    Escalera2 = img.subsurface(320,320,64,64)
    imgGema = img.subsurface(128,384,64,64)
    Bloque4 = img.subsurface(256,0,64,64)

    #Cargamos la musica
    pygame.mixer.music.load("Musica.mp3")
    pygame.mixer.music.play(-1)

    #Cargamos los sonidos
    #sonidoGema = pygame.mixer.Sound("Gema.mp3")
    #sonidoMuerte = pygame.mixer.Sound("Muerte.mp3")

    #Creamos los grupos de sprites
    jugadores = pygame.sprite.Group()
    gemas = pygame.sprite.Group()
    escaleras = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    #Creamos los sprites
    jugadores.add(jugador)

    for i in range(mapHeight):
        for j in range(mapWidth):
            minum = matrizMap[i][j]
            if minum == 1 :
                b = Bloque([j*64,i*64],Bloque1)
                bloques.add(b)
            elif minum == 2 :
                b = Bloque([j*64,i*64],Bloque2)
                bloques.add(b)
            #elif minum == 63:
            #    b = Bloque([j*64,i*64],BloqueL)
            #    bloques.add(b)
            elif minum == 3 :
                b = Bloque([j*64,i*64],Bloque3)
                bloques.add(b)
            elif minum == 7 :
                b = Bloque([j*64,i*64],Caja)
                bloques.add(b)
            elif minum == 45 :
                e = Escalera([j*64,i*64],Escalera1,True)
                escaleras.add(e)
            elif minum == 46 :
                e = Escalera([j*64,i*64],Escalera2,True)
                escaleras.add(e)
            elif minum == 51 :
                g = Gema([j*64,i*64],imgGema)
                gemas.add(g)
            elif minum == 5 :
                b = Bloque([j*64,i*64],Bloque4)
                bloques.add(b)

    while not game_over:

        screen.fill((112, 145, 241))
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
                sys.exit()

        jugador.bajar = False
        jugador.escalar = False
        jugador.escalando = False
        jugador.bajando = False

        ls = pygame.sprite.spritecollide(jugador,escaleras,False)
        if len(ls) > 0 :
            jugador.escalar = True
        for e in ls:
            if e.bajar:
                jugador.bajar = True

        temp = jugador.evento(event)
        bloques.update(temp)
        escaleras.update(temp)
        gemas.update(temp)


        ls = pygame.sprite.spritecollide(jugador,escaleras,False)
        if len(ls) > 0 :
            jugador.escalar = True


        ls = pygame.sprite.spritecollide(jugador,bloques,False)
        for e in ls:
            if jugador.rect.top < e.rect.bottom and temp[1] < 0 and not jugador.escalando:
                temp = [0,(e.rect.bottom-jugador.rect.top)]
                bloques.update(temp)
                escaleras.update(temp)
                gemas.update(temp)
                jugador.contGravedad = 0
                break
            elif jugador.rect.bottom > e.rect.top and temp[1] > 0 and not jugador.bajando:
                temp = [0,(e.rect.top-jugador.rect.bottom)]
                jugador.contGravedad = 0
                bloques.update(temp)
                escaleras.update(temp)
                gemas.update(temp)
                break

        ls = pygame.sprite.spritecollide(jugador,bloques,False)
        for e in ls:
            if jugador.rect.right > e.rect.left and temp[0] > 0 :
                temp = [(e.rect.left-jugador.rect.right),0]
                bloques.update(temp)
                escaleras.update(temp)
                gemas.update(temp)
                break
            elif jugador.rect.left < e.rect.right and temp[0] < 0:
                temp = [(e.rect.right-jugador.rect.left),0]
                bloques.update(temp)
                escaleras.update(temp)
                gemas.update(temp)
                break

        ls = pygame.sprite.spritecollide(jugador,gemas,True)
        for e in ls:
            jugador.gemas += 1
            print(jugador.gemas)
        
        for b in bloques :
            screen.blit(b.image,b.rect)
        for e in escaleras :
            screen.blit(e.image,e.rect)
        for g in gemas :
            screen.blit(g.image,g.rect)
        screen.blit(jugador.imagen,jugador.rect)
        pygame.display.flip()