#Mini Project2 - PartA Poonam Pawar


class Board:

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

     

    # Function to print the current board state
    def printBoard(self):
        
        print("-------------------")
        print(f"| R\C | 0 | 1 | 2 |")
        print("-------------------")
        print(f"| 0   | {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |")
        print("-------------------")
        print(f"| 1   | {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |")
        print("-------------------")
        print(f"| 2   | {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |")
        print("-------------------")
    

class Game:
    def __init__(self):
        self.b = Board()
        self.turn = 'X'

    #Funtion to Switch Player
    def switchPlayer(self):
        if(self.turn == 'X'):
                self.turn = 'O'
        else:
                self.turn = 'X'

    # Function to validate the player's move
    def validateEntry(self,row, col):
        
        # Check if the row and column numbers are within bounds (0, 1, or 2)
        if row >= 3 or col >= 3 or row < 0 or col < 0:
            print("Invalid entry: try again. \nRow & column numbers must be either 0, 1, or 2.")
            return False  

        # Check if the selected cell is already taken
        if self.b.board[row][col] != ' ':
            print("That cell is already taken. \nPlease make another selection.")
            return False  

        return True     # Check if the selected cell is already taken


    # Function to check if the board is completely filled
    def checkFull(self):
        return all(cell != ' ' for row in self.b.board for cell in row)


              
    # Function to check if a player has won (rows, columns, or diagonals)
    def checkWin(self):
        for i in range(3):
            if all(self.b.board[i][j] == self.turn for j in range(3)) or all(self.b.board[j][i] == self.turn for j in range(3)):
                return True

        # Check diagonals for a winning combination
        if all(self.b.board[i][i] == self.turn for i in range(3)) or all(self.b.board[i][2-i] == self.turn for i in range(3)):
            return True
        return False

    # Function to check if the board is completely filled
    def checkEnd(self):
        if self.checkWin():
            print(f"{self.turn} IS THE WINNER!!!")
            self.b.printBoard()
            return True
        if self.checkFull():
            print("\nDRAW! NOBODY WINS!")
            self.b.printBoard()
            return True
        return False

    # Funtion to play the Game
    def playGame(self):

        print("New Game: X goes first.")
        print()
        self.b.printBoard()
        while (True):
            try:
                    print(f"\n{self.turn}'s turn.")
                    inputstr = input(f"Where do you want your {self.turn} placed?\nPlease enter row number and column number separated by a comma.\n")
                    inputlist = inputstr.split(",")
                    row = int(inputlist[0])
                    col = int(inputlist[1])
                    print("You have entered row #",row,"\n\t   and column #",col)
                    
                    # Validate the player's input
                    valid = self.validateEntry(row,col)

                    if not valid:
                        continue
                    else:
                        print("Thank you for your selection.")
                        self.b.board[row][col] = self.turn # Update the board with the player's move

                    # Check if the game ends
                    if self.checkEnd():
                        break
                    else:
                        self.b.printBoard()

            except (IndexError,ValueError):
                    print("Invalid format. Please input two numbers separated by a comma, like 0,2.")
                    self.switchPlayer()
        # Switch turns between X and O
            self.switchPlayer()


def main():
    repeat = "Y"

    while(repeat[0].lower() == "y"):
        
        Newgame = Game()
        Newgame.playGame()
                 
        # Prompt the players to play again or exit
        repeat = input("Another game? Enter Y or y for yes.\n")

    print("Thank you for playing!")



if __name__ == "__main__":
    main()
