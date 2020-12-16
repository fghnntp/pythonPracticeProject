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
        
    def blitme(self):
        #将图像放置在方形容器上
        self.screen.blit(self.image, self.rect)

class Cat():
    """
        猫
    """
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('/Users/liuly/code/pythonProject/pythonPracticeProject/AlianInvadation/Src/爱宠05.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)