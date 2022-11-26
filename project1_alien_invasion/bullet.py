import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):   # The class Bullet inherits from Sprite
    '''A class to manage bullets fired from the ship'''

    def __init__(self, ai_game):
        '''Create a bullet object at the ship's current position'''
        super().__init__()  # super() to inherit properly from Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Load the bullet image and get its rect.
        self.image = pygame.image.load(r'C:\Users\Jimmy Son\Desktop\Python Crash Course\project_1_alien_invasion\images\bullet.bmp')  # returns a surface
        self.rect = self.image.get_rect()   # use x-y coordinate when working with a rect object
        
        # Create a bullet rect at (0, 0) and then set correct position -> bullet as a rectangle
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop # match bullet to the ship's midtop position

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)


    def update(self):
        '''Move the bullet up the screen'''
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y
    
    
    def blitme(self):   # draw bullet image
        '''Draw the bullet at its current location'''
        self.screen.blit(self.image, self.rect)

    
    def draw_bullet(self):  # draw bullet rectangle
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)