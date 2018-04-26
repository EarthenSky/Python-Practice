import pygame

#different tile configurations
WALL = 1
GROUND = 2
STARTPOINT = 3
ENDPOINT = 4

# single tile (blocks / background)
class tile:
    #creates objects variables
    def __init__ (self, position, size, colour):
        self._position = position
        self._size = size
        self._colour = colour
        self.m_type = WALL  #every tile is defult to wall

    # outputs the rectangles
    def draw (self, display_surface):
        pygame.draw.rect(display_surface, self._colour, (self._position + self._size))

    #checks if mouse is overtop of object
    def is_mouse_over (self, mouse_x, mouse_y):
        #assigning border variables
        top = self._position[1]
        bottom = self._position[1] + self._size[1]
        left = self._position[0]
        right = self._position[0] + self._size[0]

        #checks if mouse is inside of rectangle
        if mouse_x >= left and mouse_x < right \
        and mouse_y >= top and mouse_y < bottom:
            return True
        else:
            return False

    def set_tile_type(self, tile_type):
        if tile_type == WALL: #white
            self._colour = (255, 255, 255)
        elif tile_type == GROUND: #black
            self._colour = (0, 0, 0)
        elif tile_type == STARTPOINT: #blue
            self._colour = (0, 100, 255)
        elif tile_type == ENDPOINT: #green
            self._colour = (0, 255, 100)

        self.m_type = tile_type
