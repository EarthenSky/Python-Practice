import pygame
import pyCam  # This camera module overloads the pygame draw methods.
import Ex5Objects

# Constants
SCREEN_SIZE = [1024, 768]
FPS = 120

# Starts and sets up pygame.dd
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("Car driving game.")

# Init the game's camera and hold the id.
main_cam = pyCam.create_camera("main_cam", [0, 0])

# Init the ui object.
ui = Ex5Objects.ui()

# Instantiate Objects.
scene = Ex5Objects.scene((int(4096), int(4096)), (0, 0))
car = Ex5Objects.car((128, 64), (150, 1900))

# Runtime Constants
dt = 0
game_stopped = False

# This function handles any input.  Called before draw.
def handle_input():
    global game_stopped, DISPLAY_SURFACE, SCREEN_SIZE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True
        elif event.type == pygame.VIDEORESIZE:
            # This makes the game window resizable.
            SCREEN_SIZE = event.size
            DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE | pygame.DOUBLEBUF)
        elif car.check_input(event) == True:
            pass  # Check_input will return false if it did nothing and check the next item.

# This is for drawing stuff.  Called before update.
def draw():
    DISPLAY_SURFACE.fill( (0, 0, 0) )  # Draw the background.

    scene.draw(DISPLAY_SURFACE)
    car.draw(DISPLAY_SURFACE)

    ui.draw(DISPLAY_SURFACE)  # Draw ui over everything.

# This is the "do game math" function.  Put any math or functional code here.
def update():
    car.update(dt, DISPLAY_SURFACE)

    ui.update(car.get_speed())

    # Calculate the car's centre position then set the camera to it.
    car_center_position = (car.get_position()[0] - SCREEN_SIZE[0]/2, car.get_position()[1] - SCREEN_SIZE[1]/2)
    pyCam.get_camera(main_cam).set_position(car_center_position)

# This is the gameloop section of code.
def gameloop():
    global dt

    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    dt = framerate_clock.tick(FPS) / 1000.0

    # This is the start of the gameloop.
    while not game_stopped:
        handle_input()  # First Gameloop Stage.

        update()  # Second Gameloop Stage.

        draw() # Last Gameloop Stage.

        pygame.display.update() # Updates the display with changes.

        # Pause pygame and calculate delta time.
        dt = framerate_clock.tick(FPS) / 1000.0
        print "DEBUG: dt = " + str(dt) + ", fps -> " + str( framerate_clock.get_fps() )


    # Close pygame before application closes.
    pygame.quit()

gameloop()  # This is pretty much the only instruction run in the global scope.

print "DEBUG: Application Complete."
