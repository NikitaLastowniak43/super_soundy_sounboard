import pygame
import sys

#colors
black = [0, 0, 0]
white = [255, 255, 255]
gray = [150,150,150]
blue = [0,0,240]


screen_size=[840,480]
pygame.init()
screen=pygame.display.set_mode(screen_size)
background_color=black
pygame.display.set_caption('super soundy soundboard')


screen_works = True
while screen_works:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            screen_works = False

    screen.fill(black)

    #commands for keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        screen_works = False
        pygame.quit()
        sys.exit()

    pygame.display.flip()

