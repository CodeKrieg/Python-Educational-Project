#encoding: UTF-8
import random
# We import random in order to be able to use the random method in our script 

# We will start by drawing the board. 
# This will create 3 rows (like the classic tic tac toe, we are not looking to make a new game here)
def drawBoard(board):
     print('   |   |')
     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
     print('   |   |')

# Then we will ask for some input from the player.
def inputPlayerLetter():
     letter = ''
     # We start by having an empty variable. In this variable we will store the letter that the player will use. 
     while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = raw_input().upper()
     if letter == 'X':
         return ['X', 'O']
     else:
         return ['O', 'X']
    # In the code above we are checking if the variable letter has stored any value (X or O)
    # Then we are priting a message asking for the user to put in what letter he wishes to use
    # We are receiving input with raw_input (just input in other versions of Python. We are using 2.7.6)
    # We also store the value in the same line and we uppercase it (just to be safe)
    # After that we have a logic witch will determine the AI's (Artificial Inteligence) letter. If X then O if O then X
    
# Now we should work on the logic that will randomize who goes first.
# Since we already imported random we can freely use that function. 
# We will use it bellow, we will do a simple if statement and randomize who goes first.
def whoGoesFirst():
     if random.randint(0, 1) == 0:
         return 'computer'
     else:
        return 'player'
        
# Now we will work on the logic that will handle the play again statement.
# Its quite simple, we print a message and we ask for some input.
# I will return True if the player writes anything that starts with Y (and it will be lowercased just to be safe)
def playAgain():
     print('Do you want to play again? (yes or no)')
     return raw_input().lower().startswith('y')

# This is the logic that will make the move. It gets the move, borad and the letter of the player.
def makeMove(board, letter, move):
     board[move] = letter

# Here we will check who the winner is.
# This function takes 2 arguments and it checks each move on the board (1,2,3,4,5,6,7,8,9) with the letter. if the letter has the most board moves then it wins. 
def isWinner(board, letter):
     return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
     (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
     (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
     (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
     (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
     (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
     (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
     (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal
  
 
def getBoardCopy(board):
     dupeBoard = []
     for i in board:
         dupeBoard.append(i)

     return dupeBoard
# In above piece of code, we invoked an instance of the board by defining it as a new function getBoardCopy, inheriting the board parent class 
# Then we defined and empty variable called dupeboard and looped thru it. 
# In last line we returned the value that would get assigned to dupeboard
# Here we will check if there is any space free on the board. If there is not then we will return an empty variable.
def isSpaceFree(board, move):
     return board[move] == ' '

def getPlayerMove(board):
     move = ' '
     while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
         print('What is your next move? (1-9)')
         move = raw_input()
     return int(move)
# In the code above we ask for the players next move. 
# We are starting with an empty variable (move) and then we have a while loop which would loop thru the moves (1-9) that are being captured from user input 
# or else if there is no space left on the board it would not run that while loop for "move" 
# In next line we ask for user input with a prompt. 

def chooseRandomMoveFromList(board, movesList):
     possibleMoves = []
     for i in movesList:
         if isSpaceFree(board, i):
             possibleMoves.append(i)

     if len(possibleMoves) != 0:
         return random.choice(possibleMoves)
     else:
         return None
# Here we are chosing a random move from the available moves. 
# We are doing a for lop and checking which space is free, therefore, checking which moves are available.
# On the second if we are checking the length (len) of the possibleMoves, and we are making sure that its not equal to 0
# Then we are returning one of the possible moves randomly. 
# Else, return none


def getComputerMove(board, computerLetter):
     # This is to initialize the board for the computer, and ask the AI to choose the letter for the move as per its desired
     if computerLetter == 'X':
         playerLetter = 'O'
     else:
         playerLetter = 'X'
    # This if loop is to determine what letter the computer chose. 
     # First, check if we can win in the next move
     # We are doing a loop and we check if there is any free space.
     for i in range(1, 10):
      copy = getBoardCopy(board)
     if isSpaceFree(copy, i):
         
         makeMove(copy, computerLetter, i)
         if isWinner(copy, computerLetter):
            return i
     # Check if the player could win on their next move.
     for i in range(1, 10):
         copy = getBoardCopy(board)
     if isSpaceFree(copy, i):
             makeMove(copy, playerLetter, i)
             if isWinner(copy, playerLetter):
                 return i
     # Try to take one of the corners, if they are free.
     move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
     if move != None:
         return move
     # Try to take the center, if it is free.
     if isSpaceFree(board, 5):
         return 5
    # Move on one of the sides.
     return chooseRandomMoveFromList(board, [2, 4, 6, 8])
     

def isBoardFull(board):
     # Return True if every space on the board has been taken. Otherwise return False.
     for i in range(1, 10):
         if isSpaceFree(board, i):
             return False
     return True


print('Hello. This is a Tic Tac Toe game. Enjoy!')
# Print a message before starting the game

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
    # If we are going to end up the game, we will use break to end the while loop we're running
    # Most of the code above is self explanatory, but I will give my best to explain it better.
    # While True = If the board is full, then reseat the board.
    # Get the player and computer letter and player input
    # start the function that decides who goes first
    # Print a text
    # The variable gameIsPLaying (we will use it to decide when the game is playing and when not) is set to true
    # Do a while loop while (heh) the game is playing, if the turn is for the player: draw the board, move (get input of the move) make the move and then if its winner draw the board, print some text and put the variable gameIsPLaying t ofalse
    # If the board is full, draw the board, print a text and break (stop) the logic
    # Else, allow the computer to make the move
    
    # If the move is for the computer, then its just the same cose as above.

