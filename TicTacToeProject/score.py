class Score:
    pass


def check_winner(board):
    pass



def check_option(board, player_choice):
    if player_choice in board:
        if board[player_choice] == 'x' or board[player_choice] == "o":
            print("That spot is already taken, please choose another location")
        else:
            return True
    else:
        print("That's not an available option")
