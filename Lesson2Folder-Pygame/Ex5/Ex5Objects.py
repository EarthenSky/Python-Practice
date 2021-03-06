import pygame, math
import pyCam  # This camera module overloads the pygame draw methods.

# Key press variables.
is_w_key_down = False
is_a_key_down = False
is_s_key_down = False
is_d_key_down = False

START_TIMER = False

# Reset some variables.
def reset_scene():
    global START_TIMER
    START_TIMER = False

class scene:
    """The scene gets size then position in the constructor.
        Has a colour map (array) that holds what type of ground is at any single position, grass, pavement, or dirt. (for the car)"""

    def __init__(self, size, pos):
        # Constructor Variables.
        self._size = size
        self._pos = pos

        # Setup scene main image.
        img = pygame.image.load("Track3.png").convert_alpha()
        self._img = img

        # Setup house img.
        house_img = pygame.image.load("House.png").convert_alpha()
        self._house_img = pygame.transform.scale(house_img, (256, 256))

        # Set the checkpoints that need to be hit before hitting the end flag.
        self._checkpoints_to_hit = ""

        self._can_do_it = False
        self._wait_timer = 0.0

        # Extra time to wait.
        self._timer_mod = 0

        # Init start point and checkpoints.
        self.checkpoints = [
            checkpoint((58, 1800), 0, False),
            checkpoint((1250, 362), 1, True),
            checkpoint((1325, 2552), 2, True),
            checkpoint((3344, 192), 3, True),
            checkpoint((2550, 3968), 4, True)
        ]

        # What lap you're on.
        self.lap_counter = 0

        self.is_game_complete = False

        # Set house position.
        self.house_pos = [
            (1300, 1700),
            (2800, 1000),
            (1045, 686)
        ]

    # Output the timermod then set to zero.
    def get_timer_mod(self):
        out = self._timer_mod
        self._timer_mod = 0
        return out

    def update(self, car_pos, dt):
        #print str(dt)

        # Stop Game
        if self.lap_counter > 2:
            self.is_game_complete = True

        if self._can_do_it == True:
            self._wait_timer += float(dt)
            if self._wait_timer > 1: # Wait a second.
                self._can_do_it = False

        # Update the checkpoints and output if it is over the correct one.
        for val in self.checkpoints:
            if val.active(car_pos):
                #print str( self._checkpoints_to_hit.find( str(val.number) ) )
                if self._checkpoints_to_hit.find( str(val.number) ) >= 0:  # Case, checkpoint has not been hit yet this lap.
                    # Remove the checkpoint.
                    self._checkpoints_to_hit = self._checkpoints_to_hit.replace( str(val.number) , "")
                    #print str(val.number) + " v2"

                    return str(val.number)

                elif val.number == 0 and self._can_do_it == False:  # Case: hitting the start line
                    self._can_do_it = True
                    self._wait_timer = 0.0

                    self._timer_mod = len(self._checkpoints_to_hit) * 15  # add 15s each missed checkpoint.

                    self.lap_counter += 1

                    self._checkpoints_to_hit = "1234"  # Reset checkpoints to hit.

                    #print str(val.number) + " v1"

                    return str(val.number)
        return ""

    # Draws the img of the racetrack.
    def draw(self, surface):
        pyCam.draw_img( "main_cam", surface, self._img, (self._pos[0], self._pos[1]) )

        # Draw checkpoints.
        for val in self.checkpoints:
            val.draw(surface)

        # Draw houses.
        for val in self.house_pos:
            pyCam.draw_img("main_cam", surface, self._house_img, val)

class car:
    """This is the car class.  This holds controls, image, position, drawing, etc..."""

    def __init__(self, size, pos):
        # Constructor Variables.
        self._size = size
        self._pos = pos
        self._INIT_POS = pos  # Const, do not edit.

        # "Static" Variables.
        self._speed = 0.0
        self._angle = 90.0

        # Setup car image.
        self._img = pygame.image.load("SimpleGreenCarTopView.png").convert_alpha()
        self._img = pygame.transform.scale(self._img, (self._size[0], self._size[1]))

        # Load the car's colour map.
        self._colour_map = pygame.image.load("TrackColourMap.png")

    def reset(self):
        self._pos = self._INIT_POS

        self._speed = 0.0
        self._angle = 90.0

    # Return the position.
    def get_position(self):
        return self._pos

    def get_speed(self):
        return self._speed

    # Standard wasd keypress up-down handling.
    def check_input(self, event):
        global is_w_key_down, is_a_key_down, is_s_key_down, is_d_key_down
        global START_TIMER
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_w_key_down = True
                START_TIMER = True
                return True
            elif event.key == pygame.K_LEFT:
                is_a_key_down = True
                return True
            elif event.key == pygame.K_DOWN:
                is_s_key_down = True
                START_TIMER = True
                return True
            elif event.key == pygame.K_RIGHT:
                is_d_key_down = True
                return True
            elif event.key == pygame.K_w:
                is_w_key_down = True
                START_TIMER = True
                return True
            elif event.key == pygame.K_a:
                is_a_key_down = True
                return True
            elif event.key == pygame.K_s:
                is_s_key_down = True
                START_TIMER = True
                return True
            elif event.key == pygame.K_d:
                is_d_key_down = True
                return True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_w_key_down = False
                return True
            elif event.key == pygame.K_LEFT:
                is_a_key_down = False
                return True
            elif event.key == pygame.K_DOWN:
                is_s_key_down = False
                return True
            elif event.key == pygame.K_RIGHT:
                is_d_key_down = False
                return True
            elif event.key == pygame.K_w:
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

    # Draws the img of the race-car, rotated.
    def draw(self, surface):
        blit_img = pygame.transform.rotate(self._img, self._angle)
        blit_img_rect = blit_img.get_rect(center=self._pos)

        pyCam.draw_img("main_cam", surface, blit_img, (blit_img_rect[0] + self._size[0]/2, blit_img_rect[1] + self._size[1]/2, blit_img_rect[2], blit_img_rect[3]))
        #print str(self._check_wheels(surface))

    # Returns a tuple containing the values of each wheel.  0 is pavement, 1 is dirt, and 2 is grass.  -1 is error.
    # the order of the values is from left to right, topleft, bottomleft, topright, bottomright.
    # Ex. When the left of the car is on dirt it would return -> (1, 1, 0, 0)
    def _check_wheels(self, surface):
        car_center_pos = (self._pos[0] + self._size[0]/2, self._pos[1] + self._size[1]/2)

        # This is the pixel position of each wheel.
        # 52 (px) is the distance from the wheel center to the car center.  23.7 is the angle to the point.
        wheel_top_left_position = (
            int(car_center_pos[0] + 60 * math.cos(math.radians(-self._angle - 23))),
            int(car_center_pos[1] + 60 * math.sin(math.radians(-self._angle - 23))))
        wheel_bottom_left_position = (
            int(car_center_pos[0] + 60 * math.cos(math.radians(-self._angle - 180 + 23))),
            int(car_center_pos[1] + 60 * math.sin(math.radians(-self._angle - 180 + 23))))
        wheel_top_right_position = (
            int(car_center_pos[0] + 60 * math.cos(math.radians(-self._angle + 23))),
            int(car_center_pos[1] + 60 * math.sin(math.radians(-self._angle + 23))))
        wheel_bottom_right_position = (
            int(car_center_pos[0] + 60 * math.cos(math.radians(-self._angle - 180 - 23))),
            int(car_center_pos[1] + 60 * math.sin(math.radians(-self._angle - 180 - 23))))

        #print str(wheel_top_left_position) + " " + str(wheel_bottom_left_position) + " " + str(wheel_top_right_position) + " " + str(wheel_bottom_right_position)

        # Init the return values.
        top_left_val = -1
        bottom_left_val = -1
        top_right_val = -1
        bottom_right_val = -1

        # Check the top left pixel.
        try:
            top_left_colour = tuple(self._colour_map.get_at( (wheel_top_left_position[0], wheel_top_left_position[1]) ))

            # Set the return values
            if top_left_colour[0] > 200:  # If red then grass.
                top_left_val = 2
            elif top_left_colour[1] > 200:  # If green then dirt.
                top_left_val = 1
            elif top_left_colour[2] > 200:  # If blue then track.
                top_left_val = 0
        except:
            top_left_colour = 0
            top_left_val = 2

        # Check the bottom left pixel.
        try:
            bottom_left_colour = tuple(self._colour_map.get_at( (wheel_bottom_left_position[0], wheel_bottom_left_position[1]) ))

            # Set the return values
            if bottom_left_colour[0] > 200:  # If red then grass.
                bottom_left_val = 2
            elif bottom_left_colour[1] > 200:  # If green then dirt.
                bottom_left_val = 1
            elif bottom_left_colour[2] > 200:  # If blue then track.
                bottom_left_val = 0
        except:
            bottom_left_colour = 0
            bottom_left_val = 2

        # Check the top right pixel.
        try:
            top_right_colour = tuple(self._colour_map.get_at( (wheel_top_right_position[0], wheel_top_right_position[1]) ))

            # Set the return values
            if top_right_colour[0] > 200:  # If red then grass.
                top_right_val = 2
            elif top_right_colour[1] > 200:  # If green then dirt.
                top_right_val = 1
            elif top_right_colour[2] > 200:  # If blue then track.
                top_right_val = 0
        except:
            top_right_colour = 0
            top_right_val = 2

        # Check the bottom right pixel.
        try:
            bottom_right_colour = tuple(self._colour_map.get_at( (wheel_bottom_right_position[0], wheel_bottom_right_position[1]) ))

            # Set the return values
            if bottom_right_colour[0] > 200:  # If red then grass.
                bottom_right_val = 2
            elif bottom_right_colour[1] > 200:  # If green then dirt.
                bottom_right_val = 1
            elif bottom_right_colour[2] > 200:  # If blue then track.
                bottom_right_val = 0
        except:
            bottom_right_colour = 0
            bottom_right_val = 2

        #print str(top_left_colour) + " " + str(bottom_left_colour) + " " + str(top_right_colour) + " " + str(bottom_right_colour)

        pyCam.draw_rect("main_cam", surface, (0,0,0,255), wheel_top_left_position + (4, 4))
        pyCam.draw_rect("main_cam", surface, (0,0,0,255), wheel_top_right_position + (4, 4))
        pyCam.draw_rect("main_cam", surface, (0,0,0,255), wheel_bottom_left_position + (4, 4))
        pyCam.draw_rect("main_cam", surface, (0,0,0,255), wheel_bottom_right_position + (4, 4))

        # Return the values.
        return [top_left_val, bottom_left_val, top_right_val, bottom_right_val]

    # Updates position, speed, and angle.
    def update(self, dt, surface):
        # Before player is moved, check where it's wheels are on the colour map.
        wheel_type = self._check_wheels(surface)

        # Have wheel position affect the car, before the player is moved. (ground mod)
        for key in range(len(wheel_type)):
            if wheel_type[key] == 1:  # If the wheel is on dirt, the car decelerates a bit until it is under half of the top speed.
                if self._speed > 15 * 30 * 1.45 / 2:
                    self._speed -= 3.6 * dt * 30 * (not is_s_key_down)

                if key < 2:  # Left wheels.
                    self._angle += dt * self._speed * 0.005
                else:  # Right wheels.
                    self._angle -= dt * self._speed * 0.005

            elif wheel_type[key] == 2: # If the wheel is on grass, the car decelerates until it is under a third of the top speed.
                if self._speed > 15 * 30 * 1.45 / 2.5:
                    self._speed -= 8.3 * dt * 30 * (not is_s_key_down)

                if key < 2:  # Left wheels.
                    self._angle += dt * self._speed * 0.015
                else:  # Right wheels.
                    self._angle -= dt * self._speed * 0.015

        # Speed manager -> Manages how the user interacts with the speed variable. (acceleration)
        if is_w_key_down == True:
            self._speed += 6 * dt * 30
        elif is_s_key_down == True:
            self._speed -= 30 * dt * 30
        else:  # Road friction.
            self._speed -= 10 * dt * 30

        # Speed capper -> Caps the speed value. (top speed)
        if self._speed > 15 * 30 * 1.45 * 1.05:
            self._speed = 15 * 30 * 1.45 * 1.05
        elif is_s_key_down == False and self._speed < 0:
            self._speed = 0
        elif is_s_key_down == True and self._speed < -4 * 30 * 1.5:
            self._speed = -4 * 30 * 1.5

        # Pre assign the speed value
        out_speed = self._speed

        # Angle manager -> Manages how the user interacts with the angle variable. (turn speed)
        if is_a_key_down == True:
            self._angle += dt * self._speed * 0.19
            out_speed = self._speed * 0.98

        elif is_d_key_down == True:
            self._angle -= dt * self._speed * 0.19
            out_speed = self._speed * 0.98

        # Moves the player.
        run = float(out_speed) * math.cos(math.radians(-self._angle))
        rise = float(out_speed) * math.sin(math.radians(-self._angle))

        self._pos = (self._pos[0] + run * dt, self._pos[1] + rise * dt)

class checkpoint:
    """This is the checkpoint class.  The 0th checkpoint (set number to zero)
        is the starting checkered line thing."""
    def __init__(self, pos, number, rot_flip=False):
        self._pos = pos
        self.number = number

        self._size = (256, 48)

        self._rot_flip = rot_flip

        # Assign image based on number.
        if number == 0:
            self._img = pygame.image.load("StartPoint.png").convert()
        else:
            self._img = pygame.image.load("CheckPoint.png").convert_alpha()

    # If the current checkpoint has the car in it.
    def active(self, car_pos):
        # Rotate the size if needed.
        temp_size = 0
        if self._rot_flip == True:
            temp_size = (self._size[1], self._size[0])
            # Modify car_pos to hit the checkpoints. (different for different rotations.)
            car_pos = (car_pos[0] + temp_size[0], car_pos[1] - temp_size[1]/3)
        else:
            temp_size = self._size
            # Modify car_pos to hit the checkpoints.
            car_pos = (car_pos[0] - temp_size[0]/1.3, car_pos[1] - temp_size[1]/3)

        # Distance between car and self.
        distance = (self._pos[0] - car_pos[0], self._pos[1] - car_pos[1])

        if ( distance[0] > 0 and distance[0] < 0 + temp_size[0] ) and ( distance[1] > 0 and distance[1] < 0 + temp_size[1] ):
            return True
        else:
            return False

    # Draws the img of the checkpoint.
    def draw(self, surface):
        # Rotate the sprite if needed to be.
        if self._rot_flip == True:
            blit_img = pygame.transform.rotate(self._img, 990)
            blit_img_rect = blit_img.get_rect(center=self._pos)

            pyCam.draw_img("main_cam", surface, blit_img, (blit_img_rect[0], blit_img_rect[1]))

        else:
            pyCam.draw_img("main_cam", surface, self._img, (self._pos[0], self._pos[1]))

class ui:
    """This is the ui class.  This holds things like the lap timer and speed gui.
        This class draws them without using the camera so they don't move."""

    def __init__(self):
        # Init the ui's font.
        self._speed_font = pygame.font.SysFont("monospace", 48)
        self._speed_text = self._speed_font.render("Speed: {} km/h".format( 0 ), 1, (255, 255, 255))

        # Init timer stuff.
        self.timer_is_stopped = False
        self._timer_value = 0.0
        self._timer_font = pygame.font.SysFont("serif", 48)
        self._timer_text = self._timer_font.render("Timer: {}:{}s".format( 0, 0 ), 1, (255, 255, 255))

        # Init checkpoint counter stuff.
        self._checkpoints = ""
        self._checkpoint_font = pygame.font.SysFont("sans-serif", 48)
        self._checkpoint_text = self._checkpoint_font.render(self._checkpoints, 1, (255, 255, 255))

        # Init checkpoint counter stuff.
        self._lap_font = pygame.font.SysFont("monospace", 64)
        self._lap_text = self._lap_font.render(str(0), 1, (255, 255, 255))

    def reset(self):
        self._timer_value = 0
        self.timer_is_stopped = False

    # Draws the img of the checkpoint.
    def update(self, car_speed, dt, timer_mod, current_lap, car_reset):
        global START_TIMER  # Remember global
        # Update speed text.
        self._speed_text = self._speed_font.render("Speed: {} km/h".format( int(car_speed/4) ), 1, (255, 255, 255))

        # Update the timer's time value. (by the time the last frame took [dt or delta_time])
        if self.timer_is_stopped == False and START_TIMER == True:
            self._timer_value += dt + timer_mod
            self._timer_text = self._timer_font.render("Timer: {}:{}s".format( int(self._timer_value/60), float(int((self._timer_value%60.0)*100.0))/100.0 ), 1, (255, 255, 255))
        elif self.timer_is_stopped == True and START_TIMER == True:

            # Write the time to a file.
            with open("scores.errerr.7bxnlk.jp.win85", "a") as out_file:
                out_file.write( "Time: {}:{}s".format( int(self._timer_value/60), float(int((self._timer_value%60.0)*100.0))/100.0 ) )

            # Go to the menu scene and reset the old one.
            self.reset()
            car_reset()
            reset_scene()
            return 0

        # Update the lap counter.
        self._lap_text = self._lap_font.render( "Lap: " + str(current_lap), 1, (255, 255, 255))
        return 1

    # Sets the checkpoints.
    def set_checkpoints(self, str_checkpoints):
        self._checkpoints += str_checkpoints
        self._checkpoint_text = self._checkpoint_font.render(self._checkpoints, 1, (255, 255, 255))

    # Draws the ui to the screen, not the camera.
    def draw(self, surface):
        surface.blit(self._speed_text, (16, 16))
        surface.blit(self._timer_text, (16, 128))
        surface.blit(self._checkpoint_text, (16, 256-32))
        surface.blit(self._lap_text, (16, 256 + 128))

class button:
    """This is a button class.  It calls a function when pressed.  Uses the default font for text.
        Text is centered, yay!"""

    def __init__(self, pos, size, pressed, text, operands=None):
        # Init the position and size.
        self._pos = pos
        self._size = size

        self._function = pressed
        self._operands = operands

        self._font = pygame.font.SysFont("monospace", 48)
        self._text_string = text

    # If clicked, run function.
    def update(self):
        if pygame.mouse.get_pressed()[0] == True:
            mouse_pos = pygame.mouse.get_pos()

            # Check if mouse is inside the button.
            if ( mouse_pos[0] < self._pos[0] + self._size[0] and mouse_pos[0] > self._pos[0] ) and ( mouse_pos[1] < self._pos[1] + self._size[1] and mouse_pos[1] > self._pos[1] ):
                if self._operands == None:
                    self._function()
                else:
                    self._function(self._operands)

    # Resizes the button.
    def resize(self, pos, size):
        self._pos = pos
        self._size = size

    # Draws the ui to the screen, not the camera.
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 100), (self._pos[0], self._pos[1], self._size[0], self._size[1]), 0)

        # Draw the text to the screen.
        size = self._font.size(self._text_string)
        text = self._font.render(self._text_string, 1, (255, 255, 255))
        surface.blit(text, (self._pos[0] - (size[0] - self._size[0]) / 2, self._pos[1] + self._size[1]/2 - 48/2))
