import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """
        初始化当前窗口和游戏模块
    """
    ai_settings = Settings()
    pygame.init() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    bullets = Group()
    pygame.display.set_caption('Alien Invasion')
    while True:
        #循环检查事件
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
if __name__ == "__main__":
    run_game()