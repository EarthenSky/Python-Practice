import pygame
import tile
import pygame.mouse
import ctypes  # An included library with Python install.

#initialize
#(position, size, colour)

#creates a two dimentional array of tile objects
tile_size = 40
tile_list = [[tile.tile((x* tile_size, y* tile_size), (tile_size, tile_size), (255, 255, 255)) for y in range(18)] for x in range(32)]

is_game_complete = False
is_first_game_loop = True

def game_update():
    global is_game_complete, is_first_game_loop

    #sets cursor to starting position
    if is_first_game_loop == True:
        tile_mid = [tile_position[0] + tile_size / 2, tile_position[1] + tile_size / 2]
        pygame.mouse.set_pos(tile_mid)
        is_first_game_loop = False

    #checks if cursor reaches the endpoint
    for x in range(len(tile_list)):
        for y in range(len(tile_list[x])):
            position = pygame.mouse.get_pos()
            if tile_list[x][y].is_mouse_over(position[0], position[1]) == True:
                if tile_list[x][y].m_type == tile.WALL:
                    tile_mid = [tile_position[0] + tile_size / 2, tile_position[1] + tile_size / 2]
                    pygame.mouse.set_pos(tile_mid)
                if tile_list[x][y].m_type == tile.ENDPOINT:
                    is_game_complete = True

def render(display_surface):
    #draws a x by y grid of tiles
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

#start point
tile_position = [0, 0]
def check_maze():
    global tile_position

    # a dictionary is a list that has a value assigned to a key (word - definition)
    tile_dict = {tile.WALL : 0, tile.GROUND : 0, tile.STARTPOINT : 0, tile.ENDPOINT : 0}

    #counts all the different types of tiles
    for x in range(len(tile_list)):
        for y in range(len(tile_list[x])):
            tile_dict[tile_list[x][y].m_type] += 1

            #sets position of start point
            if tile_list[x][y].m_type == tile.STARTPOINT:
                tile_position = tile_list[x][y]._position #accessing private variable

    #checks if only 1 start-point, 1 end-point or more than 1 ground exists
    if tile_dict[tile.STARTPOINT] == 1 and tile_dict[tile.ENDPOINT] == 1 and tile_dict[tile.GROUND] >= 1:
        return False #maze valid, stop buildmode
    else:
        error_string = u"Each map has to have one start-point(Blue), one end-point(Green) and " + \
                     u"more than one ground tile(Black). Your map has {}- startpoint(s), {} - endpoint(s), {}- ground tile(s)"

        ctypes.windll.user32.MessageBoxW(0, error_string.format(tile_dict[tile.STARTPOINT], tile_dict[tile.ENDPOINT], tile_dict[tile.GROUND]), u"ERROR", 0)

        return True #maze invalid, continue buildmode
