import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('../Src/ic_rain_drop.png')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += 5
        self.rect.x = self.x
        self.rect.y = self.y
    
        
        
pygame.init()
screen = pygame.display.set_mode()
image = pygame.image.load('../Src/ic_rain_drop.png')
rain_rect = image.get_rect()
pygame.display.set_caption("rain")
rains = Group()
rain = Rain(screen)
screen_rect = screen.get_rect()
available_x = screen_rect.width - 2*rain_rect.width
for i in range(int(available_x/rain_rect.width)):
    rain = Rain(screen)
    rain.x = rain_rect.width + i*rain_rect.width
    rains.add(rain)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for rain in rains.copy():
        # print(str(rain.rect.y)+ '   '+str(rain.screen_rect.bottom))
        if rain.rect.y >= rain.screen_rect.bottom:
            rains.empty()
            break
    print(len(rains))
    if len(rains) == 0:
        for i in range(int(available_x/rain_rect.width)):
            rain_1 = Rain(screen)
            rain_1.x = rain_rect.width + i*rain_rect.width
            rains.add(rain_1)
    for rain in rains.sprites():
        rain.update()
    screen.fill((240, 248, 255))
    rains.draw(screen)
    # flip recent changes on the screen
    pygame.display.flip()