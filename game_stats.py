class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats() # initializing stats

        self.game_active = False  
        
        self.score = 0
        self.high_score = 0
    
    def reset_stats(self):
        # initializes the stats / reset stats
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0