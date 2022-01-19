# Module for managing platform and platform logic
import pygame
from spritesheet_funct import SpriteSheet

# These constants define the platform types:
# Name of file
# X and Y Location of sprite
# Width and Height of sprite

GRASS_LEFT            = (576, 720, 70, 70)
GRASS_RIGHT           = (576, 576, 70, 70)
GRASS_MIDDLE          = (504, 576, 70, 70)
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)
# name_of_file        = (X,   Y,   Width,   Height)

class Platform(pygame.sprite.Sprite):
    # Platform the user can jump on

    def __init__(self, sprite_sheet_data):
        # Platform constructor. Assumes constructed with user
        # passing in an array of 5 numbers
        super().__init__()

        sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()

class MovingPlatform(Platform):
    # Moving platform

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        # Move the platform.
        # If the player is in the way, it will move the player.
        # This does not handle what happens if a platform shoves
        # a player into another object

        # Move left/right
        self.rect.x += self.change_x

        # Check if platform hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Player has been, then move the player
            # Assumes the player wont hit anything else

            # if we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # If we are moving left, do the opposite
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

            # Check the boundaries and see if we need to reverse
            # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
