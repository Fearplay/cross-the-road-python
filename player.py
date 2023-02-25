import random

import pygame

from screen import Screen

# Set game values
PLAYER_SPEED = 3
START_LIVES = 3

# Set colors
COLOR_ONE = (0, 255, 0)
COLOR_TWO = (234, 140, 85)
COLOR_THREE = (255, 255, 255)
COLOR_FOUR = (205, 180, 219)


# Create class which extends from Screen
class Player(Screen):
    # Create init method
    def __init__(self, size):
        # Create this for use everything from Screen
        super().__init__()
        # Set list with colors
        self.list_of_colors = [COLOR_ONE, COLOR_TWO, COLOR_THREE, COLOR_FOUR]
        # Set size of our player
        self.size = size
        self.rect_left = self.screen_width // 2
        self.rect_top = self.screen_height - self.size
        # Set our player
        self.rect = pygame.Rect(self.rect_left, self.rect_top, self.size, self.size)
        # Set random color from our list
        self.color = random.choice(self.list_of_colors)
        # Set lives of player
        self.lives = START_LIVES
        # Set position
        self.set_initial_position()

    # Method for draw player
    def draw_player(self):
        pygame.draw.rect(self.display_surface, self.color, self.rect)

    def set_initial_position(self):
        self.rect.x = self.rect_left
        self.rect.y = self.rect_top

    # Method for resetting after player death
    def reset_player_died(self):
        self.color = random.choice(self.list_of_colors)
        self.lives = START_LIVES
        self.set_initial_position()

    # Method for resetting after player hits finish
    def reset_player_continue(self):
        self.set_initial_position()

    # Method for moving up
    def move_player_up(self):
        self.rect.y -= PLAYER_SPEED

    # Method for moving down
    def move_player_down(self):
        self.rect.y += PLAYER_SPEED

    # Method for moving left
    def move_player_left(self):
        self.rect.x -= PLAYER_SPEED

    # Method for moving right
    def move_player_right(self):
        self.rect.x += PLAYER_SPEED
