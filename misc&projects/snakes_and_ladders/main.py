import pygame, classes

#
SCREEN_SIZE = [1024, 768]
FPS = 120

# Starts and sets up pygame
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Father, what is my name?!")

# Globals
delta_time = 0
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
def update():
    pass

# This is the gameloop section of code.
def gameloop():
    global delta_time

    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    delta_time = framerate_clock.tick(FPS) / 1000.0

    # This is the start of the gameloop.
    while not game_stopped:
        handle_input()  # First Gameloop Stage.

        update()  # Second Gameloop Stage.

        draw() # Last Gameloop Stage.

        pygame.display.update() # Updates the display with changes.

        # Pause pygame and calculate delta time.
        delta_time = framerate_clock.tick(FPS) / 1000.0
        #print "DEBUG: delta_time = " + str(delta_time) + ", fps -> " + str( framerate_clock.get_fps() )

    # Close pygame before application closes.
    pygame.quit()

gameloop()  # This is pretty much the only instruction run in the global scope.

print "DEBUG: Application Complete."
