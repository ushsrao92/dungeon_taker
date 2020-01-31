import pygame
import random
import os


WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
bright_green = (0,255,0)
YELLOW = (255,255,0)


pygame.init()
pygame.mixer.init()
start_page = pygame.image.load('dungeon.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Taker")
clock = pygame.time.Clock()


def health_bars(bar_update):
    if bar_update > 75:
        player_health_color = GREEN
    elif bar_update > 45:
        player_health_color = YELLOW
    else:
        player_health_color = RED

    pygame.draw.rect(screen,player_health_color,(600,25,bar_update,25))

def bar_update():


    pygame.init()
    # set up assets folders
    game_folder = os.path.dirname(__file__)

    player_health = 10
    bar_update = 80
    # Game loop
    running = True
    while running:
        #if the loop takes less than 1/30th of a second, this keeps the rate steady
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # Checking for quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_health -= 1
                    bar_update -= 5
                    if player_health == 0:
                        return ("Game_Over")
                    

                elif event.key == pygame.K_UP:
                    player_health += 1
                    bar_update += 5
                        
        print(player_health)
        print(bar_update)
        health_bars(bar_update)
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.flip()