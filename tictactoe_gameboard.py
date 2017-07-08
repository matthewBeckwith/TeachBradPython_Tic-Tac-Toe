#
#GameBoard for Python Tick-Tac-Toe
#
#Created By Matthew Beckwith
#               aka - kodahScripts
#

#import random for the AI
import random

#make a board that the code can check
board = [
    0,0,0,
    0,0,0,
    0,0,0
]

#we reuse this code a lot so we make it a function
def choose():
    choice = int(input("Choose a Box (0-8)"))

    if(choice >= 0):
        if(choice <= 8):
            if(board[choice] > 0):
                print("This has already been picked.... Please pick another")
                choose()
            else:
                board[choice] = 1
                computerChoice()
        else:
            choice()
    else:
        choice()
    

#Give the player an Enemy
def computerChoice():
    choice = random.randint(-1,9)

    if(board[choice] > 0):
        computerChoice()
    else:
        board[choice] = 2
        drawBoard()

#Handles showing the board to the user
def drawBoard():
    print("\n" * 100)
    cell = []

    for i in range(0,9):
        if(board[i] == 1):
            cell.append('X')
        elif(board[i] == 2):
            cell.append('O')
        else:
            cell.append(' ')

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
    
    choose()

drawBoard()
