import math

# Define the players and empty cell
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Define the board
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

# Function to print the board
def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Function to check if there are any empty cells
def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

# Function to evaluate the board state
def evaluate(board):
    # Check for win conditions (rows, columns, diagonals)
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return 10 if row[0] == AI else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return 10 if board[0][col] == AI else -10

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == AI else -10

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == AI else -10

    return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    score = evaluate(board)

    if score == 10:  # AI wins
        return score - depth

    if score == -10:  # Human wins
        return score + depth

    if not is_moves_left(board):  # Tie
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = EMPTY
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = EMPTY
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# Function to find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to check if the game is over
def is_game_over(board):
    return evaluate(board) != 0 or not is_moves_left(board)

# Function to play the Tic-Tac-Toe game
def play_game():
    print("Tic-Tac-Toe: Human (O) vs AI (X)")
    print_board(board)

    while True:
        # Human move
        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == EMPTY:
                board[row][col] = HUMAN
                break
            else:
                print("Invalid move. Try again.")

        print_board(board)

        if is_game_over(board):
            break

        # AI move
        print("AI is making its move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI

        print_board(board)

        if is_game_over(board):
            break

    # Evaluate the final result
    score = evaluate(board)
    if score == 10:
        print("AI wins!")
    elif score == -10:
        print("Human wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_game()
