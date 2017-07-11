#import pygame for gfx
import pygame


#Setup Global Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0,0,200)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FPS = 30


#init pygame
pygame.init()


#Show Game Window
SCREEN = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

#title the window
pygame.display.set_caption('TICK-TAC-TOE')

#create a clock to control FPS
clock = pygame.time.Clock()


#main Game Loop
def mainLoop():
    game_running = True

    while game_running:
        #get Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        #update and refresh screen        
        SCREEN.fill(WHITE)

        #draw board
        pygame.draw.line(SCREEN, BLACK, (DISPLAY_WIDTH/5,DISPLAY_HEIGHT/5), (DISPLAY_WIDTH/5,DISPLAY_HEIGHT - DISPLAY_HEIGHT/5), 5)
        pygame.draw.line(SCREEN, BLACK, (DISPLAY_WIDTH/5 * 2,DISPLAY_HEIGHT/5), (DISPLAY_WIDTH/5 * 2,DISPLAY_HEIGHT - DISPLAY_HEIGHT/5), 5)
        pygame.draw.line(SCREEN, BLACK, (DISPLAY_WIDTH/10,DISPLAY_HEIGHT/5 * 2), (DISPLAY_WIDTH/10 * 4,DISPLAY_HEIGHT/5 * 2), 5)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

mainLoop()
