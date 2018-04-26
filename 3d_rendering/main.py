import pygame
import camera3d

# Constants
SCREEN_SIZE = [1024, 768]
FPS = 120

# Starts and sets up pygame
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("3d camera test.")

main_cam = camera3d.camera(50, SCREEN_SIZE)

# Global Variables
delta_time = 0
game_stopped = False

var = 0
X = 0
Y = 0
Z = 0

Rot = 0

# A list of points, to draw a wireframe quad.
pnt_list3d = [(40*2 - 50, 40*2 - 50, 200), (10*2 - 50, 40*2 - 50, 200), (10*2 - 50, 10*2 - 50, 200), (40*2 - 50, 10*2 - 50, 200)]

# A list of points, to draw a wireframe quad.
pnt_list3d2 = [(40*2 - 50, 40*2 - 50, 400), (10*2 - 50, 40*2 - 50, 400), (10*2 - 50, 10*2 - 50, 400), (40*2 - 50, 10*2 - 50, 400)]

# This function handles any input.  Called before update.
def handle_input():
    global game_stopped, X, Y, Z, Rot
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                Rot += 5
                main_cam.rotate((0, Rot, 0))
            elif event.key == pygame.K_e:
                Rot -= 5
                main_cam.rotate((0, Rot, 0))
            elif event.key == pygame.K_a:
                X = 1
                Y = 0
                Z = 0
            elif event.key == pygame.K_d:
                X = -1
                Y = 0
                Z = 0
            elif event.key == pygame.K_w:
                X = 0
                Y = 1
                Z = 0
            elif event.key == pygame.K_s:
                X = 0
                Y = -1
                Z = 0
            elif event.key == pygame.K_UP:
                X = 0
                Y = 0
                Z = 1
            elif event.key == pygame.K_DOWN:
                X = 0
                Y = 0
                Z = -1
            elif event.key == pygame.K_SPACE:
                X = 0
                Y = 0
                Z = 0

# This is for drawing stuff.  Called before update
def draw():
    global DISPLAY_SURFACE, main_cam

    DISPLAY_SURFACE.fill( (255, 255, 255, 255) )

    pnt_list2d = []
    for pnt3d in pnt_list3d2:
        # Make the list use screen points instead of 2d ones.
        pnt_list2d.append( main_cam.convertToScreenPoint(pnt3d, SCREEN_SIZE) )
        #print str( main_cam.convertToScreenPoint(pnt3d, SCREEN_SIZE) )

    pygame.draw.polygon(DISPLAY_SURFACE, (100, 200, 250, 255), pnt_list2d, 0)

    pnt_list2d = []
    for pnt3d in pnt_list3d:
        # Make the list use screen points instead of 2d ones.
        pnt_list2d.append( main_cam.convertToScreenPoint(pnt3d, SCREEN_SIZE) )
        #print str( main_cam.convertToScreenPoint(pnt3d, SCREEN_SIZE) )

    pygame.draw.polygon(DISPLAY_SURFACE, (250, 200, 150, 255), pnt_list2d, 0)

# This is the "do game math" function.  Put any math or functional code here.
def update():
    global var

    var += 1

    main_cam.translate( (X, Y, Z) )

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
