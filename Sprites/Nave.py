import pygame,utils,Sprites
from utils import Constans
class Nave(Sprites.Sprite): 
    def __init__(self,image):
        super(Nave, self).__init__(image)
        self.rect.left = 0
        self.rect.top = Constans.HEIGHT-60
    def disparar(self,superficie,objetivo):      
        pygame.draw.line(superficie,(225,0,0),(0,Constans.HEIGHT),pygame.mouse.get_pos(),4)
        pygame.draw.line(superficie,(225,0,0),(Constans.WIDTH,Constans.HEIGHT),pygame.mouse.get_pos(),4)  
        laser=pygame.mixer.Sound("data/LASER1.WAV")
        laser.play() 
        objetivo.destruir()
        #objetivo.rotates()