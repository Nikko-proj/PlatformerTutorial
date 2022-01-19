# Player creation and logic
import pygame
import CONSTANTS

from platforms import MovingPlatform
from spritesheet_funct import SpriteSheet


class Player(pygame.sprite.Sprite):
    # This class represents the bar the at the bottom that the player controls

    # Methods
    def __init__(self):
        # Constructor function

        # Call the parent's Constructor
        super().__init__()

        # Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right for the player
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("MegamanBN4.png")
        # Load all the right facing images into a list
        # Contains coordinates from the sprite sheet file used
        # (x1,y1) to (x2,y2)
        image = sprite_sheet.get_image(3, 88, 24, 29)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(32, 88, 22, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(64, 88, 17, 30)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(90, 88, 18, 33)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(116, 88, 20, 30)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(143, 88, 23, 30)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(172, 88, 14, 32)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them to face left
        image = sprite_sheet.get_image(3, 88, 24, 29)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(32, 88, 22, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(64, 88, 17, 30)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(90, 88, 18, 33)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(116, 88, 20, 30)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(143, 88, 23, 30)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(172, 88, 14, 32)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect
        self.rect = self.image.get_rect()

    def update(self):
        # Move the player
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

            # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= CONSTANTS.WINDOW_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = CONSTANTS.WINDOW_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= CONSTANTS.WINDOW_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
