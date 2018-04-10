import pygame
import random

# This is a 2d vector that holds the size of the screen.
SCREEN_SIZE = [1024, 768]

# Sets the prefered fps.  Mostly affects the speed of the main gameloop,
# although complex calculations may cause the fps to drop.
FPS = 60  #FUN FACT, if you run this at > 5000 fps it stops hurting your eyes ...

# This is a constant primarily used to set the frequency of filled shapes appearing,
# yet it also affects the max line width and min object size.
# Min object size must be larger than the max fill width.
OBJECT_MAX_FILL = 1
OBJECT_MAX_SIZE = 400  # This is a constant used to choose object size.

# Starts pygame.
pygame.init()

# Makes a screen, size by screen_size and names it.
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Random Shapes")

# Runtime constant used to modify movement.
# Delta time is set to the change in time after each frame.
delta_time = 0

# Starts the game loop.
game_stopped = False
while not game_stopped:
    time_at_frame_start = pygame.time.get_ticks()  # Get time before calulations.

    # Input handeler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True

    # Chooses a random shape to draw
    random_number = random.randint(1, 4)

    # Pre calculate shared parameters.
    random_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    random_fill = random.randint(0, OBJECT_MAX_FILL)

    # Choose the shape to draw.
    if random_number == 1:
        '''----RECTANGLE----'''
        # Calculate Perameters
        random_position = ( random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]) )
        random_size = ( random.randint(OBJECT_MAX_FILL + 1, OBJECT_MAX_SIZE), random.randint(OBJECT_MAX_FILL + 1, OBJECT_MAX_SIZE) )

        # Draw Object
        pygame.draw.rect(DISPLAY_SURFACE, random_colour, (random_position, random_size), random_fill)

    elif random_number == 2:
        '''----CIRCLE----'''
        # Calculate Perameters
        random_position = ( random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]) )
        random_radius = random.randint(OBJECT_MAX_FILL + 1, OBJECT_MAX_SIZE/2)

        # Draw Object
        pygame.draw.circle(DISPLAY_SURFACE, random_colour, random_position, random_radius, random_fill)

    elif random_number == 3:
        '''----ELLIPSE----'''
        # Calculate Parameters
        random_position = ( random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]) )
        random_size = ( random.randint(OBJECT_MAX_FILL + 5, OBJECT_MAX_SIZE), random.randint(OBJECT_MAX_FILL + 5, OBJECT_MAX_SIZE) )

        # Draw Object
        pygame.draw.ellipse(DISPLAY_SURFACE, random_colour, (random_position, random_size), random_fill)

    elif random_number == 4:
        '''----POLYGON----'''
        # Calculate Parameters
        random_point_list = [( random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]) ) for x in range(10)]  #Done

        # Draw Object
        pygame.draw.polygon(DISPLAY_SURFACE, random_colour, random_point_list, 0)  # Polygons look sucky as just a line

    pygame.display.update() # Updates the display with changes.

    # Set the wait_time (after calculations have been made) (in ms, not seconds)
    # wait_time = time_single_frame_ - time_elapsed_
    wait_time = ((1 / float(FPS)) * 1000) - (pygame.time.get_ticks() - time_at_frame_start)

    pygame.time.wait(int(wait_time))  # Pause the program for the set amount of time.

    delta_time = wait_time / 1000.0  # This updates the delta time variable. (in seconds, not ms)
    #print delta_time

# Close pygame before application closes.
pygame.quit()
