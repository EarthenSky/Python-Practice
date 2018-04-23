import pygame
import ctypes

pygame.init()
pygame.mixer.pre_init(44000, -16, 2, 2048)  # Setup mixer to avoid sound lag.
feet_steps_sound = pygame.mixer.Sound('slide.wav')  # Load sound effect.
ded_sound = pygame.mixer.Sound('Die_Smash.wav')  # Load sound effect.

# Constants
GAME_FRICTION_COEFFICIENT = 0.99
ENEMY_ROTATION_SPEED = 400

# The player's class.  Has it's own position.
class player:
    def __init__ (self, position):
        # Keys that are down.
        self.is_w_key_down = False
        self.is_a_key_down = False
        self.is_s_key_down = False
        self.is_d_key_down = False

        # Setup normal variables.
        self._size = [64, 64]
        self._position = [position[0], position[1]]
        self._impulse = [0.0, 0.0]

        # Setup player image.
        self._img = pygame.image.load("red-char.png").convert_alpha()
        self._img = pygame.transform.scale(self._img, (self._size[0], self._size[1]))

    # Encapsulates the player image.
    def get_img (self):
        return self._img

    # Encapsulates the player's position.
    def get_position (self):
        return self._position

    # Encapsulates the player's position.
    def get_size (self):
        return self._size

    # Handle all player key presses.
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                feet_steps_sound.play()
                self.is_w_key_down = True
            elif event.key == pygame.K_a:
                feet_steps_sound.play()
                self.is_a_key_down = True
            elif event.key == pygame.K_s:
                feet_steps_sound.play()
                self.is_s_key_down = True
            elif event.key == pygame.K_d:
                feet_steps_sound.play()
                self.is_d_key_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.is_w_key_down = False
            elif event.key == pygame.K_a:
                self.is_a_key_down = False
            elif event.key == pygame.K_s:
                self.is_s_key_down = False
            elif event.key == pygame.K_d:
                self.is_d_key_down = False

    # Draws the player's image at it's center, to the display_surface.
    def draw (self, display_surface):
        display_surface.blit(self._img, (self._position[0] - self._size[0]/2, self._position[1] - self._size[1]/2))

    def update (self, dt):
        # Move player.
        if self.is_w_key_down == True:
            self._impulse[1] -= 10.0
        elif self.is_a_key_down == True:
            self._impulse[0] -= 10.0
        elif self.is_s_key_down == True:
            self._impulse[1] += 10.0
        elif self.is_d_key_down == True:
            self._impulse[0] += 10.0

        # Cap player slide / impulse speed, min and max.
        if abs(self._impulse[0]) > 500:
            if self.is_a_key_down:
                self._impulse[0] = -500
            elif self.is_d_key_down:
                self._impulse[0] = 500
        elif abs(self._impulse[0]) < 1 and self.is_a_key_down == False and self.is_d_key_down == False:
            self._impulse[0] = 0

        if abs(self._impulse[1]) > 500:
            if self.is_w_key_down:
                self._impulse[1] = -500
            elif self.is_s_key_down:
                self._impulse[1] = 500
        elif abs(self._impulse[1]) < 1 and self.is_w_key_down == False and self.is_s_key_down == False:
            self._impulse[1] = 0

        # Move player by impulse.
        self._position[0] += (self._impulse[0] * dt)
        self._position[1] += (self._impulse[1] * dt)

        # Calculate impulse friction.
        self._impulse = [float(self._impulse[0]) * GAME_FRICTION_COEFFICIENT, float(self._impulse[1])  * GAME_FRICTION_COEFFICIENT]

        #print str(self._impulse)

# An enemy class.  Has it's own position too.
class enemy:
    def __init__ (self, position):
        # Setup position and size varibles
        self._position = position
        self._size = (96, 96)
        self._rotation = 0

        # Setup this object's image
        self._img = pygame.image.load("SpikeBall.png").convert_alpha()
        self._img = pygame.transform.scale(self._img, (self._size[0], self._size[1]))

    def draw(self, display_surface):
        # Create the surface to blit, rotated around the center point.
        blit_surface = pygame.transform.rotate(self._img, self._rotation)
        blit_surface_rect = blit_surface.get_rect(center=self._position)

        display_surface.blit(blit_surface, blit_surface_rect)

    def update(self, dt):
        # Update rotation amount
        self._rotation += ENEMY_ROTATION_SPEED * dt

    def check_player_collision (self, player_position, player_size):
        # find verticle and hgorizontal distance.
        run = ( abs(player_position[0] - self._position[0]) )
        rise = ( abs(player_position[1] - self._position[1]) )

        # a^2 + b^2 = c^2 or c = sqrt(a^2 + b^2)
        distance = ((rise ** 2) + (run ** 2)) ** 0.5

        print str(distance)

        # If objects are too close, end game.
        if distance < (player_size[0] + self._size[0]) / 2 - 16:
            ded_sound.play()
            message_string = u"YOU LOSE THE ENTIRE GAME!  D:"
            ctypes.windll.user32.MessageBoxW(0, message_string, u"SO VERY SAD!!!", 0)

            return True  # Close the game.
        else:
            return False  # Don't close the game.
