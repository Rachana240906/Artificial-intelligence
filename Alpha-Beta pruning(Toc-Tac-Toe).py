import math
import time

board = [" "] * 9

nodes_minimax = 0
nodes_alphabeta = 0

winning_combinations = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def check_winner(b):
    for a,b1,c in winning_combinations:
        if b[a] == b[b1] == b[c] and b[a] != " ":
            return b[a]
    if " " not in b:
        return "Draw"
    return None


# ---------- MINIMAX ----------
def minimax(board, is_max):

    global nodes_minimax
    nodes_minimax += 1

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
                score = minimax(board, False)
                board[i] = " "
                best = max(best, score)
        return best

    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                best = min(best, score)
        return best


# ---------- ALPHA BETA ----------
def alphabeta(board, alpha, beta, is_max, depth=0):

    global nodes_alphabeta
    nodes_alphabeta += 1

    result = check_winner(board)

    if result == "X":
        return 1
    elif result == "O":
        return -1
    elif result == "Draw":
        return 0

    if is_max:

        value = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                print("  "*depth + f"MAX tries position {i}")

                value = max(value,
                    alphabeta(board, alpha, beta, False, depth+1)
                )

                board[i] = " "

                alpha = max(alpha, value)

                if alpha >= beta:
                    print("  "*depth + "PRUNE remaining branches")
                    break

        return value

    else:

        value = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                print("  "*depth + f"MIN tries position {i}")

                value = min(value,
                    alphabeta(board, alpha, beta, True, depth+1)
                )

                board[i] = " "

                beta = min(beta, value)

                if alpha >= beta:
                    print("  "*depth + "PRUNE remaining branches")
                    break

        return value


# ---------- BEST MOVE ----------
def best_move_minimax():

    best_score = -math.inf
    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "X"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def best_move_alphabeta():

    best_score = -math.inf
    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "X"

            score = alphabeta(board, -math.inf, math.inf, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# ---------- PERFORMANCE COMPARISON ----------
start = time.time()
m1 = best_move_minimax()
t1 = time.time() - start

start = time.time()
m2 = best_move_alphabeta()
t2 = time.time() - start


print("\nMinimax Move:", m1)
print("Nodes explored (Minimax):", nodes_minimax)
print("Time:", t1)

print("\nAlphaBeta Move:", m2)
print("Nodes explored (AlphaBeta):", nodes_alphabeta)
print("Time:", t2)
