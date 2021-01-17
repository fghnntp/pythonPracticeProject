class GameStats():
    """
    trace the game stats
    """
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = True
        self.reset_stats()
        # hiest score in this moment
        self.high_score = 0

    def reset_stats(self):
        """
        reset the game static information
        """
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1