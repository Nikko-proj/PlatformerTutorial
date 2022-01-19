# Main game file
import pygame
import CONSTANTS
import levels

from player import Player


def main():
    # Main Program
    pygame.init()

    # Set the height and width of the screen
    size = [CONSTANTS.WINDOW_WIDTH, CONSTANTS.WINDOW_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Megaman platformer")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = [levels.Level_01(player), levels.Level_02(player)]

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = CONSTANTS.WINDOW_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button
    done = False

    # Screen update time
    clock = pygame.time.Clock()

    # ---------Main Game Loop--------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_SPACE:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()

        # Update the player
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world (-x) left
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # Code to draw below
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        # Code to draw above

        # Limit to 60 FPS
        clock.tick(60)

        # Update and displayer screen with what we have drawn
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
