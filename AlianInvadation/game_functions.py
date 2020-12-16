import sys
import pygame

def check_event():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def update_sccreen(ai_settings, screen, ship, cat):
    #填充背景色
    screen.fill(ai_settings.bg_color)
    #刷新飞船
    ship.blitme()
    cat.blitme()
    #刷新界面
    pygame.display.flip()