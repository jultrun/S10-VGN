import pygame,utils
from utils import Constans
from pygame.locals import *
from pygame.examples.mask import Sprite
from pygame import sprite
from pygame.examples.mask import Sprite


class Sprite(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image,True)
        self.rect = self.image.get_rect()
    def updated(self,screen):
        screen.blit(self.image,self.rect)
        
class Nave(Sprite): 
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
        
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
    
    