import sys
import pygame
from bullet import Bullet

def check_event(ai_settings, screen, ship, bullets):
    """
        check the key event, class by the keydown and key up
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
            
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
        response the key down
    """
    if event.key == pygame.K_RIGHT:
        ship.m_right = True
    if event.key == pygame.K_LEFT:
        ship.m_left = True
    if event.key == pygame.K_UP:
        ship.m_up = True
    if event.key == pygame.K_DOWN:
        ship.m_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """
        response the key up
    """
    if event.key == pygame.K_RIGHT:
        ship.m_right = False
    if event.key == pygame.K_LEFT:
        ship.m_left = False
    if event.key == pygame.K_UP:
        ship.m_up = False
    if event.key == pygame.K_DOWN:
        ship.m_down = False

def update_screen(ai_settings, screen, ship, bullets):
    """
        update the screen
    """
    #填充背景色
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    #刷新飞船
    ship.blitme()
    #刷新界面
    pygame.display.flip()

def update_bullets(bullets):
    """
        update the disapeared bullet
    """
    #update the bullets
    bullets.update()
    #use the copy for not to change the iterable object
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """
        add new bullet in a bullets Group to fire in case
    """
    if len(bullets) < ai_settings.bullet_allowd:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
