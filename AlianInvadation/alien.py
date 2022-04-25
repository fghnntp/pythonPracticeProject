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
        # init alien's super
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        image_addr = 'Src/alien-' + str(random.randint(1, 8)) + '.png'
        # load the image
        self.image = pygame.image.load(image_addr)
        # get the rect of the image
        self.rect = self.image.get_rect()
        # set the alien in right place
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_y_z = 100
        
    
    def blitme(self):
        """
        blit the image on the screen
        """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """
        if the aliens touch the screen return True
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or \
           self.rect.left <= screen_rect.left:
           return True
    
    def update(self):
        """
        update the aliens on the screen
        """
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x
        self.rect.y = self.y