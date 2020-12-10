import pygame
from Constantes import *
import base64
import json
import csv
import gzip
from Jugador import *
from Comienzo import *
from Escalera import *
from Bloque import *
from Gema import *
from lim import *
from Turret import *
from Mina import *
import sys
from pygame.locals import *
from Explo import *
from Robot import *

width=100
height=720
black = (0,0,0)
blue = (0, 0, 180)
white = (255,255,255)
red = (180,0,0)
green = (0,180,0)
ANCHO = 1200
ALTO = 600

backgroundColor = (205,69,159)

redSelected = (255,0,0)
greenSelected = (0,255,0)
blueSelected = (0,0,255)

screen = pygame.display.set_mode((widht, height))

jewel = pygame.image.load("jewel.jpg")

def uploadMap(name):

    global mapWidth,mapHeight,tileHeight,tileWidth,matrizMap,mapname
    mapname = name
    matrizMap = []
    f = open(name+".json", "r")
    data = json.load(f)
    f.close()

    tileWidth=data["tilewidth"]
    tileHeight=data["tileheight"]

    mapWidth=data["width"]
    mapHeight=data["height"]

    for item in data["layers"]:
        mapa=item["data"]

    for i in range(0, len(mapa), mapWidth):
        matrizMap.append(mapa[i:i+mapWidth])

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

def juego(NumeroNivel):
    #pygame.quit()
    nivel = 1
    screen = pygame.display.set_mode((ANCHO, ALTO))
    Cinematica1()
    pygame.display.set_caption("sprite")
    reloj = pygame.time.Clock()
    game_over = False
    pygame.init()
    pygame.display.set_caption("Mapa")
    clock = pygame.time.Clock()
    img = pygame.image.load("juego.png")
    hoja = arrayTileset(img)
    fuente = pygame.font.Font(None,30)


    Caja = img.subsurface(384,0,64,64)
    Escalera1 = img.subsurface(256,320,64,64)
    Escalera2 = img.subsurface(320,320,64,64)
    imgGema = img.subsurface(128,384,64,64)
    Bloque4 = img.subsurface(256,0,64,64)
    Bloque1 = img.subsurface(0,0,64,64)
    Bloque2 = img.subsurface(64,0,64,64)
    Bloque3 = img.subsurface(128,0,64,64)

    imgNivel1 = pygame.image.load("Level1.png")
    imgNivel2 = pygame.image.load("Level2.png")
    imgNivel3 = pygame.image.load("Level3.png")

    imgGameOver = pygame.image.load("GameOver.png")
    imgWin = pygame.image.load("Win.png")

    sonidoGema = pygame.mixer.Sound("Gema.wav")
    sonidoMuerte = pygame.mixer.Sound("Muerte.wav")
    sonidoWin = pygame.mixer.Sound("victory.wav")
    sonidoLose = pygame.mixer.Sound("GameOver.wav")
    sonidoBala = pygame.mixer.Sound("bala.mp3")
    sonidoExplo = pygame.mixer.Sound("explo.wav")

    jugadores = pygame.sprite.Group()
    gemas = pygame.sprite.Group()
    escaleras = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    lim = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    turrets = pygame.sprite.Group()
    balas_enemies = pygame.sprite.Group()
    minas = pygame.sprite.Group()
    explos = pygame.sprite.Group()
    robots = pygame.sprite.Group()
    musica = 0
    tiempoInicial = pygame.time.get_ticks()
    perdio = False
    TiempoMaximo = 100

    while not game_over and nivel <= 3 :
        jugador = Jugador([ANCHO/2, ALTO/2])
        desplazamientoX = 0
        desplazamientoY = 0
        screen.fill([255,255,255])
    #------------------------------------------------------------------------------------------
        if nivel == 1:
            uploadMap("mapa1")
            musica = pygame.mixer.Sound("Musica1.wav")
            desplazamientoX = 100
            desplazamientoY = 1300
            info = imgNivel1.get_size()
            screen.blit(imgNivel1,[(ANCHO/2)-(info[0]/2),(ALTO/2)-(info[1]/2)])
            pygame.display.flip()
            pygame.time.wait(2000)
        if nivel == 2:
            uploadMap("jefe2")
            musica = pygame.mixer.Sound("Musica3.wav")
            desplazamientoX = -100
            desplazamientoY = 3630
            info = imgNivel3.get_size()
            screen.blit(imgNivel3,[(ANCHO/2)-(info[0]/2),(ALTO/2)-(info[1]/2)])
            pygame.display.flip()
            pygame.time.wait(2000)
        if nivel == 3:
            uploadMap("mapa2")
            musica = pygame.mixer.Sound("Musica2.wav")
            desplazamientoX = 100
            desplazamientoY = 1520
            info = imgNivel2.get_size()
            screen.blit(imgNivel2,[(ANCHO/2)-(info[0]/2),(ALTO/2)-(info[1]/2)])
            pygame.display.flip()
            pygame.time.wait(2000)
        if nivel == 4:
            uploadMap("jefe2")
            musica = pygame.mixer.Sound("Musica3.wav")
            desplazamientoX = -100
            desplazamientoY = 3630
            info = imgNivel3.get_size()
            screen.blit(imgNivel3,[(ANCHO/2)-(info[0]/2),(ALTO/2)-(info[1]/2)])
            pygame.display.flip()
            pygame.time.wait(2000)
    #---------------------------------------------------------------------------------------------

        musica.play(10)
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
                    e = Escalera([j*64,i*64],Escalera1,True)
                    escaleras.add(e)
                elif minum == 51 :
                    g = Gema([j*64,i*64],imgGema)
                    gemas.add(g)
                elif minum == 5 :
                    b = Bloque([j*64,i*64],Bloque4)
                    bloques.add(b)
                elif minum == 38:
                    m = Mina([j*64,i*64])
                    minas.add(m)
                elif minum == 39:
                    t = Turret([j*64,i*64])
                    turrets.add(t)
                elif minum == 40:
                    r = Robot([j*64,i*64],20)
                    robots.add(r)
                elif i==0 and j ==0:
                    l = LimClass(j*64,i*64)
                    lim.add(l)
                
        for t in turrets:
            bala = t.shoot()
            balas_enemies.add(bala)

        gemasTotales = len(gemas)

        temp1 = [desplazamientoX,desplazamientoY]

        bloques.update(temp1)
        escaleras.update(temp1)
        gemas.update(temp1) 
        lim.update(temp1)
        balas.update(temp1)
        turrets.update(temp1,jugador.rect.x)
        balas_enemies.update(temp1)
        minas.update(temp1)
        explos.update(temp1)
        robots.update(temp1)

        tiempoInicioNivel = pygame.time.get_ticks() - tiempoInicial
        cont = 0
        while not game_over:
            cont += 1
            screen.fill((112, 145, 241))
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sonidoBala.play()
                        bala = jugador.shoot()
                        balas.add(bala)
                    if event.key == pygame.K_ESCAPE:
                        gemas.empty()
            
            for t in turrets:
                if cont % 25 == 0:
                    bala = t.shoot()
                    balas_enemies.add(bala)

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
            desplazamientoX -= temp[0]
            desplazamientoY -= temp[1]
            bloques.update(temp)
            escaleras.update(temp)
            gemas.update(temp)
            lim.update(temp)
            balas.update(temp)
            turrets.update(temp,jugador.rect.x)
            balas_enemies.update(temp)
            minas.update(temp)
            explos.update(temp)
            robots.update(temp)

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
                    lim.update(temp)
                    balas.update(temp)
                    turrets.update(temp,jugador.rect.x)
                    balas_enemies.update(temp)
                    minas.update(temp)
                    explos.update(temp)
                    robots.update(temp)
                    jugador.contGravedad = 0
                    break
                if jugador.rect.bottom > e.rect.top and temp[1] > 0 and not jugador.bajando:
                    temp = [0,(e.rect.top-jugador.rect.bottom)]
                    jugador.contGravedad = 0
                    bloques.update(temp)
                    escaleras.update(temp)
                    gemas.update(temp)
                    lim.update(temp)
                    balas.update(temp)
                    turrets.update(temp,jugador.rect.x)
                    balas_enemies.update(temp)
                    minas.update(temp)
                    explos.update(temp)
                    robots.update(temp)
                    jugador.salto = False
                    break
            
            ls = pygame.sprite.spritecollide(jugador,bloques,False)
            for e in ls:
                if jugador.rect.right > e.rect.left and temp[0] > 0 :
                    temp = [(e.rect.left-jugador.rect.right),0]
                    bloques.update(temp)
                    escaleras.update(temp)
                    gemas.update(temp)
                    lim.update(temp)
                    balas.update(temp)
                    turrets.update(temp,jugador.rect.x)
                    balas_enemies.update(temp)
                    minas.update(temp)
                    explos.update(temp)
                    robots.update(temp)
                    break
                elif jugador.rect.left < e.rect.right and temp[0] < 0:
                    temp = [(e.rect.right-jugador.rect.left),0]
                    bloques.update(temp)
                    escaleras.update(temp)
                    gemas.update(temp)
                    lim.update(temp)
                    balas.update(temp)
                    turrets.update(temp,jugador.rect.x)
                    balas_enemies.update(temp)
                    minas.update(temp)
                    explos.update(temp)
                    robots.update(temp)
                    break
            
            for b in bloques:
                ls = pygame.sprite.spritecollide(b,balas,True)

            for b in balas:
                if b.rect.x < 0 or b.rect.x > 1200:
                    balas.remove(b)

            for b in balas_enemies:
                if b.rect.x < 0 or b.rect.x > 1200:
                    balas_enemies.remove(b)

            ls = pygame.sprite.spritecollide(jugador,balas_enemies,True)
            for b in ls:
                jugador.health -= 10
            
            totalGemas = 0

            ls = pygame.sprite.spritecollide(jugador,gemas,True)
            for e in ls:
                jugador.gemas += 1
                totalGemas = jugador.gemas
                print("Jewels:", totalGemas)
                TiempoMaximo += 15
                sonidoGema.play()

            for t in turrets:
                ls = pygame.sprite.spritecollide(t,balas,True)
                if ls:
                    sonidoExplo.play()
                    explo = Explo([t.rect.x-70,t.rect.y-70])
                    explos.add(explo)
                    turrets.remove(t)

            ls = pygame.sprite.spritecollide(jugador,minas,True)
            for m in ls:
                jugador.health -= 30
                sonidoExplo.play()
                explo = Explo([jugador.rect.x,jugador.rect.y])
                explos.add(explo)
                    
            for b in bloques :
                screen.blit(b.image,b.rect)
            for e in escaleras :
                screen.blit(e.image,e.rect)
            for g in gemas :
                screen.blit(g.image,g.rect)
            for b in balas:
                screen.blit(b.image,b.rect)
            for t in turrets:
                screen.blit(t.image,t.rect)
            for b in balas_enemies:
                screen.blit(b.image,b.rect)
            for m in minas:
                screen.blit(m.image,m.rect)
            for e in explos:
                screen.blit(e.image,e.rect)
            for r in robots:
                screen.blit(r.image,r.rect)

            for e in explos:
                if e.terminar == True:
                    explos.remove(e)

            screen.blit(jugador.imagen,jugador.rect)
            jugador.healthbar(screen)
            pygame.draw.rect(screen,white,(1000,3,200,50))
            pygame.draw.rect(screen,blueSelected,(1000,3,200,50),3)
            string = "                " +str(jugador.gemas) + "/" + str(gemasTotales)
            info = fuente.render(string,10,(0,0,0))
            screen.blit(info,[950,20])
            screen.blit(imgGema,[990,-10])
            string2 = "Time : " + str(int(TiempoMaximo - ((pygame.time.get_ticks() - tiempoInicioNivel)/1000)))
            info2 = fuente.render(string2,10,(0,0,0))
            screen.blit(info2,[1100,20])
            pygame.display.flip()
    #----------------------------------------------------------------------------------------
            if (TiempoMaximo - ((pygame.time.get_ticks() - tiempoInicioNivel)/1000)) <= 0:
                game_over = True
                perdio = True
                musica.stop()
                sonidoMuerte.play()
                pygame.time.wait(1500)

            if l.y <-2000:
                game_over = True
                perdio = True
                musica.stop()
                sonidoMuerte.play()
                pygame.time.wait(100)

            if jugador.health <= 0:
                game_over = True
                perdio = True
                musica.stop()
                sonidoMuerte.play()
                pygame.time.wait(100)

            if(len(gemas)==0):
                nivel+=1
                print("Mapa numero:", nivel)
                jugadores.empty()
                print(jugadores)
                bloques.empty()
                escaleras.empty()
                gemas.empty()
                enemigos.empty()
                lim.empty()
                balas.empty()
                turrets.empty()
                musica.stop()
                balas_enemies.empty()
                minas.empty()
                explos.empty()
                robots.empty()
                break

    #----------------------------------------------------------------------------------------
    screen.fill([255,255,255])
    if perdio :
        sonidoLose.play()
        info = imgGameOver.get_size()
        screen.blit(imgGameOver,[(ANCHO/2)-(info[0]/2),(ALTO/2)-(info[1]/2)])
        print(sonidoLose.get_volume())
    else:
        sonidoWin.play()
        info = imgWin.get_size()
        screen.blit(imgWin,[(ANCHO/2)-(info[0]/2),(ALTO/2)-(info[1]/2)])
    pygame.display.flip()
    cerrado = False
    while not cerrado:
        for event in pygame.event.get():
            if event.type == QUIT:
                cerrado = True
                sys.exit()
