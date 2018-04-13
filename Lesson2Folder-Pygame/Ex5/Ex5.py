import pygame
import pyCam  # This camera module overloads the pygame draw methods.
import Ex5Objects

# Constants
SCREEN_SIZE = [1024, 768]
FPS = 60

# Starts and sets up pygame.
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("Father, what is my name?!")

# Init the game's camera and hols the id
main_cam = pyCam.create_camera("main_cam", [0, 0])

# Instantiate Objects.
scene = Ex5Objects.scene((int(4096), int(4096)), (0, 0))
car = Ex5Objects.car((128, 64), (200, 800))

# Runtime Constants
dt = 0
game_stopped = False

# This function handles any input.  Called before draw.
def handle_input():
    global game_stopped, main_cam, DISPLAY_SURFACE, SCREEN_SIZE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True
        elif event.type == pygame.VIDEORESIZE:
            # This makes the game window resizable.
            SCREEN_SIZE = event.size
            DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
        elif car.check_input(event) == True:
            pass  # Check_input will return false if it did nothing and check the next item.

# This is for drawing stuff.  Called before update.
def draw():
    DISPLAY_SURFACE.fill( (0, 0, 0, 0) )  # Draw the background.

    scene.draw(DISPLAY_SURFACE)
    car.draw(DISPLAY_SURFACE)

# This is the "do game math" function.  Put any math or functional code here.
def update():
    car.update(dt)

    # Calculate the car's centre position then set the camera to it.
    car_center_position = (car.get_position()[0] - SCREEN_SIZE[0]/2, car.get_position()[1] - SCREEN_SIZE[1]/2)
    pyCam.get_camera(main_cam).set_position(car_center_position)

# This is the gameloop section of code.
def gameloop():
    global dt

    clock = pygame.time.Clock()

    # This is the start of the gameloop.
    while not game_stopped:
        fs = pygame.time.get_ticks()  # Get time before calulations.

        handle_input()  # First Gameloop Stage.

        update()  # Second Gameloop Stage.

        draw() # Last Gameloop Stage.

        pygame.display.update() # Updates the display with changes.

        # wait_time = time_single_frame_ - time_elapsed_
        wait_time = ((1 / float(FPS)) * 1000) - (pygame.time.get_ticks() - fs)
        #print "DEBUG: frame_lag = " + str( (1 / float(FPS)) * 1000 ) + " .. " + str( (pygame.time.get_ticks() - fs) )

        pygame.time.wait(wait_time)  # Pause the program for the set amount of time.

        dt = ( wait_time + (pygame.time.get_ticks() - fs) ) / 1000.0  # This updates the delta time variable. (in seconds, not ms)
        #print "DEBUG: dt = " + str(dt)

        '''

        # wait_time = time_single_frame_ - time_elapsed_
        time_elapsed = pygame.time.get_ticks() - fs
        wait_time = ((1 / float(FPS)) * 1000) - (time_elapsed)
        dt = ( wait_time + (time_elapsed) ) / 1000.0  # This updates the delta time variable. (in seconds, not ms)
        print "DEBUG: dt = " + str(dt)

        clock.tick(FPS)  # Set fps.
        print "DEBUG: fps -> " + str(clock.get_fps())
        '''

    # Close pygame before application closes.
    pygame.quit()

gameloop()  # This is pretty much the only instruction run in the global scope.

print "DEBUG: Application Complete."
