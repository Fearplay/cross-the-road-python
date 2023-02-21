import random

import pygame

# Set screen variables
WINDOWS_WIDTH = 945
WINDOWS_HEIGHT = 600

# Set FPS and time
FPS = 60
clock = pygame.time.Clock()

# Set colors
COLOR_ONE = (0, 0, 0)
COLOR_TWO = (43, 45, 66)
COLOR_THREE = (0, 20, 39)

# Set background music
BACKGROUND_MUSIC_ONE = "resources/sound/game_music1.wav"
BACKGROUND_MUSIC_TWO = "resources/sound/game_music2.wav"
BACKGROUND_MUSIC_THREE = "resources/sound/game_music3.wav"

# Set sounds
HIT_SOUND = "resources/sound/hit.wav"
NEXT_ROUND_SOUND = "resources/sound/next_round.wav"


# Method for updating display
def update_display():
    pygame.display.flip()
    clock.tick(FPS)


class Screen:
    def __init__(self):
        # Init pygame
        pygame.init()
        # Set list with background music
        self.list_of_background_music = [BACKGROUND_MUSIC_ONE, BACKGROUND_MUSIC_TWO, BACKGROUND_MUSIC_THREE]
        # Choose random background music
        self.random_background_music = random.choice(self.list_of_background_music)
        # Load sounds
        self.hit_sound = pygame.mixer.Sound(HIT_SOUND)
        self.finish_sound = pygame.mixer.Sound(NEXT_ROUND_SOUND)
        # Set list with colors
        self.list_of_colors = [COLOR_ONE, COLOR_TWO, COLOR_THREE]
        # Choose random color
        self.color = random.choice(self.list_of_colors)
        self.screen_width = WINDOWS_WIDTH
        self.screen_height = WINDOWS_HEIGHT
        # Set display surface with screen variables
        self.display_surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        # Set caption
        pygame.display.set_caption("Cross the road")
        # Play background music on the begging
        self.play_background_music()

    # Method for filling screen
    def fill_screen(self):
        # Fill display with random color created on begging
        self.display_surface.fill(self.color)

    # Method for playing background music
    def play_background_music(self):
        # Load random background music
        pygame.mixer.music.load(self.random_background_music)
        # Play background music for infinity time
        pygame.mixer.music.play(-1, 0.0)
        # Set volume on less than before
        pygame.mixer.music.set_volume(0.3)

    # Method for playing hit sound
    def play_hit_sound(self):
        # Play loaded sound
        self.hit_sound.play()
        # Set volume of that sound
        self.hit_sound.set_volume(0.3)

    # Method for playing next round sound
    def play_next_round_sound(self):
        self.finish_sound.play()
        self.finish_sound.set_volume(0.3)
