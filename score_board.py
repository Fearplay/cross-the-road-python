import os
import random

import pygame

from screen import Screen

# Set game value
START_SCORE = 0
# Set file for high score
HIGH_SCORE_FILE = "resources/text_file/high_score.txt"
# Set colors
BLACK = (0, 0, 0)
BACKGROUND_ONE = (0, 180, 216)
BACKGROUND_TWO = (238, 97, 35)
BACKGROUND_THREE = (217, 4, 41)
BACKGROUND_FOUR = (255, 89, 94)
BACKGROUND_FIVE = (244, 213, 141)

# Set font variable
FONT = "resources/font/SunnySpellsBasicRegular.ttf"


class ScoreBoard(Screen):
    def __init__(self):
        super().__init__()
        self.list_of_backgrounds = [BACKGROUND_ONE, BACKGROUND_TWO, BACKGROUND_THREE, BACKGROUND_FOUR, BACKGROUND_FIVE]
        self.random_background_color = random.choice(self.list_of_backgrounds)
        self.color = BLACK
        self.background_color = self.random_background_color
        self.score = START_SCORE
        # Open file in read mode as "data"
        with open(HIGH_SCORE_FILE, "r") as data:
            # If nothing in that file
            if os.path.getsize(HIGH_SCORE_FILE) == 0:
                # Set high score on score (0)
                self.high_score = self.score
            else:
                # Set high score with number from that file
                self.high_score = int(data.read())
        # set font
        self.font = pygame.font.Font(FONT, 32)

    # Method for showing score
    def score_text(self):
        # Render score text
        score_text = self.font.render("Score: " + str(self.score), True, self.color, self.background_color)
        # Get rect of score
        score_rect = score_text.get_rect()
        # Set (x,y) of our score
        score_rect.topleft = (0, 0)
        # Blit it on display
        self.display_surface.blit(score_text, score_rect)

    # Method for showing lives with attribute lives which will be taken from player
    def lives_text(self, lives):
        lives_text = self.font.render("Lives: " + str(lives), True, self.color, self.background_color)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (0, 50)
        self.display_surface.blit(lives_text, lives_rect)

    # Method for showing game over
    def game_over_text(self):
        game_over_text = self.font.render("GAME OVER ", True, self.color, self.background_color)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.display_surface.blit(game_over_text, game_over_rect)

    # Method for showing high score text
    def high_score_text(self):
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, self.color,
                                           self.background_color)
        high_score_rect = high_score_text.get_rect()
        high_score_rect.topleft = (0, 25)
        self.display_surface.blit(high_score_text, high_score_rect)

    # Method for showing continue after player's death
    def continue_score(self):
        continue_text = self.font.render("Click anything for continue", True, self.color,
                                         self.background_color)
        continue_rect = continue_text.get_rect()
        continue_rect.center = (self.screen_width // 2, (self.screen_height // 2) + 26)
        self.display_surface.blit(continue_text, continue_rect)

    # Method for showing your score after player's death
    def over_score(self):
        self.update_high_score()
        over_score_text = self.font.render("Your Score was: " + str(self.score), True, self.color,
                                           self.background_color)
        over_score_rect = over_score_text.get_rect()
        over_score_rect.center = (self.screen_width // 2, (self.screen_height // 2) + 52)
        self.display_surface.blit(over_score_text, over_score_rect)

    # Method for updating score
    def update_score(self):
        # Add 1 to score
        self.score += 1
        self.score_text()

    # Method for resetting score
    def reset_score(self):
        # Score is starting score
        self.score = START_SCORE
        self.score_text()

    # Method for updating high score
    def update_high_score(self):
        # If score is bigger than high score
        if self.score > self.high_score:
            # High score is score
            self.high_score = self.score
            # Open file with writing option as "data"
            with open(HIGH_SCORE_FILE, "w") as data:
                # Write into file my high score
                data.write(f"{self.high_score}")
