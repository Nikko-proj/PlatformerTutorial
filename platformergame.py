# imports constants and initializes pygame
# Following tutorial on https://realpython.com/pygame-a-primer/
import CONSTANTS as CTS
import pygame as pg

# from module pygame.locals, import the following keywords
from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# initializes all pygame modules
pg.init()


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


# create from class Player a player
player = Player()


# move_ip() = move in place
def update(self, pressed_keys):
    if pressed_keys[K_w]:
        self.rect.move_ip(0, -5)
    elif pressed_keys[K_s]:
        self.rect.move_ip(0, 5)
    elif pressed_keys[K_d]:
        self.rect.move_ip(5, 0)
    elif pressed_keys[K_a]:
        self.rect.move_ip(-5, 0)


# Set up screen size 800x600
screen = pg.display.set_mode([CTS.WINDOW_HEIGHT, CTS.WINDOW_WIDTH])

# Run until the user asks to quit
running = True
# Main loop
while running:

    # check if use pressed the close button?
    for event in pg.event.get():
        # check if a key was pressed
        if event.type == KEYDOWN:
            # check which key was pressed and what to do
            if event.key == K_ESCAPE:
                print("You pressed escape!")
                running = False
        elif event.type == QUIT:
            print("You pressed the exit button!")
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pg.key.get_pressed()

    # update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill background screen with color from CONSTANTS
    screen.fill(CTS.Yellow)

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # create a surface and pass in a tuple containing its length and width
    surf = pg.Surface((20, 80))

    # # draw the surface on to the screen at the center
    # screen.blit(surf, (CTS.WINDOW_WIDTH / 2, CTS.WINDOW_HEIGHT / 2))
    #
    # # Flip the display
    # Updates the contents of the display to the screen
    pg.display.flip()

# Quit
pg.quit()
