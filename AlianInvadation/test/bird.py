import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite

class Bird(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('../Src/BIRD.png')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.x = float(self.screen_rect.centerx)
        self.y = float(self.screen_rect.centery)
        self.u_move = False
        self.d_move = False
        self.l_move = False
        self.r_move = False

    def update(self):
        if self.u_move:
            self.y -= 2
        if self.d_move:
            self.y += 2
        if self.l_move:
            self.x -= 2
        if self.r_move:
            self.x += 2
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption("bird")
bird = Bird(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird.u_move = True
            if event.key == pygame.K_DOWN:
                bird.d_move = True
            if event.key == pygame.K_LEFT:
                bird.l_move = True
            if event.key == pygame.K_RIGHT:
                bird.r_move = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                bird.u_move = False
            if event.key == pygame.K_DOWN:
                bird.d_move = False
            if event.key == pygame.K_LEFT:
                bird.l_move = False
            if event.key == pygame.K_RIGHT:
                bird.r_move = False
    bird.update()
    screen.fill((240, 248, 255))
    bird.blitme()
    # flip recent changes on the screen
    pygame.display.flip()