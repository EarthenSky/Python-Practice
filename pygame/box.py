import pygame
import sys
import game_manager
import ctypes
pygame.init() #starts pygame
pygame.font.init()

#makes a screen of 1280 by 720
display_surface = pygame.display.set_mode( (1280, 720) )

#title on top
pygame.display.set_caption("Maze")
myfont = pygame.font.SysFont('Comic Sans MS', 18)

#checks to quit build mode
is_build_mode_on = True

#check to quit application
stopped = False
while not stopped:
    #updates game logic
    if is_build_mode_on == False:
        game_manager.game_update()

        #if mouse reaches endpoint, go back to buildmode
        if game_manager.is_game_complete == True:
            is_build_mode_on = True
            #when cursor reaches enpoint, is_game_complete is equal True, resets
            game_manager.is_game_complete = False
            game_manager.is_first_game_loop = True #sets the cursor to startpoint
            ctypes.windll.user32.MessageBoxW(0, u"You Win", u"Congratz", 0)

    #this renders tile images
    game_manager.render(display_surface)

    #text box describing tiles on display
    text_surface_top = myfont.render("Wall - White | Ground - Black ", True, (0, 0, 0))
    text_surface_bot = myfont.render("Startpoint - Blue | Endpoint - Green", True, (0, 0, 0))
    display_surface.blit(text_surface_top,(0,0))
    display_surface.blit(text_surface_bot,(0,22))

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  #if space pressed
                    is_build_mode_on = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stopped = True

    pygame.display.update() #updates displays

#closes application
pygame.quit()
