# Set imports
import pygame

from enemy_manager import EnemyManager
from player import Player
from score_board import ScoreBoard
from screen import Screen, update_display

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_ONE = (0, 180, 216)
BACKGROUND_TWO = (238, 97, 35)
BACKGROUND_THREE = (217, 4, 41)
BACKGROUND_FOUR = (255, 89, 94)
BACKGROUND_FIVE = (244, 213, 141)

# Create player with size 25
player = Player(25)
# Create "enemies" with size 50
enemy_manager = EnemyManager(50)
# Create screen
screen = Screen()
# Create score
score = ScoreBoard()


# Method for showing finish and enemies
def create_finish_and_enemy():
    # Fill screen with color selected in screen
    screen.fill_screen()
    for i in range(0, 5):
        # Draw finish i * (start position of y)
        draw_finish_line(i * 15)
    # Call method (create enemy) from "enemies"
    enemy_manager.create_enemy()


# Method for draw finish lane with attribute start position of y
def draw_finish_line(start_y):
    # Create start position
    start_position = 0
    # Create end_position
    end_position = 21
    # For i in range 45 (45 == WINDOWS_WIDTH / 21)
    for i in range(45):
        # If i % 2 is 0 for example 10 / 2
        if i % 2 == 0:
            # Change color of line on white
            color_of_line = WHITE
        # Else for example 10 / 3
        else:
            # Change color of line on black
            color_of_line = BLACK
        # Draw line on display
        pygame.draw.line(screen.display_surface, color_of_line, (start_position, start_y), (end_position, start_y), 15)
        # Add to Start Position, End Position
        start_position = end_position
        # Add to End Position 21
        end_position += 21
    # Draw black horizontal line
    pygame.draw.line(screen.display_surface, BLACK, (0, start_y), (screen.screen_width, start_y), 6)


# Create running on True
running = True
# While running is True
while running:
    # for event in pygame events
    for event in pygame.event.get():
        # If player click on quit button
        if event.type == pygame.QUIT:
            # End while loop
            running = False
    # Create keys for key which is pressed
    keys = pygame.key.get_pressed()
    # If score is smaller than 10
    if score.score < 10:
        # Player can use left key and if player x is bigger than 0. So player can touch only left side
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.rect.left > 0:
            player.move_player_left()
        # And right key and if player x is smaller than screen_width. So player can touch only right side
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.rect.right < screen.screen_width:
            player.move_player_right()
    # Player can go up if his y position is bigger than 0
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.rect.top > 0:
        player.move_player_up()
    # Player can go down if his y position is smaller than screen_height
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.rect.bottom < screen.screen_height:
        player.move_player_down()
    # Call method for create finish and enemy
    create_finish_and_enemy()
    # Call method for drawing player from Player
    player.draw_player()
    # Call method for showing score from Score
    score.score_text()
    # Call method for showing high score from Score
    score.high_score_text()
    # Call method for showing lives from Score with lives from Player
    score.lives_text(player.lives)
    # If player position of y is smaller than 68 (he reached the finish line)
    if player.rect.y < 68:
        # Call method for playing next round sound from Screen
        screen.play_next_round_sound()
        # If score >= 5 (If 6 in this case)
        if score.score >= 5:
            # Call method for update enemy (harder)
            enemy_manager.update_enemy()
        # Call method for updating score because he reached the finish line
        score.update_score()
        # Call method for resetting player after reaching the finish line
        player.reset_player_continue()
        # Call method for resetting enemies after reaching the finish line
        enemy_manager.reset_enemy_finish()
    # For enemy in list (all_enemies)
    for enemy in enemy_manager.all_enemies:
        # If player rect collide with enemy rect
        if player.rect.colliderect(enemy):
            # Call method for playing hit sound from Screen
            screen.play_hit_sound()
            # Reduce player lives
            player.lives -= 1
            # If lives of player == 0 we will pause the game
            if player.lives == 0:
                # Create pause on True
                pause = True
                # Call method for filling screen from Screen
                screen.fill_screen()
                # Call method for showing game over text
                score.game_over_text()
                # Call method for showing text that you can click on anything from Score
                score.continue_score()
                # Call method for showing end score from Score
                score.over_score()
                # Call method for updating display from Screen
                update_display()
                # While pause is True
                while pause:
                    # For event in pygame events
                    for event in pygame.event.get():
                        # If player click on quit button
                        if event.type == pygame.QUIT:
                            # End pause while loop
                            pause = False
                            # End running while loop
                            running = False
                        # If player click any key
                        if event.type == pygame.KEYDOWN:
                            # End pause while loop
                            pause = False
                            # Call method for resetting player after his death from Player
                            player.reset_player_died()
                            # Call method for resetting enemy after game over from "Enemies"
                            enemy_manager.reset_enemy_game_over()
                            # Call method for resetting score from Score
                            score.reset_score()
                            # Call method for updating display from Screen
                            update_display()

            else:
                # Call method for resetting player after reaching the finish line
                player.reset_player_continue()
    # Call method update display from Screen
    update_display()
# Call method update high score which will update high score after player leaving game from Score
score.update_high_score()
# Pygame quit
pygame.quit()
