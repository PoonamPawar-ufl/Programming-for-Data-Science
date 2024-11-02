
# Function to print the current board state
def printBoard(board):
    
    print("-------------------")
    print(f"| R\C | 0 | 1 | 2 |")
    print("-------------------")
    print(f"| 0   | {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("-------------------")
    print(f"| 1   | {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("-------------------")
    print(f"| 2   | {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print("-------------------")
    
# Function to reset the board (3x3 grid filled with empty spaces)
def resetBoard():
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    printBoard(board)
    return board

# Function to validate the player's move
def validateEntry(row, col, board):

    # Check if the row and column numbers are within bounds (0, 1, or 2)
    if row >= 3 or col >= 3 or row < 0 or col < 0:
        print("Invalid entry: try again. \nRow & column numbers must be either 0, 1, or 2.")
        return False  

    # Check if the selected cell is already taken
    if board[row][col] != ' ':
        print("That cell is already taken. \nPlease make another selection.")
        return False  

    return True     # Check if the selected cell is already taken


# Function to check if the board is completely filled
def checkFull(board):
    return all(cell != ' ' for row in board for cell in row)


# Function to check if the board is completely filled
def checkEnd(board):
    if checkFull(board):
        print("\nDRAW! NOBODY WINS!")
        return True
    return False
               
# Function to check if a player has won (rows, columns, or diagonals)
def checkWin(board, turn):
    for i in range(3):
        if all(board[i][j] == turn for j in range(3)) or all(board[j][i] == turn for j in range(3)):
            return True

    # Check diagonals for a winning combination
    if all(board[i][i] == turn for i in range(3)) or all(board[i][2-i] == turn for i in range(3)):
        return True
    return False

def main():
    repeat = "Y"

    while(repeat[0].lower() == "y"):
        
        print("New Game: X goes first.")
        print()

        # Initialize/reset the board for a new game
        board = resetBoard()

        turn = "X"
        while (True):
            try:
                print(f"\n{turn}'s turn.")
                inputstr = input(f"Where do you want your {turn} placed?\nPlease enter row number and column number separated by a comma.\n")
                inputlist = inputstr.split(",")
                row = int(inputlist[0])
                col = int(inputlist[1])
                print("You have entered row #",row,"\n\t   and column #",col)
                
                # Validate the player's input
                valid = validateEntry(row,col,board)

                if not valid:
                    continue
                else:
                    print("Thank you for your selection.")
                    board[row][col] = turn # Update the board with the player's move

                 # Check if the current player has won
                    if checkWin(board, turn):
                        print(f"{turn} IS THE WINNER!!!")
                        printBoard(board)
                        break
                    elif checkEnd(board):       # Check if the game ends in a draw
                        printBoard(board)
                        break
                    
                    else:
                        printBoard(board)
            except (IndexError,ValueError):
                print("Invalid format. Please input two numbers separated by a comma, like 0,2.")

            
            # Switch turns between X and O
            if(turn == 'X'):
                turn = 'O'
            else:
                turn = 'X'

            
        # Prompt the players to play again or exit
        repeat = input("Another game? Enter Y or y for yes.\n")

    print("Thank you for playing!")



if __name__ == "__main__":
    main()
