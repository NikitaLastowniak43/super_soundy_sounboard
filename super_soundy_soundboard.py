import pygame
import sys
import time


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

def draw_text(text,font,color,screen,x,y):
    points_text = font.render(text,True,color)
    screen.blit(points_text, [x,y])


def Menu():
    #fonts
    super_small_font = pygame.font.SysFont(None, 16)
    small_font = pygame.font.SysFont(None, 36)
    mid_font = pygame.font.SysFont(None, 52)
    large_font = pygame.font.SysFont(None, 40)

    screen_works = True
    while screen_works:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False

        screen.fill(black)

        #texts and buttons
        mouse_cord = pygame.mouse.get_pos()
        draw_text("Super Soundy Soundboard", mid_font, white, screen, 30, 50)
        draw_text("totaly NOT a button", super_small_font,white,screen,490, 68)

        if mouse_cord[0] > 50 and mouse_cord[0] < 500:
            if mouse_cord[1] > 50 and mouse_cord[1] < 80:
                if pygame.mouse.get_pressed()[0]:
                    draw_text("Super Soundy Soundboard", mid_font, gray, screen, 30, 50)
                    secret = pygame.mixer.Sound("fart-83471.mp3")
                    secret.play()
                    # time.sleep(100)
                    # secret.stop()

        #commands for keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            screen_works = False
            pygame.quit()
            sys.exit()

        pygame.display.flip()

Menu()