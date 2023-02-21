import random

import pygame

from screen import Screen

# Set game values
STARTING_END_NUMBER = 60
STARTING_ENEMY_SPEED = 1
ENDING_END_NUMBER = 10
UPDATE_SPEED = 0.5
ENDING_SPEED = 9

# Set colors
COLOR_ONE = (255, 0, 0)
COLOR_TWO = (255, 255, 0)
COLOR_THREE = (0, 255, 255)
COLOR_FOUR = (255, 0, 255)
COLOR_FIVE = (51, 92, 103)
COLOR_SIX = (242, 84, 45)
COLOR_SEVEN = (2, 195, 154)


class EnemyManager(Screen):
    def __init__(self, size):
        super().__init__()
        self.list_of_colors = [COLOR_ONE, COLOR_TWO, COLOR_THREE, COLOR_FOUR, COLOR_FIVE, COLOR_SIX]
        self.all_enemies = []
        self.end_number = STARTING_END_NUMBER
        self.speed = STARTING_ENEMY_SPEED
        self.size = size
        self.color = random.choice(self.list_of_colors)

    # Method for creating enemy
    def create_enemy(self):
        # Random number to avoid spawning 50 enemies per second
        number = random.randint(1, self.end_number)
        # If random number is 1
        if number == 1:
            # Create random position of y
            random_y = random.randint(100, self.screen_height - 100)
            # Create new enemy
            new_enemy = pygame.Rect(self.screen_width, random_y, self.size, self.size)
            # Append new enemy to list of all enemies
            self.all_enemies.append(new_enemy)
        # Call method for moving enemies
        self.move_enemies()

    # Method for moving enemies
    def move_enemies(self):
        # For enemy in list of all enemies
        for enemy in self.all_enemies:
            # Draw enemy
            pygame.draw.rect(self.display_surface, self.color, enemy)
            # Add speed to enemy
            enemy.x -= self.speed

    # Method for updating enemies (harder levels)
    def update_enemy(self):
        # If speed is smaller than ending speed
        if self.speed < ENDING_SPEED:
            # Add UPDATE_SPEED to speed
            self.speed += UPDATE_SPEED
        # If end number is bigger than ending end number
        if self.end_number > ENDING_END_NUMBER:
            # Reduce 10 from end number
            self.end_number -= 10

    # Reset enemy after player reaches the finish line
    def reset_enemy_finish(self):
        # Change color to random color
        self.color = random.choice(self.list_of_colors)
        # Clear all enemies from display
        self.all_enemies.clear()

    # Reset enemies after player death
    def reset_enemy_game_over(self):
        # Call method enemy finish because to change color and delete all enemies
        self.reset_enemy_finish()
        # Reset speed
        self.speed = STARTING_ENEMY_SPEED
        # Reset end number
        self.end_number = STARTING_END_NUMBER
