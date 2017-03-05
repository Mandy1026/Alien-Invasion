class Settings():
    """A class to store all settings for Alien Invasion."""
    def__init__(self):
        """Initialize the game's settings."""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color= (0, 0, 0)

        #Ship settings
        self.ship_speed_factor = 3

        #Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
