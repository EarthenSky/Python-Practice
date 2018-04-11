# This template is built to make the user no longer need to work with the
# "while loop" that runs pygame when building something simple.
# This template is also made to include a frame independent movement constant,
# as well as some other useful prebuilt code.

import pygame

# This is a 2d vector that holds the size of the screen.
SCREEN_SIZE = [1024, 768]

# Sets the prefered fps.  Mostly affects the speed of the main gameloop,
# although complex calculations may cause the fps to drop.
# Use delta_time to link movement to frame change speed.
FPS = 60

# Starts and sets up pygame
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Father, what is my name?!")

# Runtime constant used to modify movement. (More like readonly.)
# Delta time is set to the change in time after each frame.
# Multiply any movement by this to make it frame indepentent.
# Delta time will be roughly less than 1/FPS (if FPS == 60, then ~< 0.0166666...)
delta_time = 0

# This is the flag that controls ending the game.
game_stopped = False

# This function handles any input.  Called before update.
def handle_input():
    global game_stopped
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True

# This is for drawing stuff.  Called before update
def draw():
    pass

# This is the "do game math" function.  Put any math or functional code here.
# Called after handle_input.  This function is updated FPS times per second.
# Remember to define any outside defined, non-constant varaibles as "global"
def update():
    #ex.
    #global my_var_non_const
    #my_var_non_const += 1
    #print str(my_var_non_const)
    pass

# This is the gameloop section of code.
# This template is designed so that you don't need to interact with
# this function / section of the code.
def gameloop():
    global delta_time

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

gameloop()  # This is pretty much the only instruction run in the global scope.

print "DEBUG: Application Complete."
