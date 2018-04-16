# This module acts as a camera and interfaces the pygame draw functions.
import pygame

# Sets up the camera dictionary.
_camera_dict = {}

# This is the camera class.
class camera:
    """This is a camera.  You can change it's position.  Using camera like a
        string will return the id value."""

    # Init camera, id can be int or string.
    def __init__(self, id, pos):
        self._id = id
        self._pos = pos

    # Using a camera like a string will output it's id value.
    def __str__(self):
        return self._id

    # Get the id value, (can be str or int.)
    def get_id(self):
        return self._id

    # Set the camera's position.
    def get_position(self):
        return self._pos

    # Set the camera's position.
    def set_position(self, pos):
        self._pos = pos

# Instantiates a camera object.
def create_camera(id, pos):
    """This function creates a camera object. Please pass a unique id to
    specify a camera to draw from.  Returns the passed id."""
    _camera_dict[id] = camera(id, pos)

    return id

def get_camera(id):
    """This function returns a camera object based on it's id."""
    return _camera_dict[id]

def draw_rect(camera_id, surface, colour, rect, width=0):
    """Blits a rectangle into specified rectangle.  Width 0 makes the rect filled."""
    pygame.draw.rect(surface, colour, (rect[0] - _camera_dict[camera_id].get_position()[0], rect[1] - _camera_dict[camera_id].get_position()[1], rect[2], rect[3]), width)

def draw_img(camera_id, surface, img, pos, cut_area=None):
    """Blits an image to a surface at the top left position.  The rectangle parameter is structured like -> (x, y, width, height)"""
    surface.blit(img, (pos[0] - _camera_dict[camera_id].get_position()[0], pos[1] - _camera_dict[camera_id].get_position()[1]))


"""
# Some Basic camera controlls...
elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_w:
        pyCam.get_camera(main_cam).set_position( (pyCam.get_camera(main_cam).get_position()[0], pyCam.get_camera(main_cam).get_position()[1] + 10) )
    elif event.key == pygame.K_s:
        pyCam.get_camera(main_cam).set_position( (pyCam.get_camera(main_cam).get_position()[0], pyCam.get_camera(main_cam).get_position()[1] - 10) )
    elif event.key == pygame.K_a:
        pyCam.get_camera(main_cam).set_position( (pyCam.get_camera(main_cam).get_position()[0] - 10, pyCam.get_camera(main_cam).get_position()[1]) )
    elif event.key == pygame.K_d:
        pyCam.get_camera(main_cam).set_position( (pyCam.get_camera(main_cam).get_position()[0] + 10, pyCam.get_camera(main_cam).get_position()[1]) )
"""
