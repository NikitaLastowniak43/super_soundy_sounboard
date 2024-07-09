import pygame
import sys
import time


#colors
black = [0, 0, 0]
white = [255, 255, 255]
gray = [150,150,150]
back_ground = [60,100,160]


screen_size=[840,480]
pygame.init()
screen=pygame.display.set_mode(screen_size)
background_color=black
pygame.display.set_caption('super soundy soundboard')

def draw_text(text,font,color,screen,x,y):
    points_text = font.render(text,True,color)
    screen.blit(points_text, [x,y])

def Game():
    # fonts
    super_small_font = pygame.font.SysFont(None, 16)
    small_font = pygame.font.SysFont(None, 36)
    mid_font = pygame.font.SysFont(None, 52)
    large_font = pygame.font.SysFont(None, 80)
    sound_mode = 1

    screen_works = True
    while screen_works:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False

        screen.fill(back_ground)

        #texts and figures
        mouse_cord = pygame.mouse.get_pos()

        pygame.draw.polygon(screen, white, ((10, 27), (25, 12), (39, 27)))
        rect_for_house = pygame.Rect(15, 27, 20, 20)
        pygame.draw.rect(screen, white, rect_for_house)
        window_for_house = pygame.Rect(17, 31, 6, 6)
        pygame.draw.rect(screen, gray, window_for_house)
        door_for_house = pygame.Rect(25, 31, 8, 16)
        pygame.draw.rect(screen, gray, door_for_house)

        rect_for_note1 = pygame.Rect(30, 350, 80, screen_size[1]-350)
        pygame.draw.rect(screen, white, rect_for_note1)
        rect_for_note2 = pygame.Rect(130, 350, 80, screen_size[1] - 350)
        pygame.draw.rect(screen, white, rect_for_note2)
        rect_for_note3 = pygame.Rect(230, 350, 80, screen_size[1] - 350)
        pygame.draw.rect(screen, white, rect_for_note3)
        rect_for_note4 = pygame.Rect(330, 350, 80, screen_size[1] - 350)
        pygame.draw.rect(screen, white, rect_for_note4)
        rect_for_note5 = pygame.Rect(430, 350, 80, screen_size[1] - 350)
        pygame.draw.rect(screen, white, rect_for_note5)
        rect_for_note6 = pygame.Rect(530, 350, 80, screen_size[1] - 350)
        pygame.draw.rect(screen, white, rect_for_note6)
        rect_for_note7 = pygame.Rect(630, 350, 80, screen_size[1] - 350)
        pygame.draw.rect(screen, white, rect_for_note7)
        rect_for_note8 = pygame.Rect(730, 350, 80, screen_size[1] - 350)
        pygame.draw.rect(screen, white, rect_for_note8)

        #interactions
        if mouse_cord[0] > 12 and mouse_cord[0] < 41:
            if mouse_cord[1] > 10 and mouse_cord[1] < 47:
                pygame.draw.polygon(screen, gray, ((10, 27), (25, 12), (39, 27)))
                pygame.draw.rect(screen, gray, rect_for_house)
                pygame.draw.rect(screen, black, window_for_house)
                pygame.draw.rect(screen, black, door_for_house)
                if pygame.mouse.get_pressed()[0]:
                    screen_works = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LALT]:
            if sound_mode == 3:
                sound_mode = 1
            else:
                sound_mode = sound_mode + 1

        if keys[pygame.K_1]:
            sound_mode = 1

        if keys[pygame.K_2]:
            sound_mode = 2

        if keys[pygame.K_3]:
            sound_mode = 3

        if sound_mode == 1:
            draw_text("Guitar mode", mid_font, white, screen, 320, 300)
        elif sound_mode == 2:
            draw_text("Piano mode", mid_font, white, screen, 320, 300)
        else:
            draw_text("Drum mode", mid_font, white, screen, 320, 300)

        if keys[pygame.K_a]:
            pygame.draw.rect(screen, gray, rect_for_note1)
            if sound_mode == 1:
                note1 = pygame.mixer.Sound("slap_bass1.mp3")
                note1.play()
            elif sound_mode == 2:
                note1 = pygame.mixer.Sound("piano1.mp3")
                note1.play()
            elif sound_mode == 3:
                note1 = pygame.mixer.Sound("drum1.mp3")
                note1.play()

        if keys[pygame.K_s]:
            pygame.draw.rect(screen, gray, rect_for_note2)
            if sound_mode == 1:
                note2 = pygame.mixer.Sound("slap_bass2.mp3")
                note2.play()
            elif sound_mode == 2:
                note2 = pygame.mixer.Sound("piano2.mp3")
                note2.play()
            elif sound_mode == 3:
                note2 = pygame.mixer.Sound("drum2.mp3")
                note2.play()

        if keys[pygame.K_d]:
            pygame.draw.rect(screen, gray, rect_for_note3)
            if sound_mode == 1:
                note3 = pygame.mixer.Sound("slap_bass3.mp3")
                note3.play()
            elif sound_mode == 2:
                note3 = pygame.mixer.Sound("piano3.mp3")
                note3.play()
            elif sound_mode == 3:
                note3 = pygame.mixer.Sound("drum3.mp3")
                note3.play()

        if keys[pygame.K_f]:
            pygame.draw.rect(screen, gray, rect_for_note4)
            if sound_mode == 1:
                note4 = pygame.mixer.Sound("slap_bass4.mp3")
                note4.play()
            elif sound_mode == 2:
                note4 = pygame.mixer.Sound("piano4.mp3")
                note4.play()
            elif sound_mode == 3:
                note4 = pygame.mixer.Sound("drum4.mp3")
                note4.play()

        if keys[pygame.K_g]:
            pygame.draw.rect(screen, gray, rect_for_note5)
            if sound_mode == 1:
                note5 = pygame.mixer.Sound("slap_bass5.mp3")
                note5.play()
            elif sound_mode == 2:
                note5 = pygame.mixer.Sound("piano5.mp3")
                note5.play()
            elif sound_mode == 3:
                note5 = pygame.mixer.Sound("drum5.mp3")
                note5.play()

        if keys[pygame.K_h]:
            pygame.draw.rect(screen, gray, rect_for_note6)
            if sound_mode == 1:
                note6 = pygame.mixer.Sound("slap_bass6.mp3")
                note6.play()
            elif sound_mode == 2:
                note6 = pygame.mixer.Sound("piano6.mp3")
                note6.play()
            elif sound_mode == 3:
                note6 = pygame.mixer.Sound("drum6.mp3")
                note6.play()

        if keys[pygame.K_j]:
            pygame.draw.rect(screen, gray, rect_for_note7)
            if sound_mode == 1:
                note7 = pygame.mixer.Sound("slap_bass7.mp3")
                note7.play()
            elif sound_mode == 2:
                note7 = pygame.mixer.Sound("piano7.mp3")
                note7.play()
            elif sound_mode == 3:
                note7 = pygame.mixer.Sound("drum7.mp3")
                note7.play()

        if keys[pygame.K_k]:
            pygame.draw.rect(screen, gray, rect_for_note8)
            if sound_mode == 1:
                note8 = pygame.mixer.Sound("slap_bass8.mp3")
                note8.play()
            elif sound_mode == 2:
                note8 = pygame.mixer.Sound("piano8.mp3")
                note8.play()
            elif sound_mode == 3:
                note8 = pygame.mixer.Sound("drum8.mp3")
                note8.play()

        if keys[pygame.K_ESCAPE]:
            screen_works = False

        pygame.display.flip()

def Menu():
    #fonts
    super_small_font = pygame.font.SysFont(None, 16)
    small_font = pygame.font.SysFont(None, 36)
    mid_font = pygame.font.SysFont(None, 52)
    large_font = pygame.font.SysFont(None, 80)

    screen_works = True
    while screen_works:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False

        screen.fill(back_ground)

        #texts, buttons and figures
        mouse_cord = pygame.mouse.get_pos()

        frame_for_name = pygame.Rect(10, 40, 600, 50)
        pygame.draw.rect(screen, white, frame_for_name, 2)
        draw_text("Super Soundy Soundboard", mid_font, white, screen, 30, 50)
        draw_text("totaly NOT a button", super_small_font, white, screen, 490, 68)


        frame_for_start_button = pygame.Rect(10, 155, 170, 60)
        pygame.draw.rect(screen, white, frame_for_start_button, 2)
        draw_text("Start", large_font, white, screen, 30, 160)

        #interaction with menu NOT button
        if mouse_cord[0] > 50 and mouse_cord[0] < 500:
            if mouse_cord[1] > 50 and mouse_cord[1] < 80:
                if pygame.mouse.get_pressed()[0]:
                    draw_text("Super Soundy Soundboard", mid_font, gray, screen, 30, 50)
                    secret = pygame.mixer.Sound("fart-83471.mp3")
                    secret.play()

        #interaction with start button
        if mouse_cord[0] > 10 and mouse_cord[0] < 180:
            if mouse_cord[1] > 148 and mouse_cord[1] < 220:
                pygame.draw.rect(screen, gray, frame_for_start_button, 2)
                draw_text("Start", large_font, gray, screen, 30, 160)
                if pygame.mouse.get_pressed()[0]:
                    Game()

        #if keys are pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            screen_works = False
            pygame.quit()
            sys.exit()

        pygame.display.flip()

Menu()

