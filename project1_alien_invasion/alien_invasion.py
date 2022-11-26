# Creating a Pygame Window and Responding to User Input
import sys # we'll use tools in the sys module to exit the game
from time import sleep
import pygame   # pygame contains functionality we need to make a game
from settings import Settings   # import the class Settings, which stores all settings for Alien Invasion
from game_stats import GameStats
from ship import Ship   # import the class Ship
from bullet import Bullet # import the Bullet class
from alien import Alien # import the Alien class
from button import Button # import the Button class
from scoreboard import Scoreboard # import the Scoreboard class


class AlienInvasion:    # create a class
    '''Overall class to manage game assets and behavior'''


    def __init__(self):
        '''Initialize the game, and create game resources'''
        pygame.init()   # initializes the background settings that pygame needs to work properly
        self.settings = Settings()  # create an instance of Settings and assign it to self.settings, whose attributes can be used in AlienInvasion
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
                                # creates a display window with input dimensions (60% of screen size)
                                # the object assigned to self.screen is called a surface - entire game window
                                # each element in the game, like an alien or a ship, is its own surface
        
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # python to figure out a window size that will fill the screen
        # self.settings.screen_width = self.screen.get_rect().width -> update fullscreen width in Setting
        # self.settings.screen_height = self.screen.get_rect().height -> update fullscreen height in Setting
                                                                     
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics, and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)  # Ship() requires one argument, ai_game. "self" argument referes to the current instance of AlienInvasion
                                # "self" argument gives Ship access to the game's resources, such as screen object
        self.bullets = pygame.sprite.Group()    # group to store all live bullets using pygame.sprite.Group class
        self.aliens = pygame.sprite.Group()     # group to store all live aliens using pygame.sprite.Group class
        self._create_fleet()    # create a fleet of aliens

        # Make the Play button
        self.play_button = Button(self, 'Play')

        '''
        When we activate the game’s animation loop, this surface will be redrawn   on every pass through the loop,
        so it can be updated with any changes triggered by user input
        '''

        # set the background color, in RGB colors
        self.bg_color = self.settings.bg_color


    def run_game(self):
        '''Start the main loop for the game'''
        while True: # the while loop contains an event loop and code that manages screen updates
            self._check_events()    # a helper method does work inside a class but isn't meant to be called through an instance
                                    # in Python, a single leading underscore indicates a helper method
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()   # refactoring using helper methods
            

    def _check_events(self):    # refactoring run_game method, helper method
        '''Respond to keypresses and mouse events'''
        # Watch for keyboard and mouse events
        for event in pygame.event.get():    # an event is an action that the user performs while playing the game, such as a keypress
                                                # we write this event loop to listen for events and perform appropriate tasks
                                                # pygame.event() function returns a list of events that have taken place since the last time this function was called
                
            if event.type == pygame.QUIT:   # when the player clicks the game window’s X button, a pygame.QUIT event is detected
                    sys.exit()  # sys module to exit the window
            
            # Add elif block to the event loop to respond when Pygame detects a KEYDOWN event
            elif event.type == pygame.KEYDOWN:  # Each keypress is registered as a KEYDOWN event
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:    # Each key-release is registered as a KEYUP event
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        '''Start a new game when the player clicks Play'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    
    def _check_keydown_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT: # K_RIGHT corresponds to the right arrow key
            # set moving_right to True
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:   # press Q to exit the game
            sys.exit()


    def _check_keyup_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
             # set moving_right to False
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:   # limits the number of fired bullets at a time
            new_bullet = Bullet(self)   # new_bullet is an instance of the class Bullet
            self.bullets.add(new_bullet)    # add() method is written specifically for Pygame groups


    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets'''
        # Update bullet positions
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():  # copy() method enables us to modify bullets inside the loop
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)         
        #print(len(self.bullets))

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        '''Respond to bullet-alien collisions'''
        # Remove any bullets and aliends that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()


    def _create_fleet(self):
        '''Create the fleet of aliens'''
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self) # 'self' is a reference to the current AlienInvasion (ai_game)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (4 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):   # nested loop
            for alien_number in range(number_aliens_x + 1):
                self._create_alien(alien_number, row_number)           


    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size # rect.size returns a tuple (width, height)
        alien.x = alien_width + 2 * alien_width * alien_number          # set x-coordinate of each alien
        alien.y = alien.rect.height + 2 * alien_height * row_number     # set y-coordinate of each alien
        alien.rect.x = alien.x  # place each alien to the set x-coordinate
        alien.rect.y = alien.y  # place each alien to the set y-coordinate
        self.aliens.add(alien)  # add alien instance to the group aliens
    

    def _update_aliens(self):
        '''Check if the fleet is at an edge, then update the positions of all aliens in the fleet'''
        self.aliens.update()

        # Look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_fleet_edges()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    
    def _check_fleet_edges(self):
        '''Respond appropriately if any aliens have reached an edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _ship_hit(self):
        '''Respond to the ship being hit by an alien'''
        if self.stats.ships_left > 1:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        '''Check if any aliens have reached the bottom of the screen'''
        screen_rect =self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break


    def _update_screen(self):   # refactoring run_game method, helper method
        '''Update images on the screen, and flip to the new screen'''
        # redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.bullets.draw(self.screen)
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible
        pygame.display.flip() # When we move the game elements around, pygame.display .flip() continually updates the display


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()