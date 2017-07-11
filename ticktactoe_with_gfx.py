#import pygame for gfx
import pygame
import random

#Setup Global Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0,0,200)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FPS = 30

BOX1 = pygame.Rect(230,120,110,120)
BOX2 = pygame.Rect(340,120,110,120)
BOX3 = pygame.Rect(460,120,110,120)
BOX4 = pygame.Rect(230,240,110,120)
BOX5 = pygame.Rect(340,240,110,120)
BOX6 = pygame.Rect(460,240,110,120)
BOX7 = pygame.Rect(230,360,110,120)
BOX8 = pygame.Rect(340,360,110,120)
BOX9 = pygame.Rect(460,360,110,120)

#init pygame
pygame.init()

#Show Game Window
SCREEN = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

#title the window
pygame.display.set_caption('TICK-TAC-TOE')

#create a clock to control FPS
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32) 

def drawX(box):
    pygame.draw.line(SCREEN, GREEN, (box.topleft),(box.bottomright),4)
    pygame.draw.line(SCREEN, GREEN, (box.topright),(box.bottomleft),4)

def drawO(box):
    pygame.draw.ellipse(SCREEN, RED, box, 4)

#main Game Loop
def mainLoop():
    board = [
        0,0,0,
        0,0,0,
        0,0,0
    ]

    def computerChoose():
        ai = random.randrange(0,3)

        if ai % 3 == 0:
            if(
            board[1] == 1 and board[2] == 1 and board[0] == 0 or
            board[3] == 1 and board[6] == 1 and board[0] == 0 or
            board[1] == 2 and board[2] == 2 and board[0] == 0 or
            board[3] == 2 and board[6] == 2 and board[0] == 0 or
            board[4] == 1 and board[8] == 1 and board[0] == 0 or
            board[4] == 2 and board[8] == 2 and board[0] == 0):
                choice = 0
            elif(
            board[0] == 1 and board[2] == 1 and board[1] == 0 or
            board[4] == 1 and board[7] == 1 and board[1] == 0 or
            board[0] == 2 and board[2] == 2 and board[1] == 0 or
            board[4] == 2 and board[7] == 2 and board[1] == 0):
                choice = 1
            elif(
            board[0] == 1 and board[1] == 1 and board[2] == 0 or
            board[5] == 1 and board[8] == 1 and board[2] == 0 or
            board[0] == 2 and board[1] == 2 and board[2] == 0 or
            board[5] == 2 and board[8] == 2 and board[2] == 0 or
            board[4] == 1 and board[6] == 1 and board[2] == 0 or
            board[4] == 2 and board[6] == 2 and board[2] == 0):
                choice = 2
            elif(
            board[0] == 1 and board[6] == 1 and board[3] == 0 or
            board[4] == 1 and board[5] == 1 and board[3] == 0 or
            board[0] == 2 and board[6] == 2 and board[3] == 0 or
            board[4] == 2 and board[5] == 2 and board[3] == 0):
                choice = 3
            elif(
            board[1] == 1 and board[7] == 1 and board[4] == 0 or
            board[3] == 1 and board[5] == 1 and board[4] == 0 or
            board[1] == 2 and board[7] == 2 and board[4] == 0 or
            board[3] == 2 and board[5] == 2 and board[4] == 0 or
            board[0] == 1 and board[8] == 1 and board[4] == 0 or
            board[2] == 1 and board[6] == 1 and board[4] == 0 or
            board[0] == 2 and board[8] == 2 and board[4] == 0 or
            board[2] == 2 and board[6] == 2 and board[4] == 0):
                choice = 4
            elif(
            board[2] == 1 and board[8] == 1 and board[5] == 0 or
            board[3] == 1 and board[4] == 1 and board[5] == 0 or
            board[2] == 2 and board[8] == 2 and board[5] == 0 or
            board[3] == 2 and board[4] == 2 and board[5] == 0):
                choice = 5
            elif(
            board[0] == 1 and board[3] == 1 and board[6] == 0 or
            board[7] == 1 and board[8] == 1 and board[6] == 0 or
            board[0] == 2 and board[3] == 2 and board[6] == 0 or
            board[7] == 2 and board[8] == 2 and board[6] == 0 or
            board[2] == 1 and board[4] == 1 and board[6] == 0 or
            board[2] == 2 and board[4] == 2 and board[6] == 0):
                choice = 6
            elif(
            board[1] == 1 and board[4] == 1 and board[7] == 0 or
            board[6] == 1 and board[8] == 1 and board[7] == 0 or
            board[1] == 2 and board[4] == 2 and board[7] == 0 or
            board[6] == 2 and board[8] == 2 and board[7] == 0):
                choice = 7
            elif(
            board[2] == 1 and board[5] == 1 and board[8] == 0 or
            board[6] == 1 and board[7] == 1 and board[8] == 0 or
            board[2] == 2 and board[5] == 2 and board[8] == 0 or
            board[6] == 2 and board[7] == 2 and board[8] == 0 or
            board[0] == 1 and board[4] == 1 and board[8] == 0 or
            board[0] == 2 and board[4] == 2 and board[8] == 0):
                choice = 8
            else:
                choice = random.randrange(0,9)
                print(choice)
        else:  
            choice = random.randrange(0,9)
            print(choice)

        if board[choice] > 0:
            computerChoose()
        else:
            board[choice] = 2
            checkBoard()

    def checkBoard():
        if(
        board[0] == 1 and board[1] == 1 and board[2] == 1 or
        board[3] == 1 and board[4] == 1 and board[5] == 1 or
        board[6] == 1 and board[7] == 1 and board[8] == 1 or
        board[0] == 1 and board[3] == 1 and board[6] == 1 or
        board[1] == 1 and board[4] == 1 and board[7] == 1 or
        board[2] == 1 and board[5] == 1 and board[8] == 1 or
        board[0] == 1 and board[4] == 1 and board[8] == 1 or
        board[2] == 1 and board[4] == 1 and board[6] == 1):
            gameOver("You Win!")
        if(
        board[0] == 2 and board[1] == 2 and board[2] == 2 or
        board[3] == 2 and board[4] == 2 and board[5] == 2 or
        board[6] == 2 and board[7] == 2 and board[8] == 2 or
        board[0] == 2 and board[3] == 2 and board[6] == 2 or
        board[1] == 2 and board[4] == 2 and board[7] == 2 or
        board[2] == 2 and board[5] == 2 and board[8] == 2 or
        board[0] == 2 and board[4] == 2 and board[8] == 2 or
        board[2] == 2 and board[4] == 2 and board[6] == 2):
            gameOver("You Lose!")
            
    game_running = True

    def gameOver(msg):
        game_over = True
        message = font.render(msg,1,BLACK)
        instructions = font.render("To play again, hit the 'r' key; To Exit the game, close the window",1,BLACK)
        
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    game_over = False
                
            SCREEN.fill(WHITE)

            SCREEN.blit(message, [DISPLAY_WIDTH / 3, DISPLAY_HEIGHT / 3])
            SCREEN.blit(instructions, [DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 3 * 2])
            
            pygame.display.update()

            clock.tick(FPS)
    

    while game_running:
        #get Events
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOX1.collidepoint(event.pos):
                    if board[0] > 0:
                        print("Please Try Again")
                    else:
                        board[0] = 1
                        computerChoose()
                        
                elif BOX2.collidepoint(event.pos):
                    if board[1] > 0:
                        print("Please Try Again")
                    else:
                        board[1] = 1
                        computerChoose()
                        
                elif BOX3.collidepoint(event.pos):
                    if board[2] > 0:
                        print("Please Try Again")
                    else:
                        board[2] = 1
                        computerChoose()
                        
                elif BOX4.collidepoint(event.pos):
                    if board[3] > 0:
                        print("Please Try Again")
                    else:
                        board[3] = 1
                        computerChoose()
                        
                elif BOX5.collidepoint(event.pos):
                    if board[4] > 0:
                        print("Please Try Again")
                    else:
                        board[4] = 1
                        computerChoose()
                        
                elif BOX6.collidepoint(event.pos):
                    if board[5] > 0:
                        print("Please Try Again")
                    else:
                        board[5] = 1
                        computerChoose()
                        
                elif BOX7.collidepoint(event.pos):
                    if board[6] > 0:
                        print("Please Try Again")
                    else:
                        board[6] = 1
                        computerChoose()
                        
                elif BOX8.collidepoint(event.pos):
                    if board[7] > 0:
                        print("Please Try Again")
                    else:
                        board[7] = 1
                        computerChoose()
                        
                elif BOX9.collidepoint(event.pos):
                    if board[8] > 0:
                        print("Please Try Again")
                    else:
                        board[8] = 1
                        computerChoose()

        #update and refresh screen        
        SCREEN.fill(WHITE)

        #draw board
        pygame.draw.line(SCREEN, BLACK, (DISPLAY_WIDTH/7 * 3,DISPLAY_HEIGHT/5), (DISPLAY_WIDTH/7 * 3,DISPLAY_HEIGHT/5 * 4), 5)
        pygame.draw.line(SCREEN, BLACK, (DISPLAY_WIDTH/7 * 4,DISPLAY_HEIGHT/5), (DISPLAY_WIDTH/7 * 4,DISPLAY_HEIGHT/5 * 4), 5)
        pygame.draw.line(SCREEN, BLACK, (DISPLAY_WIDTH/7 * 2,DISPLAY_HEIGHT/5 * 2), (DISPLAY_WIDTH/7 * 5,DISPLAY_HEIGHT/5 * 2), 5)
        pygame.draw.line(SCREEN, BLACK, (DISPLAY_WIDTH/7 * 2,DISPLAY_HEIGHT/5 * 3), (DISPLAY_WIDTH/7 * 5,DISPLAY_HEIGHT/5 * 3), 5)

        if board[0] == 1:
            drawX(BOX1)
        elif board[0] == 2:
            drawO(BOX1)
            
        if board[1] == 1:
            drawX(BOX2)
        elif board[1] == 2:
            drawO(BOX2)
            
        if board[2] == 1:
            drawX(BOX3)
        elif board[2] == 2:
            drawO(BOX3)
            
        if board[3] == 1:
            drawX(BOX4)
        elif board[3] == 2:
            drawO(BOX4)
            
        if board[4] == 1:
            drawX(BOX5)
        elif board[4] == 2:
            drawO(BOX5)
            
        if board[5] == 1:
            drawX(BOX6)
        elif board[5] == 2:
            drawO(BOX6)
            
        if board[6] == 1:
            drawX(BOX7)
        elif board[6] == 2:
            drawO(BOX7)
            
        if board[7] == 1:
            drawX(BOX8)
        elif board[7] == 2:
            drawO(BOX8)
            
        if board[8] == 1:
            drawX(BOX9)
        elif board[8] == 2:
            drawO(BOX9)
    
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

mainLoop()
