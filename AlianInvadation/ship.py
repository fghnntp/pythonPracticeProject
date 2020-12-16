import pygame

class Ship():
    """
        宇宙飞船
    """
    def __init__(self, screen):
        self.screen = screen
        #获取图片，飞船的方形抽象，屏幕的方形抽象
        self.image = pygame.image.load('/Users/liuly/code/pythonProject/pythonPracticeProject/AlianInvadation/Src/飞船.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将方形容器放置在坐标的最底层
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #设置移动标志
        self.m_left = False
        self.m_right = False
        self.m_up = False
        self.m_down = False

    def update(self):
        """
            更新飞船的位置
        """     
        if self.m_left == True:
            self.rect.centerx -= 1
        elif self.m_right == True:
            self.rect.centerx += 1
        elif self.m_up == True:
            self.rect.centery -= 1
        elif self.m_down == True:
            self.rect.centery += 1
        
    def blitme(self):
        #将图像放置在方形容器上
        self.screen.blit(self.image, self.rect)