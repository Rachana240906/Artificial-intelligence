import math
import time

board = [" "] * 9
nodes_explored = 0

winning_combinations = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

# Print board
def print_board(b):
    print()
    print(b[0], "|", b[1], "|", b[2])
    print("--+---+--")
    print(b[3], "|", b[4], "|", b[5])
    print("--+---+--")
    print(b[6], "|", b[7], "|", b[8])
    print()

# Check winner
def check_winner(b):
    for a, b1, c in winning_combinations:
        if b[a] == b[b1] == b[c] and b[a] != " ":
            return b[a]

    if " " not in b:
        return "Draw"

    return None


# Minimax algorithm
def minimax(board, depth, is_max):
    global nodes_explored
    nodes_explored += 1

    result = check_winner(board)

    if result == "X":
        return 1
    elif result == "O":
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                print("  "*depth + f"MAX places X at {i}")

                score = minimax(board, depth+1, False)

                board[i] = " "

                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                print("  "*depth + f"MIN places O at {i}")

                score = minimax(board, depth+1, True)

                board[i] = " "

                best = min(best, score)

        return best


# Find best move
def best_move(board):

    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":

            board[i] = "X"

            score = minimax(board, 0, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Run algorithm
start = time.time()

move = best_move(board)

end = time.time()

print("\nBest Move for X:", move)
print("Nodes Explored:", nodes_explored)
print("Execution Time:", end - start)

board[move] = "X"
print_board(board)
