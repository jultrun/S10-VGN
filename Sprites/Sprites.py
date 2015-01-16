import pygame,utils.Funtions
class Sprite(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = utils.Funtions.load_image(image,True)
        self.rect = self.image.get_rect()
    def updated(self,screen):
        screen.blit(self.image,self.rect)