import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('../Src/Star large.png')
        self.rect = self.image.get_rect()
        x = randint(0, int(self.screen_rect.width/self.rect.width)-1)
        y = randint(0, int(self.screen_rect.height/self.rect.height)-1)
        self.rect.x = x*self.rect.width
        self.rect.y = y*self.rect.height
        
pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption("stars")
stars = Group()
for i in range(5):
    for j in range(5):
        star = Star(screen)
        stars.add(star)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((240, 248, 255))
    stars.draw(screen)
    # flip recent changes on the screen
    pygame.display.flip()