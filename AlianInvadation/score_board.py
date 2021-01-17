import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """
    score display class
    """
    def __init__(self, ai_settings, screen, stats):
        # init some socre info
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # display font configration
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # prepare the score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """
        convert score to iamge
        """
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.socre_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        # set the score in right top of the screen
        self.score_rect = self.socre_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """
        convert highest socre to image
        """
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color, self.ai_settings.bg_color)
        # display higest score int the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """
        convert player level to iamge
        """
        self.level_image = self.font.render(str(self.stats.level), True,
                            self.text_color, self.ai_settings.bg_color)
        # display the level in the bottom of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """
        display the score on the screen
        """
        self.screen.blit(self.socre_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)