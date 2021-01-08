import sys
import pygame
from bullet import Bullet
from alien import Alien

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
    if event.key == pygame.K_q:
        sys.exit()

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

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """
    update the bullets and ship
    """
    # 填充背景色
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    # 刷新飞船
    ship.blitme()
    # 刷新外星人
    aliens.draw(screen)
    # 刷新界面
    pygame.display.flip()

def update_bullets(bullets):
    """
    rm the disapeared bullet
    """
    # update the bullets
    bullets.update()
    # use the copy for not to change the iterable object
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

def create_fleet(ai_settings, screen, aliens):
    """
    create a aliens fleet in half of the front screen
    """
    alien = Alien(ai_settings ,screen)
    # get the aliens num in one row
    alien_width = alien.rect.width
    availabe_space_x = ai_settings.screen_width - 2*alien_width
    aliens_num = int(availabe_space_x / (2*alien_width))
    # get the aliens rows in half of the screen
    availabe_space_y = ai_settings.screen_height / 2
    alien_height = alien.rect.height
    aliens_row = int(availabe_space_y / (1.5*alien_height))
    # create alien's fleet
    for column in range(aliens_row):
        for alien_num in range(aliens_num):
            alien = Alien(ai_settings, screen)
            alien.x = 2*alien_num*alien_width + alien_width
            alien.rect.x = alien.x
            alien.y = 1.5*column*alien_height + 0.5*alien_height
            alien.rect.y = alien.y
            aliens.add(alien)

def check_fleet_direction(ai_settings, aliens):
    """
    check the fleet direction
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """
    change the fleet dirction and drop down fleet in pre_setting num
    """
    for alien in aliens.sprites():
        alien.y += ai_settings.alien_drop_speed
    ai_settings.fleet_direction *= -1
    

def update_aliens(aliens):
    """
    update the aliens
    """
    aliens.update()