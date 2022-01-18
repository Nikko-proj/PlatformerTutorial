# Following tutorial at http://programarcadegames.com/ on "Platformer with Sprite Sheets
# This module is used to pull individual sprites from sprite sheets

import pygame
import CONSTANTS

class SpriteSheet(object):
    # Class used to grab images from a sprite sheet.

    def __init__(self, file_name):
        # Constructor to pass in the file name of the sprite sheet.

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        # Grab a single image out of a larger spritesheet
        # Pass in the x, y location of the sprite
        # and the width and height of the sprite

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image.
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transpartent color
        image.set_colorkey(CONSTANTS.Black)

        # Return the Image
        return image

