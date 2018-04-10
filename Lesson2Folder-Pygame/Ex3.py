import pygame

# Constants.
SCREEN_SIZE = [512, 768]
FPS = 60

pygame.init()  # Start pygame.

# Makes a screen, size by screen_size and names it.
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Random Shapes")

# Init image constants
PLAYER_IMG = pygame.image.load("red-char.png").convert_alpha()
ENEMY_IMG = pygame.image.load("SpikeBall.png").convert_alpha()

# Runtime constants.
delta_time = 0
game_stopped = False

# Keys that are down.
is_w_key_down = False
is_a_key_down = False
is_s_key_down = False
is_d_key_down = False

# This function handles any input.  Called before update.
def handle_input():
    global game_stopped

    # Query events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                is_w_key_down = True
            elif event.key == pygame.K_a:
                is_a_key_down = True
            elif event.key == pygame.K_s:
                is_s_key_down = True
            elif event.key == pygame.K_d:
                is_d_key_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                is_w_key_down = False
            elif event.key == pygame.K_a:
                is_a_key_down = False
            elif event.key == pygame.K_s:
                is_s_key_down = False
            elif event.key == pygame.K_d:
                is_d_key_down = False

# This is for drawing stuff.  Called before update
def draw():
    DISPLAY_SURFACE.fill( (180, 245, 255, 255) )  # Draw ice as the background.
    #DISPLAY_SURFACE.blit(myimage, imagerect)

# This is the "do game math" function.  Put any math or functional code here.
def update():
    pass

# This is the gameloop section of code.
def gameloop():
    # This is the start of the gameloop.
    while not game_stopped:
        time_at_frame_start = pygame.time.get_ticks()  # Get time before calulations.

        handle_input()  # First Gameloop Stage.

        update()  # Second Gameloop Stage.

        draw() # Lasp Gameloop Stage.

        pygame.display.update() # Updates the display with changes.

        # Set the wait_time (after calculations have been made) (in ms, not seconds)
        # wait_time = time_single_frame_ - time_elapsed_
        wait_time = ((1 / float(FPS)) * 1000) - (pygame.time.get_ticks() - time_at_frame_start)

        pygame.time.wait(int(wait_time))  # Pause the program for the set amount of time.

        delta_time = wait_time / 1000.0  # This updates the delta time variable. (in seconds, not ms)
        #print "DEBUG: delta_time = " + str(delta_time)

    # Close pygame before application closes.
    pygame.quit()

gameloop()  # Start gameloop.  # This is pretty much the only instruction run in the global scope.

print "DEBUG: Application Complete."
