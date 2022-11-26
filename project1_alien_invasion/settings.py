# Creating a Settings Class
'''
Each time we introduce new functionality into the game, we’ll typically create some new settings as well.
Instead of adding settings throughout the code,
let’s write a module called settings that contains a class called Settings to store all these values in one place.
This approach allows us to work with just one settings object any time we need to access an individual setting.
This also makes it easier to modify the game’s appearance and behavior as our project grows.
'''

class Settings:
    '''A class to store all settings for Alien Invasion'''

    def __init__(self):
        '''Initialize the game's static settings'''

        # screen settings
        self.screen_width = 1500
        self.screen_height = 750
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        '''Initialize settings that change throughout the game'''
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50


    def increase_speed(self):
        '''Increase speed settings and alien point values'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
