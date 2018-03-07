import pygame
import sys
import game_manager
pygame.init() #starts pygame
pygame.font.init()

#makes a screen of 1280 by 720
display_surface = pygame.display.set_mode( (1280, 720) )

#title on top
pygame.display.set_caption("Box")
myfont = pygame.font.SysFont('Comic Sans MS', 20)
#checks to quit build mode
is_build_mode_on = True

#check to quit application
stopped = False
while not stopped:
    #update and render function
    game_manager.update()
    game_manager.render(display_surface)

    #text box with description
    text_surface = myfont.render('Wall - white', True, (0, 0, 0))
    display_surface.blit(text_surface,(0,0))

    #input handeler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit
            stopped = True
        elif is_build_mode_on == True: #buildmode on
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:    #left click toggles wall <-> ground
                    game_manager.on_left_mouse_pressed()
                elif event.button == 3:  #right click toggles STARTPOINT <-> endpoint
                    game_manager.on_right_mouse_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  #if space pressed
                    is_build_mode_on = game_manager.check_maze()  #quit build-mode if maze is correct

        elif is_build_mode_on == False:
            pass
    pygame.display.update() #updates displays

#closes application
pygame.quit()
