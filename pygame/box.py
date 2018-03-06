import pygame
import game_manager
pygame.init() #starts pygame

#makes a screen of 1280 by 720
display_surface = pygame.display.set_mode( (1280, 720) )

#title on top
pygame.display.set_caption("Box")

#check to quit application
stopped = False
while not stopped:
    #update and render function
    game_manager.update()
    game_manager.render(display_surface)

    #input handeler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game_manager.on_left_mouse_pressed()
            elif event.button == 3:
                game_manager.on_right_mouse_pressed()
    pygame.display.update() #updates displays

#closes application
pygame.quit()
