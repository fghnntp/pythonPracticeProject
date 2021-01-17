import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button


def run_game():
    """
    初始化当前窗口和游戏模块
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                      ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, "Play")
    pygame.mouse.set_visible(False)
    ship = Ship(screen, ai_settings)
    aliens = Group()
    bullets = Group()
    stats = GameStats(ai_settings)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    while True:
        # 循环检查事件
        gf.check_event(ai_settings, screen, stats, play_button, aliens,
                       ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens,
                         bullets, play_button)
        
if __name__ == "__main__":
    run_game()