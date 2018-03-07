import pygame
import tile
import pygame.mouse
import ctypes  # An included library with Python install.

#initialize
#(position, size, colour)

#creates a two dimentional array of tile objects
tile_list = [[tile.tile((x* 40, y* 40), (40, 40), (255, 255, 255)) for y in range(18)] for x in range(32)]


def update():
    pass

def render(display_surface):
    #draws a 2d array of tiles (x by y) (makes a box)
    for x in range(len(tile_list)):
        for y in range(len(tile_list[x])):
            tile_list[x][y].draw(display_surface)

#checks mouse position (left click) to toggle wall - ground
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

#checks mouse position (right click) to toggle STARTPOINT <-> endpoint
def on_right_mouse_pressed():
        for x in range(len(tile_list)):
            for y in range(len(tile_list[x])):
                position = pygame.mouse.get_pos()
                #toggles tile type on click (STARTPOINT <-> endpoint)
                if tile_list[x][y].is_mouse_over(position[0], position[1]) == True:
                    if tile_list[x][y].m_type == tile.ENDPOINT:
                        tile_list[x][y].set_tile_type(tile.STARTPOINT)
                    else:
                        tile_list[x][y].set_tile_type(tile.ENDPOINT)

def check_maze():
    # a dictionary is a list that has a value assigned to a key
    tile_dict = {tile.WALL : 0, tile.GROUND : 0, tile.STARTPOINT : 0, tile.ENDPOINT : 0}

    #loops thru all the tiles
    for x in range(len(tile_list)):
        for y in range(len(tile_list[x])):
            tile_dict[tile_list[x][y].m_type] += 1

    #checks if only 1 start-point, end-point or more than 1 ground exists
    if tile_dict[tile.STARTPOINT] == 1 and tile_dict[tile.ENDPOINT] == 1 and tile_dict[tile.GROUND] >= 1:
        return False #maze valid, stop buildmode
    else:
        ctypes.windll.user32.MessageBoxW(0, u"Each map has to have one start-point(Blue), one end-point(Green)and more than one ground tile(Black). \nYour map has {}- startpoint(s), {} - endpoint(s), {}- ground tile(s)".format(tile_dict[tile.STARTPOINT], tile_dict[tile.ENDPOINT], tile_dict[tile.GROUND]), u"ERROR", 0)

        return True #maze invalid, continue buildmode
