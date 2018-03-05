import pygame
import tile

#initialize
#(position, size, colour)

#creates a two dimentional array of tile objects
tile_list = [[tile.tile((x* 40, y* 40), (40, 40), (x*8, y*8, 255)) for y in range(18)] for x in range(32)]

def update():
    pass

def render(display_surface):
    #draws a 2d array of tiles (x by y) (makes a box)
    for x in range(len(tile_list)):
        for y in range(len(tile_list[x])):
            tile_list[x][y].draw(display_surface)
