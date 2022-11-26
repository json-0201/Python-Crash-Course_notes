# Adding the Ship Image
# load the image and use pygame.blit() method to draw the image
# pygame loads bitmaps(bmp) by default

# Creating the Ship Class
# This class will manage most of the behavior of the player’s ship

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''A class to manage the ship'''

    def __init__(self, ai_game):    # ai_game = reference to the current instance of the AlienInvasion class
        '''Initialize the ship and set its starting position'''
        super().__init__()
        self.screen = ai_game.screen    # assign the screen to an attribute of Ship
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()    # pygame treats all game elements like rectangles (rects)

        # Load the ship image and get its rect.
        self.image = pygame.image.load(r'C:\Users\Jimmy Son\Desktop\Python Crash Course\project_1_alien_invasion\images\ship.bmp')  # returns a surface
        self.rect = self.image.get_rect()   # use x-y coordinate when working with a rect object
        
        '''
        When you’re centering a game element, work with the center, centerx, or centery attributes of a rect.
        When you’re working at an edge of the screen, work with the top, bottom, left, or right attributes.
        '''
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x) # rect only keeps the integer, need more accurate representation of x position

        # Movement flag - motionless when False / in-motion when True
        self.moving_right = False # Initialize
        self.moving_left = False # Initialize


    def update(self):
        '''Update the ship's position based on the movement flag'''
        # Update the ship's x-value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:  # self.rect.right returns x coordinate of the right edge of the ship's rect
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: # self.rect.left returns x coordinate of the left edge of the ship's rect
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x    # rect.x controls the position of the ship - update it using self.x


    def center_ship(self):
        '''Center the ship on the screen'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)