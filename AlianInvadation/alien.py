import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    """
        a alien class to built some enemies
    """
    def __init__(self, ai_settings, screen):
        """
            init the alien
        """
        #init alien's super
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        image_addr = 'Src/alien-' + str(random.randint(1, 5)) + '.png'
        #load the image
        self.image = pygame.image.load(image_addr)
        #get the rect of the image
        self.rect = self.image.get_rect()
        #set the alien in right place
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)