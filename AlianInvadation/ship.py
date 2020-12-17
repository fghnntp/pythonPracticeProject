import pygame

class Ship():
    """
        宇宙飞船
    """
    def __init__(self, screen, ai_settings):
        #初始化参数
        self.speed_factor = ai_settings.speed_factor
        self.screen = screen
        #获取图片，飞船的方形抽象，屏幕的方形抽象
        self.image = pygame.image.load('/Users/liuly/code/pythonProject/pythonPracticeProject/AlianInvadation/Src/飞船.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将方形容器放置在坐标的最底层
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #设置移动标志
        self.m_left = False
        self.m_right = False
        self.m_up = False
        self.m_down = False

    def update(self):
        """
            更新飞船的位置
        """     
        #对上下左右键进行响应
        if self.m_left == True and self.rect.left > self.screen_rect.left:
            self.centerx -= self.speed_factor
        if self.m_right == True and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed_factor
        if self.m_up == True and self.rect.top > self.screen_rect.top:
            self.centery -= self.speed_factor
        if self.m_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def blitme(self):
        #将图像放置在方形容器上
        self.screen.blit(self.image, self.rect)