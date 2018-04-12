import pygame
import pyCam  # This camera module overloads the draw methods.

# Constants
SCREEN_SIZE = [1024, 768]
FPS = 60

# Starts and sets up pygame.
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Father, what is my name?!")

# Init the game's camera and hols the id
main_cam = pyCam.create_camera("main_cam", (0, 0))

# Runtime Constants
dt = 0
game_stopped = False

# This function handles any input.  Called before draw.
def handle_input():
    global game_stopped, main_cam

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True

# This is for drawing stuff.  Called before update.
def draw():
    DISPLAY_SURFACE.fill( (180, 245, 255, 255) )  # Draw ice as the background.
    pyCam.draw_rect("main_cam", DISPLAY_SURFACE, (255, 255, 255, 255), (100, 100, 100, 100))

# This is the "do game math" function.  Put any math or functional code here.
def update():
    pass

# This is the gameloop section of code.
def gameloop():
    global dt

    # This is the start of the gameloop.
    while not game_stopped:
        fs = pygame.time.get_ticks()  # Get time before calulations.

        handle_input()  # First Gameloop Stage.

        update()  # Second Gameloop Stage.

        draw() # Last Gameloop Stage.

        pygame.display.update() # Updates the display with changes.

        # wait_time = time_single_frame_ - time_elapsed_
        wait_time = ((1 / float(FPS)) * 1000) - (pygame.time.get_ticks() - fs)

        pygame.time.wait(int(wait_time))  # Pause the program for the set amount of time.

        dt = wait_time / 1000.0  # This updates the delta time variable. (in seconds, not ms)
        #print "DEBUG: dt = " + str(dt)

    # Close pygame before application closes.
    pygame.quit()

gameloop()  # This is pretty much the only instruction run in the global scope.

print "DEBUG: Application Complete."
