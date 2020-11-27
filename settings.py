class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self, caption):
        """Initialize the game's static setings."""
        # Screen settings:
        self.screen_caption = caption
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (204, 255, 153)

        # Ship settings:
        self.ship_limit = 2 

        # Bullet settings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3

        # Alien settings:
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the game's dynamic settings."""
        self.ship_speed = 1
        self.bullet_speed = 1
        self.alien_speed = 0.9

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring.
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)