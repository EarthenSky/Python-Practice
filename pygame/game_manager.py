import pygame
import tile
import pygame.mouse
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

def on_left_mouse_pressed():
    for x in range(len(tile_list)):
        for y in range(len(tile_list[x])):
            position = pygame.mouse.get_pos()
            #toggles tile type on click (wall <-> ground)
            if tile_list[x][y].is_mouse_over(position[0], position[1]) == True:
                if tile_list[x][y].m_type == tile.WALL:
                    tile_list[x][y].set_tile_type(tile.GROUND)
                else:
                    tile_list[x][y].set_tile_type(tile.WALL)

def on_right_mouse_pressed():
        for x in range(len(tile_list)):
            for y in range(len(tile_list[x])):
                position = pygame.mouse.get_pos()
                #toggles tile type on click (wall <-> ground)
                if tile_list[x][y].is_mouse_over(position[0], position[1]) == True:
                    if tile_list[x][y].m_type == tile.ENDPOINT:
                        tile_list[x][y].set_tile_type(tile.PLAYER)
                    else:
                        tile_list[x][y].set_tile_type(tile.ENDPOINT)
