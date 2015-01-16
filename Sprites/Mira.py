import pygame,utils,Sprites
from utils import Constans
from pygame.locals import *
from pygame.examples.mask import Sprite
from pygame import sprite
from pygame.examples.mask import Sprite
class Mira(Sprites.Sprite): 
    def __init__(self,image):
        super(Mira, self).__init__(image)
        self.rect.left = 0
        self.rect.top = Constans.HEIGHT-60
    def update(self,superfice):
        self.rect.centerx,self.rect.centery=(pygame.mouse.get_pos())               
        superfice.blit(self.image,self.rect) 