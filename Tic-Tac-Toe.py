# Tic-Tac-Toe game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there's a winner
def check_winner(board, mark):
    # Check rows
    for row in board:
        if all([spot == mark for spot in row]):
            return True
    # Check columns
    for col in range(3):
        if all([row[col] == mark for row in board]):
            return True
    # Check diagonals
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False

# Function to check if the board is full (a tie)
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to play the game
def play_game():
    # Initial empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_mark = "X"
    
    while True:
        print_board(board)
        # Ask the current player for a move
        try:
            # Handle both "1 1" and "1,1" formats
            move = input(f"Player {current_mark}, enter row and column (0-2): ").replace(",", " ")
            row, col = map(int, move.split())
        except ValueError:
            print("Invalid input! Please enter row and column numbers between 0 and 2.")
            continue

        # Check if the input is within bounds and the spot is available
        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        # Place the player's mark on the board
        board[row][col] = current_mark
        
        # Check if the current player has won
        if check_winner(board, current_mark):
            print_board(board)
            print(f"Player {current_mark} wins!")
            break
        
        # Check if the game is a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_mark = "O" if current_mark == "X" else "X"

# Run the game
play_game()
