# TODO 1: make this OOB
# TODO 2: implement TRY and EXCEPT blocks
# TODO 3: check why the board is not static



import random




def print_board(board):
    divider = 10 * "-"

    print(board["1"] + "  | " + board["2"] + "  | " + board["3"])
    print(divider)
    print(board["4"] + "  | " + board["5"] + "  | " + board["6"])
    print(divider)
    print(board["7"] + "  | " + board["8"] + "  | " + board["9"])


def explanation():
    print("""This is a textbased version of TicTacToe.
To place your symbol on the board, type the number of that area:

                1 | 2 | 3
                ---------- 
                4 | 5 | 6
                ---------- 
                7 | 8 | 9  
-------------------------------------------------------
Game start:
                """)

def symbol_selection():
    player_symbol = input("With which symbol do you want to play? x or o?").lower()
    return player_symbol



def check_who_won(board):
    # Check horizontally
    # First row
    if board["1"] == board["2"] == board["3"] == player_one:
        return "Player One"
    elif board["1"] == board["2"] == board["3"] == player_pc:
        return "Computer"

    # Second row
    elif board["4"] == board["5"] == board["6"] == player_one:
        return "Player One"
    elif board["4"] == board["5"] == board["6"] == player_pc:
        return "Computer"

    # Third row
    elif board["7"] == board["8"] == board["9"] == player_one:
        return "Player One"
    elif board["7"] == board["8"] == board["9"] == player_pc:
        return "Computer"

    # Check vertically
    # First column
    if board["1"] == board["4"] == board["7"] == player_one:
        return "Player One"
    elif board["1"] == board["4"] == board["7"] == player_pc:
        return "Computer"

    # Second column
    elif board["2"] == board["5"] == board["8"] == player_one:
        return "Player One"
    elif board["2"] == board["5"] == board["8"] == player_pc:
        return "Computer"

    # Third column
    elif board["3"] == board["6"] == board["9"] == player_one:
        return "Player One"
    elif board["3"] == board["6"] == board["9"] == player_one:
        return "Computer"

    # Check diagonally
    # From upper left to right bottom
    if board["1"] == board["5"] == board["9"] == player_one:
        return "Player_One"
    elif board["1"] == board["5"] == board["9"] == player_pc:
        return 'Computer'
    # From left bottom to upper right
    elif board["7"] == board["5"] == board["3"] == player_one:
        return "Player One"
    elif board["7"] == board["5"] == board["3"] == player_pc:
        return 'Computer'

    else:
        return None


def player_one_turn(board):
    player_choice = input("Player One: ")

    if player_choice in board:
        if board[player_choice] == 'x' or board[player_choice] == "o":
            print("That's spot is already taken")
            player_one_turn(board)
        else:
            board[player_choice] = player_one
            return True
    else:
        print("That's not an option")
        player_one_turn(board)


def random_loc_pc():
    return str(random.randint(1, 9))


def computer_turn(board):
    location = random_loc_pc()
    if board[location] == "x" or board[location] == "o":
        computer_turn(board)
    else:
        board[location] = player_pc




current_board = {"1": "", "2": "", "3": "",
                 "4": "", "5": "", "6": "",
                 "7": "", "8": "", "9": "",
                 }

game_over = False

explanation()
player_one = symbol_selection()

if player_one == "x":
    player_pc = "o"
else:
    player_pc = "x"


while not game_over:
    print_board(current_board)
    winner = check_who_won(current_board)
    if winner is not None:
        game_over = True
    else:
        if player_one_turn(current_board):
            computer_turn(current_board)
        else:
            computer_turn(current_board)

print(f"{winner} has won! The game will close now. Thanks for playing!")
