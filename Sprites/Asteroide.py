import pygame,Sprites,random,utils
from utils import Vars
from utils import Constans
class Asteriode(Sprites.Sprite):
    def __init__(self, x,y):
        super(Asteriode, self).__init__("data/asteroide.png")
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
        Vars.nivel = round(self.numWavesDestroy/10)+1#nivel aumenta cada 10 oleadeas(WAVEs) destruidos por uno mismo
        astMin,astMax=({1:(2,6), 2:(3,7), 3:(4,8),4:(0,0)}[Vars.nivel])#ajusta el  minimo y maximo de asteorides de la oleada por cada nivel
        if len(self.wave)==0:
            self.isdestroymy=False
            num=random.randint(astMin,astMax)
            while(len(self.wave)<num):
                numerox= random.randint(0,Constans.WIDTH)
                numeroy= random.randint(-3*self.AstroWidh,-self.AstroWidh)
                self.wave.append(Asteriode(numerox,numeroy))
            return self.wave
    def update(self,screen):
        for asteriodes in self.wave: #por cada asteroidede la wave llamar la funcion mover
            asteriodes.update(screen)
            if asteriodes.rect.centery >= (Constans.HEIGHT): #si esta por debajo del mapo se borra
                self.wave.remove(asteriodes)
                Vars.vidas-=1  
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
                Vars.score+=1              
                print self.isdestroymy
                if self.isdestroymy==False:
                    self.isdestroymy=True
                    print "fue destruido el primero"   