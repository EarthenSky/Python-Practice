import pygame  # Import the pygame library.

# Init pygame
def init():
    pygame.init()  # Init pygame
    pygame.display.set_caption("Mai Windou")

# Init pygame
init()

# Create a game window
display_surface = pygame.display.set_mode( (300, 100) )

# Exit flag
f_done = False
while not f_done:
    # Draw things -w-
    pygame.draw.rect(display_surface, (0, 255, 255), (100, 100, 10, 50))

    # Query user input
    for event in pygame.event.get():

        # Check if the close button has been pressed
        if event.type == pygame.QUIT:
            pygame.quit();
            f_done = True;  # Set completed flag to true

    pygame.display.update()


print "PAAAIIIINNNN!!!"
