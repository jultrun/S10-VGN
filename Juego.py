#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Modulos
import sys, pygame,utils.Vars,utils.Constans,Sprites.Mira,Sprites.Nave,Sprites.Asteroide
from pygame.locals import *
from __builtin__ import str          
def main():
    #iniciar variables
    playing=True
    screen = pygame.display.set_mode((utils.Constans.WIDTH, utils.Constans.HEIGHT))
    pygame.display.set_caption("Viaje a la Galxia Negra")
    pygame.mouse.set_visible(False)
    mira = Sprites.Mira.Mira("data/mira.png")  
    astro = Sprites.Asteroide.waveAsteorides() 
    navePanel = Sprites.Nave.Nave("data/navePanel.png")   
    fuenteDig=pygame.font.Font("data/fuenteDigital.TTF",20)#ds digital datafont.com
    fondo = pygame.image.load("data/Space.jpg")#flick
    clock = pygame.time.Clock()
    while playing:   
            clock.tick(60)            
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
            textoScore=fuenteDig.render(str(utils.Vars.score),0,(0,225,0))
            textoVidas=fuenteDig.render(str(utils.Vars.vidas),0,(225,0,0))
            screen.blit(textoScore,(400,utils.Constans.HEIGHT-35))
            screen.blit(textoVidas,(200,utils.Constans.HEIGHT-35))         
            pygame.display.update()
            #fin del juego
            if utils.Vars.vidas <=0 or utils.Vars.nivel>=4:
                gameover=True
                while gameover:
                    for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                            playing=gameover=False 
                    pygame.mouse.set_visible(True)
                    screen.blit(fondo,(0,0))
                    if utils.Vars.vidas <=0:
                        msj="Has perdido"
                    else:
                        msj="has ganado"
                    textoEnd=fuenteDig.render(msj,0,(0,225,0))
                    screen.blit(textoEnd,( (utils.Constans.WIDTH/2)-fuenteDig.get_height() ,(utils.Constans.HEIGHT/2)-fuenteDig.get_height() ) )               
                    pygame.display.update()
    pygame.quit()
    sys.exit()                
    return 0
if __name__ == '__main__':
    pygame.init()
    main()