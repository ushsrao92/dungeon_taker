import pygame
import character
import roomLib


# Initialize pygame
pygame.init()

######################################################################
#SETTINGS
screenWidth = 800
screenHeight = 600
FPS = 30
# timeDelay = 50 DEPRECATED





#Creates window, and clock, sets Icon
screen = pygame.display.set_mode((screenWidth, screenHeight ))
pygame.display.set_caption("Dungeon Taker: OTA")
icon = pygame.image.load('images/oubliette.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

######################################################################

player = character.Character()

wallColor = (50, 50, 50)

running = True

def drawHandling():
    #this function handles the drawing in layers
    #RGB VALUES
    screen.fill((0,0,0))
    # pDraw()
    all_sprites.draw(screen)
    roomLib.drawTestRoom(screen, wallColor)


def spawn_handling():
    if player.attack == True:
        print("spawn thing now")
        attack = character.Player_Attack(player.direction, player, 10)
        all_sprites.add(attack)
        player.attack = False

# sprite groups! <3 
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Loading area for rooms
# roomLib.procRoomX()

# A state machine for managing the main game loop



while running:

    clock.tick(FPS)
    # pygame.time.delay(timeDelay) DEPRECATED

    #Update
    
    all_sprites.update()
    spawn_handling()
    running = player.game_running
    
    # Draw / render
    drawHandling()

    pygame.display.flip()

    
    

quit()