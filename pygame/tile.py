import pygame
# single tile (blocks / background)
class tile:
    #creates objects variables
    def __init__ (self, position, size, colour):
        self._position = position
        self._size = size
        self._colour = colour

    # outputs the rectangles
    def draw (self, display_surface):
        pygame.draw.rect(display_surface, self._colour, (self._position + self._size))
