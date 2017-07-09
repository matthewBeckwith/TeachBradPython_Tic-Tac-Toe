#
#GameBoard for Python Tick-Tac-Toe
#
#Created By Matthew Beckwith
#               aka - kodahScripts
#

#import random for the AI
import random

#make a board that the code can check
def initGame():
    board = [
        0,0,0,
        0,0,0,
        0,0,0
    ]
    drawBoard(board)


#we reuse this code a lot so we make it a function
def choose(board):
    choice = int(input("Choose a Box (0-8)"))

    if(choice >= 0):
        if(choice <= 8):
            if(board[choice] > 0):
                print("This has already been picked.... Please pick another")
                choose(board)
            else:
                board[choice] = 1
                computerChoice(board)
        else:
            choose(board)
    else:
        choose(board)
    

#Give the player an Enemy
def computerChoice(board):
    choice = random.randint(-1,9)

    if(board[choice] > 0):
        computerChoice(board)
    else:
        board[choice] = 2
        drawBoard(board)

#Handles showing the board to the user
def drawBoard(board):
    cell = []

    for i in range(0,9):
        if(board[i] == 1):
            cell.append('X')
        elif(board[i] == 2):
            cell.append('O')
        else:
            cell.append(' ')
            
    print("\n" * 100)
    print("""
    TICK-TAC-TOE!
---------------------
    """)
    print("     |     |")
    print("  " + cell[0] + "  |  " + cell[1] + "  |  " + cell[2])
    print("     |     |")
    print("-----|-----|-----")
    print("     |     |")
    print("  " + cell[3] + "  |  " + cell[4] + "  |  " + cell[5])
    print("     |     |")
    print("-----|-----|-----")
    print("     |     |")
    print("  " + cell[6] + "  |  " + cell[7] + "  |  " + cell[8])
    print("     |     |")
    
    checkForWinner(board)

#Check if a Player Won
def checkForWinner(board):
    if(board[0] == 1 and board[1] == 1 and board[2] == 1 or
       board[3] == 1 and board[4] == 1 and board[5] == 1 or
       board[6] == 1 and board[7] == 1 and board[8] == 1 or
       board[0] == 1 and board[3] == 1 and board[6] == 1 or
       board[1] == 1 and board[4] == 1 and board[7] == 1 or
       board[2] == 1 and board[5] == 1 and board[8] == 1 or
       board[0] == 1 and board[4] == 1 and board[8] == 1 or
       board[2] == 1 and board[4] == 1 and board[6] == 1):
        print("\n" * 100)
        print("You Win!")
        playAgain()
    elif(board[0] == 2 and board[1] == 2 and board[2] == 2 or
       board[3] == 2 and board[4] == 2 and board[5] == 2 or
       board[6] == 2 and board[7] == 2 and board[8] == 2 or
       board[0] == 2 and board[3] == 2 and board[6] == 2 or
       board[1] == 2 and board[4] == 2 and board[7] == 2 or
       board[2] == 2 and board[5] == 2 and board[8] == 2 or
       board[0] == 2 and board[4] == 2 and board[8] == 2 or
       board[2] == 2 and board[4] == 2 and board[6] == 2):
        print("\n" * 100)
        print("You Loose!")
        playAgain()
    else:
        choose(board)


#ask if the player wants to play again
def playAgain():
    choice = int(input("""
        Play Again?

        1 - Yes
        2 - No
    """))

    if(choice == 1):
        initGame()
    elif(choice == 2):
        quit()
    else:
        playAgain()

#init the game
initGame()
