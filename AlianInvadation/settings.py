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
        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowd = 3
        # alien settings
        self.alien_speed_factor = 1
        self.alien_drop_speed = 10
        self.fleet_direction = 1