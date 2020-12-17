import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """
        初始化当前窗口和游戏模块
    """
    ai_settings = Settings()
    pygame.init() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    pygame.display.set_caption('Alien Invasion')
    while True:
        #循环检查事件
        gf.check_event(ship)
        ship.update()
        gf.update_sccreen(ai_settings, screen, ship)
        
    
if __name__ == "__main__":
    run_game()