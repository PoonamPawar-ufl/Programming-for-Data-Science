def printBoard(board):
    # Print the current board state
    print()
    for row in range(6, 0, -1):
        row_data = [board[col][row] for col in 'abcdefg']
        print(f"| {row} | {' | '.join(row_data)} |")
        print("---------------------------------")
    print("|R/C| a | b | c | d | e | f | g |")
    print("---------------------------------\n")
 

def resetBoard():
    # Create an empty board (columns 'a' to 'g', rows 1 to 6)
    return {col: {row: ' ' for row in range(1, 7)} for col in 'abcdefg'}

def availablePosition(board):
    # Return a list of available positions (only bottom-most unfilled spots)
    positions = []
    for col in 'abcdefg':
        for row in range(1, 7):
            if board[col][row] == ' ':
                positions.append(f"{col}{row}")
                break
    return positions

def validateEntry(position, board):
    # Validate the position entry
    if len(position) != 2 or position[0] not in 'abcdefg' or not position[1].isdigit():
        return False
    col = position[0]
    row = int(position[1])
    if row < 1 or row > 6 or board[col][row] != ' ':
        return False

    for r in range(1, row):
        if board[col][r] == ' ':
            return False  # Player is trying to place in a non-bottommost row
  
    return True

def make_move(board, position, turn):
    # Place the player's mark in the lowest available row in the column
    col = position[0]
    for row in range(1, 7):
        if board[col][row] == ' ':
            board[col][row] = turn
            break

def checkWin(board, turn):
    # Check for a winning sequence of 4 in all directions
    # Horizontal, vertical, and diagonal checks
    def check_direction(c, r, dc, dr):
        count = 0
        while c in 'abcdefg' and 1 <= r <= 6 and board[c][r] == turn:
            count += 1
            if count == 4:
                return True
            c = chr(ord(c) + dc)  # Move in column
            r += dr               # Move in row
        return False

    for col in 'abcdefg':
        for row in range(1, 7):
            if board[col][row] == turn:
                if (check_direction(col, row, 1, 0) or  # Horizontal right
                    check_direction(col, row, 0, 1) or  # Vertical up
                    check_direction(col, row, 1, 1) or  # Diagonal up-right
                    check_direction(col, row, 1, -1)):  # Diagonal down-right
                    return True
    return False

def checkFull(board):
    # Check if the board is full
    return all(board[col][6] != ' ' for col in 'abcdefg')

def checkEnd(board):
    if checkFull(board):
        print("\nDRAW! NOBODY WINS!")
        return True
    return False
    
def main():
    repeat = "Y"

    while(repeat[0].lower() == "y"):
        print("New Game: X goes first.")
        board = resetBoard()
        turn = 'X'

        while True:
            printBoard(board)
            print(f"{turn}'s turn.")
            positions = availablePosition(board)
            print(f"Where do you want your {turn} placed? \nAvailable positions are: {positions}")

            # Get valid input
            while True:
                position = input("\nPlease enter column-letter and row-number (e.g., a1): ").lower()
                
                if validateEntry(position, board):
                    print("Thank you for your selection.")
                    break
                else:
                    print("Invalid input. Please try again.")

            # Make the move
            make_move(board, position, turn)

            # Check for a win
            if checkWin(board, turn):
                print(f"{turn} IS THE WINNER!!!")
                printBoard(board)
                break

            # Check if the board is full (draw)
            elif checkEnd(board):
                printBoard(board)
                break

            # Switch turns
            turn = 'O' if turn == 'X' else 'X'

        # Ask if players want to play another game
        repeat = input("Another game? Enter Y or y for yes.\n")

    print("Thank you for playing!")

if __name__ == "__main__":
    main()