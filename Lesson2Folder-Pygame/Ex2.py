import pygame
import math
import random

# This is a 2d vector that holds the size of the screen.
SCREEN_SIZE = [1024, 768]

# Sets the prefered fps.  Mostly affects the speed of the main gameloop,
# although complex calculations may cause the fps to drop.
# Use delta_time to link movement to frame change speed.
FPS = 150

LINE_WIDTH = 5
RADIUS = SCREEN_SIZE[1] / 2.1
ROTATION_MOD = 1.674562  # How fast the thingy spins.

# Delta time is set to the change in time after each frame.
delta_time = 0

# The initial line position is in the middle of the screen, at the size of the screen height / 2.
line_point_start = [SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - RADIUS]

rotation = 0

# This function handles any input.  Called before update.
def handle_input():
    global game_stopped

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True

# This is the "do game math" function.  Put any math or functional code here.
# Called after handle_input.  This function is updated FPS times per second.
def update():
    global rotation, line_point_start

    # Increment rotation.
    rotation += ROTATION_MOD

    # Calculate rotation of the line by using the radius as the scale factor for
    # the hypotensue of a right triangle with a theta of rotation degrees.
    line_point_start[0] = (SCREEN_SIZE[0] / 2) + math.cos(math.radians(rotation)) * RADIUS
    line_point_start[1] = (SCREEN_SIZE[1] / 2) - math.sin(math.radians(rotation)) * RADIUS

    #line_point_start[0] = line_point_start[0] * math.cos(math.radians(rotation)) - line_point_start[1] * math.sin(math.radians(rotation))
    #line_point_start[1] = line_point_start[1] * math.cos(math.radians(rotation)) + line_point_start[0] * math.sin(math.radians(rotation))

    # The end point of the line is on the oposite side of the circle.
    line_point_end = [SCREEN_SIZE[0] - line_point_start[0], SCREEN_SIZE[1] - line_point_start[1]]

    # Draw the line.
    pygame.draw.line(DISPLAY_SURFACE, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), line_point_start, line_point_end, LINE_WIDTH)

# This function initializes the pygame window.
def init():
    global DISPLAY_SURFACE  # Initialize the global DISPLAY_SURFACE variable.

    pygame.init()  # Start pygame.

    # Makes a screen, size by screen_size and names it.
    DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Random Shapes")

    gameloop()  # Start the gameloop.

# This is the gameloop section of code.
# This template is designed so that you don't need to interact with
# this function / section of the code.
def gameloop():
    global game_stopped

    # This is the start of the gameloop.
    game_stopped = False
    while not game_stopped:
        time_at_frame_start = pygame.time.get_ticks()  # Get time before calulations.

        handle_input()  # First Gameloop Stage.

        update()  # Second Gameloop Stage.

        pygame.display.update() # Updates the display with changes.

        # Set the wait_time (after calculations have been made) (in ms, not seconds)
        # wait_time = time_single_frame_ - time_elapsed_
        wait_time = ((1 / float(FPS)) * 1000) - (pygame.time.get_ticks() - time_at_frame_start)

        pygame.time.wait(int(wait_time))  # Pause the program for the set amount of time.

        delta_time = wait_time / 1000.0  # This updates the delta time variable. (in seconds, not ms)
        #print delta_time

    # Close pygame before application closes.
    pygame.quit()

init()  # This is pretty much the only instruction run in the global scope.

print "Application Complete."
