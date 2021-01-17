import pygame.font

class Button():
    """
    a button to show the play msg
    """
    def __init__(self, ai_setting, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # button size and attribute
        self.width, self.height = 200,50
        self.bullet_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # create button rect objetc, and placed it in the mid
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.pre_msg(msg)

    def pre_msg(self, msg):
        """
        apply mesg as pucter, then set center the button on it
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.bullet_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        draw a button with one color then draw text
        """
        self.screen.fill(self.bullet_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)