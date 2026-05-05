class Settings():
    def __init__(self):
        # screen settings
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (28,37,60)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_height = 15
        self.bullet_wideth = 3
        self.bullet_color = (255,87,87)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_direction = 1 # 1 represents right ; -1 represents left
        self.fleet_drop_speed = 30