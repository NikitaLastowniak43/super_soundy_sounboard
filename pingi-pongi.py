import pygame
import sys
import random

clock=pygame.time.Clock()
screen_size=[840,480]
pygame.init()
screen=pygame.display.set_mode(screen_size)


black = [0, 0, 0]
white = [255, 255, 255]
gray = [150,150,150]

background_color=black
pygame.display.set_caption('pingi-pongi')

def draw_text(text,font,color,screen,x,y):
    points_text = font.render(text,True,color)
    screen.blit(points_text, [x,y])

def setting():
    return 0

def escape():
    pygame.quit()
    sys.exit()

def main_menu():
    font = pygame.font.SysFont(None, 36)
    font2 = pygame.font.SysFont(None, 52)
    font3 = pygame.font.SysFont(None, 40)
    screen_works=True
    #logic
    menu_items={'Start':game,'Settings':setting,'Escape':escape}
    while screen_works:


        screen.fill(black)

        mouse_cord=pygame.mouse.get_pos()
        y=120
        for i,item in enumerate(menu_items):
            if mouse_cord[1] < y+50*i+36/2+10 and mouse_cord[1] > y+50*i-36/2+10:
                draw_text(item, font3, gray, screen, 30, y+50*i)
            else:
                draw_text(item, font, white, screen, 30, y+50*i)

            draw_text("PINGI PONGI", font2, white, screen, 30, 50)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, item in enumerate(menu_items):
                    if mouse_cord[1] < y + 50 * i + 36 / 2 + 10 and mouse_cord[1] > y + 50 * i - 36 / 2 + 10:
                        menu_items[item]()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def game():
    font = pygame.font.SysFont(None, 30)
    # changers
    music = pygame.mixer.Sound("skibidi-toilet.mp3")
    music.play(-1)

    stick_width = 30
    stick_height = 100
    space_from_walls = 25

    first_stick_start_x_coordinate = space_from_walls
    first_stick_start_y_coordinate = screen_size[1] / 2 - stick_height / 2

    second_stick_start_x_coordinate = screen_size[0] - space_from_walls - stick_width
    second_stick_start_y_coordinate = first_stick_start_y_coordinate

    circles_x_coord = screen_size[0] / 2
    circles_y_coord = screen_size[1] / 2
    radius = 20

    speed = 5

    screen_works = True
    game_works = False

    balls_x_speed = random.choice([3, -3])

    balls_y_speed = random.choice([3, -3])

    basic_speed = balls_x_speed

    lefts_points = 0
    right_points = 0

    while screen_works:
        # logic will be here
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                screen_works = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and first_stick_start_y_coordinate > 0:
            first_stick_start_y_coordinate = first_stick_start_y_coordinate - speed

        if keys[pygame.K_s] and first_stick_start_y_coordinate < screen_size[1] - stick_height:
            first_stick_start_y_coordinate = first_stick_start_y_coordinate + speed

        if keys[pygame.K_UP] and second_stick_start_y_coordinate > 0:
            second_stick_start_y_coordinate = second_stick_start_y_coordinate - speed

        if keys[pygame.K_DOWN] and second_stick_start_y_coordinate < screen_size[1] - stick_height:
            second_stick_start_y_coordinate = second_stick_start_y_coordinate + speed

        if keys[pygame.K_f]:
            game_works = True

        if game_works == True:
            circles_x_coord = circles_x_coord + balls_x_speed
            circles_y_coord = circles_y_coord + balls_y_speed

        if circles_y_coord <= 0:
            balls_y_speed = balls_y_speed * (-1)

        if circles_y_coord >= screen_size[1] - radius:
            balls_y_speed = balls_y_speed * (-1)

        # пофіксити захват яїчками
        # за відбиття від лівої стінки
        if circles_x_coord - radius <= first_stick_start_x_coordinate + stick_width and first_stick_start_y_coordinate + stick_height > circles_y_coord - radius and first_stick_start_y_coordinate < circles_y_coord + radius:
            balls_x_speed = balls_x_speed * (-1.1)

        # за відбиття від правої стінки
        if circles_x_coord + radius >= second_stick_start_x_coordinate and second_stick_start_y_coordinate + stick_height > circles_y_coord - radius and second_stick_start_y_coordinate < circles_y_coord + radius:
            balls_x_speed = balls_x_speed * (-1.1)

        if circles_x_coord <= 0:
            right_points = right_points + 1
            circles_x_coord = screen_size[0] / 2
            circles_y_coord = screen_size[1] / 2
            balls_x_speed = basic_speed * (-1)

        if circles_x_coord >= screen_size[0]:
            lefts_points = lefts_points + 1
            circles_x_coord = screen_size[0] / 2
            circles_y_coord = screen_size[1] / 2
            balls_x_speed = basic_speed * (-1)

        # all paintings will be here

        screen.fill(black)
        pygame.draw.rect(screen, white,
                         [first_stick_start_x_coordinate, first_stick_start_y_coordinate, stick_width, stick_height])
        pygame.draw.rect(screen, white,
                         [second_stick_start_x_coordinate, second_stick_start_y_coordinate, stick_width, stick_height])
        pygame.draw.circle(screen, white, [circles_x_coord, circles_y_coord], radius)

        # виводимо рахунок
        points_text = font.render(f"{lefts_points}:{right_points}", True, white)
        screen.blit(points_text, [screen_size[0] / 2 - 12, 20])
        # flip must be the last thing in here
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main_menu()


