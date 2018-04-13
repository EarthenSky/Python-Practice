import pygame, math
import pyCam  # This camera module overloads the pygame draw methods.

# Key press variables.
is_w_key_down = False
is_a_key_down = False
is_s_key_down = False
is_d_key_down = False

class scene:
    """The scene gets size then position in the constructor."""

    def __init__(self, size, pos):
        # Constructor Variables.
        self._size = size
        self._pos = pos

        # Setup scene image.
        self._img = pygame.image.load("Track.png").convert()
        self._img = pygame.transform.scale(self._img, (self._size[0], self._size[1])).convert()

    # Draws the img of the racetrack.
    def draw(self, surface):
        pyCam.draw_img("main_cam", surface, self._img, (self._pos[0], self._pos[1]))

class car:
    """This is the car class.  This holds controls, image, position, drawing, etc..."""

    def __init__(self, size, pos):
        # Constructor Variables.
        self._size = size
        self._pos = pos

        # "Static" Variables.
        self._speed = 0.0
        self._angle = 0.0

        # Setup car image.
        self._img = pygame.image.load("SimpleGreenCarTopView.png").convert_alpha()
        self._img = pygame.transform.scale(self._img, (self._size[0], self._size[1]))

    # Return the position.
    def get_position(self):
        return self._pos

    # Standard wasd keypress up-down handling.
    def check_input(self, event):
        global is_w_key_down, is_a_key_down, is_s_key_down, is_d_key_down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                is_w_key_down = True
                return True
            elif event.key == pygame.K_a:
                is_a_key_down = True
                return True
            elif event.key == pygame.K_s:
                is_s_key_down = True
                return True
            elif event.key == pygame.K_d:
                is_d_key_down = True
                return True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                is_w_key_down = False
                return True
            elif event.key == pygame.K_a:
                is_a_key_down = False
                return True
            elif event.key == pygame.K_s:
                is_s_key_down = False
                return True
            elif event.key == pygame.K_d:
                is_d_key_down = False
                return True
        return False

    # Draws the img of the race-car.
    def draw(self, surface):
        blit_img = pygame.transform.rotate(self._img, self._angle)
        blit_img_rect = blit_img.get_rect(center=self._pos)

        pyCam.draw_img("main_cam", surface, blit_img, (blit_img_rect[0], blit_img_rect[1]))

    # Updates position, speed, and angle.
    def update(self, dt):
        # Speed manager -> Manages how the user interacts with the speed variable.
        if is_w_key_down == True:
            self._speed += 6 * dt * 30
        elif is_s_key_down == True:
            self._speed -= 12 * dt * 30
        else:
            if self._speed >= 0:
                self._speed -= 10 * dt * 30
            else:
                pass
                #self._speed += 10 * dt

        # Speed capper -> Caps the speed value.
        if self._speed > 10 * 30:
            self._speed = 10 * 30
        elif is_s_key_down == False and self._speed < 0:
            self._speed = 0
        elif is_s_key_down == True and self._speed < -4 * 30:
            self._speed = -4 * 30

        # Angle manager -> Manages how the user interacts with the angle variable.
        if is_a_key_down == True:
            self._angle += 100 * dt
        elif is_d_key_down == True:
            self._angle -= 100 * dt

        # Move the player.
        run = float(self._speed) * math.cos(math.radians(-self._angle))
        rise = float(self._speed) * math.sin(math.radians(-self._angle))

        self._pos = (self._pos[0] + run * dt, self._pos[1] + rise * dt)

class checkpoint:
    """This is the checkpoint class."""
    def __init__(self, pos):
        self._pos = pos

    # Draws the img of the racetrack.
    def draw(self, surface):
        pyCam.draw_img("main_cam", surface, self._img, (self._pos[0], self._pos[1], self._size[0], self._size[1]))
