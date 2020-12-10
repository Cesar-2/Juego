import pygame
from Constantes import *
import base64
import json
import csv
import gzip
from Jugador import *
from Escalera import *
from Bloque import *
from Gema import *
from Nivel1 import *
from Bala import *

intro = True


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def game_intro():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        imagen = pygame.image.load(os.path.join("IMG","menu1.png"))
        screen.blit(imagen,(0,0))
        NumeroNivel = 1
        button("Play",290/2 - 60 ,464/2, 125,60, green, greenSelected, NumeroNivel, juego)
        button("Tutorial",290/2 - 60 ,464/2 + 65, 125,60, blue, blueSelected, 0, tutorial)
        button("Quit",290/2 - 60 ,464/2 + 130,125,60, red, redSelected ,NumeroNivel, quitgame)

        pygame.display.update()

def tutorial(NumeroNivel):

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen = pygame.display.set_mode((1200, 600))
        tuto = pygame.image.load(os.path.join("IMG","Tutorial.png"))
        screen.blit(tuto,(0,0))
        button("Start",1000 ,400, 125,60, green, greenSelected,1, juego)
        pygame.display.update()

def quitgame():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,mapa,action=None):

    global intro

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action(mapa)
            intro = False
            return
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

game_intro()
