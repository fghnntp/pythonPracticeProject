import sys
import pygame
import json
from bullet import Bullet
from alien import Alien
from time import sleep

def read_config(stats):
    """
    read the config and set them
    """
    with open('config.json', 'r') as f_obj:
        settings = json.loads(f_obj.read())
        stats.high_score = settings["high_score"]

def check_event(ai_settings, screen, stats, sb, play_button, aliens,
                ship, bullets):
    """
    check the key event, class by the keydown and key up
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_out(stats)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship,
                                 aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)
    
def check_keydown_events(event, ai_settings, screen, stats, sb, ship,
                         aliens, bullets):
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
        game_out(stats)
    if event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

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

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """
    creating a new game when player trigger the play button
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets):
    """
    check if hte bullet and aliens collided
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        # level up
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    restart the game
    """
    # hiden the cursor
    pygame.mouse.set_visible(False)
    # reset the game statistic info
    stats.reset_stats()
    stats.game_active = True
    # clear aliens list and bullets list
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    aliens.empty()
    bullets.empty()
    # create aliens and reset the ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens,
                  bullets, play_button):
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
    # show scorebord
    sb.show_score()
    # if game is not active, show play button
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    rm the disapeared bullet
    """
    # update the bullets
    bullets.update()
    # use the copy for not to change the iterable object
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets)
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """
    add new bullet in a bullets Group to fire in case
    """
    if len(bullets) < ai_settings.bullet_allowd:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
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

def check_fleet_edges(ai_settings, aliens):
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

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """
    response ship collied by alens
    """
    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.prep_ships()
        # clear the aliens and bullets
        aliens.empty()
        bullets.empty()
        ship.center_ship()
        # create aliens and reset the ship
        create_fleet(ai_settings, screen, ship, aliens)
        # pause the game
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """
    check if the aliens have reached the screen bottom
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break
    
def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """
    update the aliens
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
    # check if the aliens have reached the screen bottom
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    """
    check if a higer score have born
    """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def game_out(stats):
    """
    save the higest score when the game out
    """
    settings = {"high_score": stats.high_score}
    with open('config.json', 'w') as f_obj:
        f_obj.write(json.dumps(settings))
    sys.exit()
        