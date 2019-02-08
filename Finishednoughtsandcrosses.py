# implement a program that prints a noughts-and-crosses grid, asks 
# where the player wants to place their mark, places the player's 
# mark on this grid if the square is empty, and prints the grid again 
# if something was placed on board.
# The board is a 3x3 grid, where an empty square is marked by a "." symbol. 
# Each square contains a coordinate whose x and y values are between 0 and 2. 
# The coordinate (0,0) is on the left upper corner of the grid. The coordinate 
# values increase when going rightwards and downwards. For instance, the square 
# coordinate of the lower right corner is (2,2) and the one on the right side 
# of the centre row is (1,2).
# The user enters the coordinates of the square they choose, separated by one space. 
# The first coordinate is the x coordinate and the second one is the y coordinate. 
# The mark of the player whose turn it is is placed the square given by the player 
# if the square is empty. If there is already a mark in the square, print the error 
# message "Error: a mark has already been placed on this square." The turn changes 
# to the other player when a mark is placed on the board successfully. We have 
# already implemented the reviewing of errors for the user's entries, and the 
# ending of the game when the grid is filled, to the file template.
# checks when the game ends and declares the winner.The program must check the horizontal 
# and vertical rows and both slanted rows. If the players are in a draw, print: "Draw!"

def main():

    # TODO: implement the datastructure for storing the board
    board=[['.','.','.'],['.','.','.'],['.','.','.']]
    s=''
    print(s.join(board[0]))
    print(s.join(board[1]))
    print(s.join(board[2]))
    
    turns = 0  # How many turns have been played

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.

    while (turns != -1):

            # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)

            # TODO: implement the turn of one player here
            if board[y][x]=='.':
                board[y][x]= mark
                print(s.join(board[0]))
                print(s.join(board[1]))
                print(s.join(board[2]))
                turns += 1
                if (board[0][0]== board[0][1]==board[0][2]==mark):
                    print("The game ended, the winner is ", board[0][0])
                    turns=-1
                elif board[1][0]== board[1][1]==board[1][2]==mark:
                    print("The game ended, the winner is ", board[1][0])
                    turns = -1
                elif board[2][0]== board[2][1]==board[2][2]==mark:
                    print("The game ended, the winner is ", board[2][0])
                    turns = -1
                elif board[0][0]== board[1][0]==board[2][0]==mark:
                    print("The game ended, the winner is ", board[0][0])
                    turns = -1
                elif board[0][1]== board[1][1]==board[2][1]==mark:
                    print("The game ended, the winner is ", board[0][1])
                    turns = -1
                elif board[0][2]== board[1][2]==board[2][2]==mark:
                    print("The game ended, the winner is ", board[0][2])
                    turns = -1
                elif board[0][2]== board[1][1]==board[2][0]==mark:
                    print("The game ended, the winner is ", board[0][2])
                    turns = -1
                elif board[0][0]== board[1][1]==board[2][2]==mark:
                    print("The game ended, the winner is ", board[0][0])
                    turns = -1
                elif board[0][0]!='.' and board[0][1]!='.' and board[0][2]!='.' and board[1][0]!='.' and board[1][1]!='.' and board[1][2]!='.' \
                        and board[2][0]!='.' and board[2][1]!='.' and board[2][2]!='.':
                    turns=-1
                    print("Draw!")
            else:
                print("Error: a mark has already been placed on this square.")

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")


main()
