import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
        a class to manage the Bullet from the ship
    """
    def __init__(self, ai_settings, screen, ship):
        """
            inherit the Sprite
        """
        super().__init__()
        #locate the screen
        self.screen = screen
        #create the bullet Rectangor
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        #set the bullet in ship
        self.rect.centerx = ship.rect.centerx
        #set the bullet on the top of the ship
        self.rect.top = ship.rect.top
        #store the y location of the bullet
        self.y = float(self.rect.y)
        #get the cloar parameter and speed_factor parameter
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.speed_factor

    def update(self):
        """
            upate data the bullet's y location
        """
        self.rect.y -= self.speed_factor
        self.y = float(self.rect.y)

    def draw_bullet(self):
        """
            draw the bullet on the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)

