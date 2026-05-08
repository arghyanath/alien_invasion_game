class Settings():
    def __init__(self):
        # screen settings
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (28,37,60)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_height = 15
        self.bullet_wideth = 3
        self.bullet_color = (255,87,87)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_direction = 1 # 1 represents right ; -1 represents left
        self.fleet_drop_speed = 20
        self.alien_points = 10

        # dynamic speed;
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.score_scale = 1.5

    def initialize_dynamic_settings(self): #initialize the settings
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        self.alien_points = 10


    def increase_speed(self): # increasing speed level by level
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)