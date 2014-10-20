#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Modulos
import sys, pygame, random
from pygame.locals import *
from pygame.examples.mask import Sprite
from pygame import sprite
from __builtin__ import str
# variables
score=0
vidas=10
# Constantes
WIDTH = 640
HEIGHT = 480
COLOR_LASER = (225,0,0)
# Clases
# ---------------------------------------------------------------------
class NavePanel(pygame.sprite.Sprite): 
    def __init__(self, x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image,True)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
    def disparar(self,superficie,mouse):  
        if mouse==(1,0,0): #se haga clik dibujar 2 lineas saliendo desde los extremos inferiores hasta la mira
            laser=pygame.mixer.Sound("data/LASER1.WAV")
            laser.play()
            pygame.draw.line(superficie,COLOR_LASER,(0,HEIGHT),pygame.mouse.get_pos(),4)
            pygame.draw.line(superficie,COLOR_LASER,(WIDTH,HEIGHT),pygame.mouse.get_pos(),4)   
            return True 
        else:
            return False      
    def update(self, superficie):
        superficie.blit(self.image,self.rect) 
class Mira(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image,True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y 
    def mover(self, posxy):
        self.rect.centerx,self.rect.centery=(posxy)            
    def update(self,superfice):
        superfice.blit(self.image,self.rect)
class Asteriode(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("data/asteroide.png",True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 0.1
    def mover(self,time):
        self.rect.centery += self.speed *time
        self.rect.move_ip(0,1)
    def update(self,superficie):
        superficie.blit(self.image,self.rect)      
class ListaAsteorides(): #crea un arreglo de asteroides y los mueve y actualia
    def __init__(self,numeroIni):
        AstroWidh=Asteriode(0,0).rect.width
        self.list=[]
        numerosxy=[]#arreglo de posiciones
        while (len(numerosxy) < numeroIni):
            numerox= random.randint(AstroWidh,WIDTH-AstroWidh)
            numeroy= random.randint(numeroIni*-60*3,-5)
            numeroxy=(numerox ,numeroy)
            if not numeroxy in numerosxy:
                numerosxy.append((numerox,numeroy))#retorna un arreglo de tuplas aletorias si que se repitan en un espacio determinado
        for x in range(numeroIni):
            xr,yr = numerosxy[x]
            self.list.append(Asteriode(xr,yr))
    def mover(self,time):
        for asteriodes in self.list: #por cada asteroidede la lista llamar la funcion mover
            asteriodes.mover(time)
            if asteriodes.rect.centery >= (HEIGHT): #si esta por debajo del mapo se borra
                self.list.remove(asteriodes)
                global vidas
                vidas-=1
                print vidas  
    def update(self,screen):
        for asteroides in self.list:
            asteroides.update(screen)
    def listExis(self):
        if self.list.__len__() ==0:
            return True
        else:
            return False
    def destruir(self):
        for asteriodes in self.list:
            x,y=pygame.mouse.get_pos()
            if ((x<asteriodes.rect.right and x>asteriodes.rect.left)and(y<asteriodes.rect.bottom and y>asteriodes.rect.top)):
                self.list.remove(asteriodes)
                global score
                score+=1

     
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
    #iniciar variales
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    ##astro = Asteriode(100,100)
    pygame.display.set_caption("Viaje a la Galxia Negra")
    pygame.mouse.set_visible(False)
    mira = Mira(0,0,"data/mira.png")
    navePanel = NavePanel(0,HEIGHT-60,"data/navePanel.png")    
    fuenteDig=pygame.font.Font("data/fuenteDigital.TTF",20)#ds digital datafont.com
    fuenteEnd=pygame.font.Font(None,80)
    fondo = pygame.image.load("data/Space.jpg")#flick
    clock = pygame.time.Clock()
    astro = ListaAsteorides(vidas+90)
    while True:        
            time = clock.tick(60)
            screen.blit(fondo,(0,0))                 
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                    sys.exit(0)             
                if eventos.type == MOUSEBUTTONDOWN:
                    if navePanel.disparar(screen, pygame.mouse.get_pressed()):
                        astro.destruir() 
            #UPDATES/DIBIJAR
            astro.mover(time)
            astro.update(screen)
            mira.mover(pygame.mouse.get_pos())
            mira.update(screen)            
            navePanel.update(screen)
            global score
            textoScore=fuenteDig.render(str(score),0,(0,225,0))
            textoVidas=fuenteDig.render(str(vidas),0,(225,0,0))
            screen.blit(textoScore,(400,HEIGHT-35))
            screen.blit(textoVidas,(200,HEIGHT-35))         
            pygame.display.update()
            #fin del juego
            if vidas <=0 or astro.listExis():
                fuenteEnd=pygame.font.Font("data/fuenteDigital.TTF",80)
                pygame.mouse.set_visible(True)
                while True:
                    screen.blit(fondo,(0,0))
                    msj=""
                    if vidas <=0:
                        msj="Has perdido"
                    elif astro.listExis():
                        msj="has ganado"
                    textoEnd=fuenteEnd.render(msj,0,(0,225,0))
                    screen.blit(textoEnd,( (WIDTH/2)-fuenteEnd.get_height() ,(HEIGHT/2)-fuenteEnd.get_height() ) )
                    for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                            pygame.quit()
                            sys.exit()
                    pygame.display.update()           
    return 0       
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()