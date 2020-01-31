# Pygame template - skeleton for a new pygame project
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
aegean = (70,143,162)


pygame.init()
pygame.mixer.init()
start_page = pygame.image.load('dungeon.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Taker Start")
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, aegean)
    return textSurface, textSurface.get_rect()

def text_object2(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()



def button(msg,x,y,w,h,ic,ac,action = None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                return("main")
            elif action=="quit":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    smalltext = pygame.font.Font('freesansbold.ttf',20)
    textsurf,textrect = text_object2(msg,smalltext)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(textsurf,textrect)



def game_over_screen():


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

        screen.fill(BLACK)
        largetext = pygame.font.Font('freesansbold.ttf',80)
        TextSurf,TextRect = text_objects("Game Over!",largetext)
        TextRect.center = (400,250)
        screen.blit(TextSurf,TextRect)
        x = button("RETRY",250,380,100,50,GREEN,bright_green,"play")
        if x== "main":
            return ("main")
        
        button("QUIT",450,380,100,50,GREEN,bright_green,"quit")
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.flip()