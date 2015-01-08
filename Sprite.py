import pygame
from pygame.examples.mask import Sprite

class Sprite(pygame.sprite.Sprite):
    pass
    def update(self,screen):
        screen.blit(self.image,self.rect)
        
