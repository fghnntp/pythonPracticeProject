import sys
import pygame
from settings import Settings

def run_game():
    """
        初始化当前窗口和游戏模块
    """
    setting = Settings()
    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    while True:
        #循环检查事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #填充背景色
        screen.fill(setting.bg_color)
        #刷新界面
        pygame.display.flip()
    
if __name__ == "__main__":
    run_game()