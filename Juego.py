#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Modulos
import sys, pygame, random
from pygame.locals import *
from Sprites import Sprites
from pygame.examples.mask import Sprite
from pygame import sprite
from __builtin__ import str
# variables
score=0
nivel=1
vidas=100
# Constantes
WIDTH = 640
HEIGHT = 480
# Clases
# ---------------------------------------------------------------------

class Mira(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image,True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y 
    def update(self,superfice):
        self.rect.centerx,self.rect.centery=(pygame.mouse.get_pos())               
        superfice.blit(self.image,self.rect)
class Asteriode(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("data/asteroide.png",True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y        
    def update(self,screen):
        self.rect.move_ip(0,1)
        screen.blit(self.image,self.rect)      
class waveAsteorides(): #crea un arreglo de asteroides y los mueve y actualia
    def __init__(self):       
        self.AstroWidh=Asteriode(0,0).rect.width
        self.wave=[]
        self.numWavesDestroy=0
    def cwave(self):     
        global nivel
        nivel = round(self.numWavesDestroy/10)+1#nivel aumenta cada 10 oleadeas(WAVEs) destruidos por uno mismo
        astMin,astMax=({1:(2,6), 2:(3,7), 3:(4,8),4:(0,0)}[nivel])#ajusta el  minimo y maximo de asteorides de la oleada por cada nivel
        if len(self.wave)==0:
            self.isdestroymy=False
            num=random.randint(astMin,astMax)
            while(len(self.wave)<num):
                numerox= random.randint(0,WIDTH)
                numeroy= random.randint(-3*self.AstroWidh,-self.AstroWidh)
                self.wave.append(Asteriode(numerox,numeroy))
            return self.wave
    def update(self,screen):
        for asteriodes in self.wave: #por cada asteroidede la wave llamar la funcion mover
            asteriodes.update(screen)
            if asteriodes.rect.centery >= (HEIGHT): #si esta por debajo del mapo se borra
                self.wave.remove(asteriodes)
                global vidas
                vidas-=1  
        if len(self.wave)==0 and self.isdestroymy:
                    self.numWavesDestroy+=1
                    print "primera oleada destruida"
        for asteroides in self.wave:
            asteroides.update(screen)
    def destruir(self):         
        for asteriodes in self.wave:           
            x,y=pygame.mouse.get_pos()
            if ((x<asteriodes.rect.right and x>asteriodes.rect.left)and(y<asteriodes.rect.bottom and y>asteriodes.rect.top)):
                self.wave.remove(asteriodes)
                global score
                score+=1                
                print self.isdestroymy
                if self.isdestroymy==False:
                    self.isdestroymy=True
                    print "fue destruido el primero"              
# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
# ---------------------------------------------------------------------
 
def main():
    #iniciar variables
    playing=True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Viaje a la Galxia Negra")
    pygame.mouse.set_visible(False)
    mira = Mira(0,0,"data/mira.png")
    astro = waveAsteorides() 
    navePanel = Sprites.Nave("data/navePanel.png")   
    fuenteDig=pygame.font.Font("data/fuenteDigital.TTF",20)#ds digital datafont.com
    fondo = pygame.image.load("data/Space.jpg")#flick
    clock = pygame.time.Clock()
    while playing:   
            time = clock.tick(60)
            screen.blit(fondo,(0,0))
            astro.cwave()                 
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                    playing=False           
                if eventos.type == MOUSEBUTTONDOWN:
                    navePanel.disparar(screen, astro)                 
            #UPDATES/DIBIJAR
            astro.update(screen)
            mira.update(screen)            
            navePanel.updated(screen)
            global score
            textoScore=fuenteDig.render(str(score),0,(0,225,0))
            textoVidas=fuenteDig.render(str(vidas),0,(225,0,0))
            screen.blit(textoScore,(400,HEIGHT-35))
            screen.blit(textoVidas,(200,HEIGHT-35))         
            pygame.display.update()
            #fin del juego
            if vidas <=0 or nivel>=4:
                gameover=True
                while gameover:
                    for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                            playing=gameover=False 
                    pygame.mouse.set_visible(True)
                    screen.blit(fondo,(0,0))
                    if vidas <=0:
                        msj="Has perdido"
                    else:
                        msj="has ganado"
                    textoEnd=fuenteDig.render(msj,0,(0,225,0))
                    screen.blit(textoEnd,( (WIDTH/2)-fuenteDig.get_height() ,(HEIGHT/2)-fuenteDig.get_height() ) )               
                    pygame.display.update()
    pygame.quit()
    sys.exit()                
    return 0
if __name__ == '__main__':
    pygame.init()
    main()