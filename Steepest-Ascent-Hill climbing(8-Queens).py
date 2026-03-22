import random
import math

# Generate random board
def random_board():
    return [random.randint(0,7) for _ in range(8)]

# Heuristic function: count attacking pairs
def heuristic(board):
    h = 0
    for i in range(8):
        for j in range(i+1,8):
            # same row
            if board[i] == board[j]:
                h += 1
            # same diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

# Generate neighbors
def get_neighbors(board):
    neighbors = []
    for col in range(8):
        for row in range(8):
            if row != board[col]:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

# Steepest Ascent Hill Climbing
def steepest_hill_climb(board):
    steps = 0
    current = board
    while True:
        current_h = heuristic(current)
        neighbors = get_neighbors(current)
        next_board = min(neighbors, key=heuristic)
        next_h = heuristic(next_board)

        if next_h >= current_h:
            return current, current_h, steps

        current = next_board
        steps += 1

for i in range(50):
    board = random_board()
    initial_h = heuristic(board)
    final_board, final_h, steps = steepest_hill_climb(board)
    
    status = "Solved" if final_h == 0 else "Fail"
    
    print(i+1, initial_h, final_h, steps, status)
