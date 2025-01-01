def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    print("-------------")
    for i in range(0, 3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")

def check_win(board, player):
    """Checks if the given player has won the game."""
    # Check rows
    for i in range(0, 3):
        if board[i * 3] == player and board[i * 3 + 1] == player and board[i * 3 + 2] == player:
            return True

    # Check columns
    for i in range(0, 3):
        if board[i] == player and board[i + 3] == player and board[i + 6] == player:
            return True

    # Check diagonals
    if (board[0] == player and board[4] == player and board[8] == player) or \
    (board[2] == player and board[4] == player and board[6] == player):
        return True

    return False

def check_draw(board):
    """Checks if the game is a draw."""
    for i in range(0, 9):
        if board[i] == " ":
            return False
    return True

def get_player_move(board):
    """Gets the player's move and validates it."""
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row * 3 + col] == " ":
                return row * 3 + col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_tic_tac_toe():
    """Plays a game of Tic-Tac-Toe."""
    board = [" " for _ in range(9)]
    current_player = "X"

    print("Let's play Tic-Tac-Toe!")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        move = get_player_move(board)
        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()