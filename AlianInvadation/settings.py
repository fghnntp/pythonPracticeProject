class Settings():
    """
    存储游戏设置的类型
    """
    def __init__(self):
        # screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (240, 248, 255)
        # ship settings
        self.speed_factor = 2.5
        self.ship_limit = 3
        # bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowd = 3
        # alien settings
        self.alien_speed_factor = 1
        self.alien_drop_speed = 10
        self.fleet_direction = 1
        # game level
        self.speedup_scale = 2
        # alien point scale
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        init the game setting
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """
        speed up
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)