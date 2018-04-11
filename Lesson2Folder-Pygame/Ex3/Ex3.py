import pygame
import Ex3Objects  # Import object classes.
import ctypes

# Constants.
SCREEN_SIZE = [512, 768]
FPS = 60  # Keep at >= 60 fps, cause input handling.

# Starts and sets up pygame
pygame.init()
pygame.mixer.pre_init(44000, -16, 2, 2048)  # Setup mixer to avoid sound lag.
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Ice Game")

# Runtime constants.
dt = 0.0
game_stopped = False

# Instantiate the player class and all the obstacles.
player = Ex3Objects.player( [(SCREEN_SIZE[0]/2), SCREEN_SIZE[1] / 8] )
obstacles = []
obstacles.append(Ex3Objects.enemy( (100, 300 + 70*0) ))
obstacles.append(Ex3Objects.enemy( (450, 300 + 70*1) ))
obstacles.append(Ex3Objects.enemy( (217, 300 + 70*2) ))
obstacles.append(Ex3Objects.enemy( (485, 300 + 70*3) ))
obstacles.append(Ex3Objects.enemy( (302, 300 + 70*4) ))
obstacles.append(Ex3Objects.enemy( (10, 300 + 70*4) ))

# This function handles any input.  Called before update.
def handle_input():
    global game_stopped

    # Query events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True

        # Handle player input.
        player.handle_input(event);

# This is for drawing stuff.  Called before update
def draw():
    DISPLAY_SURFACE.fill( (180, 245, 255, 255) )  # Draw ice as the background.

    # Draw the endzone.
    pygame.draw.rect(DISPLAY_SURFACE, (255, 180, 150, 255), (0, 650 + 64, SCREEN_SIZE[0],100))

    player.draw(DISPLAY_SURFACE)  # Pass the display surface to the player.

    # Draw all obstacle objects
    for obstacle in obstacles:
        obstacle.draw(DISPLAY_SURFACE)

# This is the "do game math" function.  Put any math or functional code here.
def update():
    global game_stopped

    player.update(dt)  # Pass delta time to the player.

    # Update all obstacle objects and check collision with player
    for obstacle in obstacles:
        obstacle.update(dt)
        game_stopped = obstacle.check_player_collision(player.get_position(), player.get_size())

        # This prevents the game from saying you lose more times if you hit
        # multiple spike balls at the same time and end the function right away.
        if game_stopped:
            return

    # Check if player wins and send message if they have.
    if player.get_position()[1] > 690:
        message_string = u"YOU WIN ENTIRE GAME!"
        ctypes.windll.user32.MessageBoxW(0, message_string, u"CONGLAGURATION!", 0)

        game_stopped = True  # Close the game.

# This is the gameloop section of code.
def gameloop():
    global dt
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

        dt = wait_time / 1000.0  # This updates the delta time variable. (in seconds, not ms)
        #print "DEBUG: dt = " + str(dt)

    # Close pygame before application closes.
    pygame.quit()

gameloop()  # Start gameloop.  # This is pretty much the only instruction run in the global scope.

print "DEBUG: Application Complete."
