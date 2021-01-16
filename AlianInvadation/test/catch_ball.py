import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint

class Warroir(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('../Src/warrior.png')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.x = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.l_move = False
        self.r_move = False

    def update(self):
        if self.l_move and self.rect.left >= self.screen_rect.left:
            self.x -= 2
        if self.r_move and self.rect.right <= self.screen_rect.right:
            self.x += 2
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Ball(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('../Src/ball.png')
        self.rect = self.image.get_rect()
        self.aviliable_space = self.screen_rect.width - self.rect.width
        self.rect.top = self.screen_rect.top
        self.rect.x = randint(0, self.aviliable_space)
        self.y = float(self.rect.y)
        self.uncatched_times = 0

    def reset_ball(self, flag=False):
        if self.rect.y >= self.screen_rect.bottom:
            self.uncatched_times += 1
        if self.rect.y >= self.screen_rect.bottom or flag:
            self.y = 0.0
            self.rect.x = randint(0, self.aviliable_space)
            self.rect.top = self.screen_rect.top
        
    def update(self):
        self.reset_ball()
        self.y += 2
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen_rect = screen.get_rect()
pygame.display.set_caption("warroir")
warroir = Warroir(screen)
ball = Ball(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                warroir.l_move = True
            elif event.key == pygame.K_RIGHT:
                warroir.r_move = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                warroir.l_move = False
            elif event.key == pygame.K_RIGHT:
                warroir.r_move = False
    if ball.uncatched_times < 3:
        warroir.update()
        ball.update()
        result = pygame.sprite.collide_rect(warroir, ball)
        ball.reset_ball(flag=result)
    screen.fill((240, 248, 255))
    warroir.blitme()
    ball.blitme()
    # flip recent changes on the screen
    pygame.display.flip()