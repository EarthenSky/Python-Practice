import pygame
import random

# This is a 2d vector that holds the size of the screen.
screen_size = [1024, 768]
object_max_size = 400

# Starts pygame.
pygame.init()

# Makes a screen of 1280 by 720 and names it.
display_surface = pygame.display.set_mode( (screen_size[0], screen_size[1]) )
pygame.display.set_caption("Random Shapes")

# Helpful constants.
_fps = 240
_delta_time = 0

# Starts the game loop.
stopped = False
while not stopped:
    time_at_frame_start = pygame.time.get_ticks()  # Get time before calulations

    # Input handeler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True

    # Chooses a random shape to draw
    random_number = random.randint(1, 4)
    if random_number == 1:
        # Calculate Perameters
        random_colour = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        random_rect = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1]), random.randint(6, object_max_size), random.randint(6, object_max_size))
        random_fill = random.randint(0, 3)

        # Draw Object
        pygame.draw.rect(display_surface, random_colour, random_rect, random_fill)

    elif random_number == 2:
        # Calculate Perameters
        random_colour = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        random_position = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1]))
        random_radius = random.randint(6, object_max_size/2)  # Radius must be smaller than fill
        random_fill = random.randint(0, 3)

        # Draw Object
        pygame.draw.circle(display_surface, random_colour, random_position, random_radius, random_fill)
    elif random_number == 3:
        # Calculate Perameters
        random_colour = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        random_rect = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1]), random.randint(6, object_max_size), random.randint(6, object_max_size))
        random_fill = random.randint(0, 3)

        # Draw Object
        pygame.draw.ellipse(display_surface, random_colour, random_rect, random_fill)
    elif random_number == 4:
        # Calculate Perameters
        random_colour = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        random_point_list = [(random.randint(0, screen_size[0]), random.randint(0, screen_size[1])) for x in range(10)]  #Done
        random_fill = random.randint(0, 3)

        # Draw Object
        pygame.draw.polygon(display_surface, random_colour, random_point_list, random_fill)

    pygame.display.update() #updates the display

    # Set the wait time (after calculations have been made) (in ms not seconds)
    wait_time = ((1 / float(_fps)) * 1000) - (pygame.time.get_ticks() - time_at_frame_start)
    pygame.time.wait(int(wait_time))  # Pause the program for the set amount of time.

    _delta_time = wait_time / 1000.0  # This updates the delta time variable. (in seconds not ms)
    #print _delta_time

#closes application when done
pygame.quit()
