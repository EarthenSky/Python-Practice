import pygame
import tile

#initialize
x = tile.tile((0, 0), (20, 20), (0, 0, 255))

def update():
    pass

def render(display_surface):
    x.draw(display_surface)
