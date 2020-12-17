import sys
import pygame

def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_down_func(event, ship)
        if event.type == pygame.KEYUP:
            key_up_func(event, ship)
            

def key_down_func(event, ship):
    """
        响应按键按下
    """
    if event.key == pygame.K_RIGHT:
        ship.m_right = True
    if event.key == pygame.K_LEFT:
        ship.m_left = True
    if event.key == pygame.K_UP:
        ship.m_up = True
    if event.key == pygame.K_DOWN:
        ship.m_down = True

def key_up_func(event, ship):
    """
        响应按键抬起
    """
    if event.key == pygame.K_RIGHT:
        ship.m_right = False
    if event.key == pygame.K_LEFT:
        ship.m_left = False
    if event.key == pygame.K_UP:
        ship.m_up = False
    if event.key == pygame.K_DOWN:
        ship.m_down = False

def update_sccreen(ai_settings, screen, ship):
    #填充背景色
    screen.fill(ai_settings.bg_color)
    #刷新飞船
    ship.blitme()
    #刷新界面
    pygame.display.flip()