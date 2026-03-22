import random
import math

# -----------------------------
# Generate Random Board
# -----------------------------
def random_board():
    return [random.randint(0,7) for _ in range(8)]


# -----------------------------
# Heuristic Function
# h(n) = number of attacking pairs
# -----------------------------
def heuristic(board):
    h = 0
    for i in range(8):
        for j in range(i+1, 8):
            if board[i] == board[j]:   # same row
                h += 1
            if abs(board[i] - board[j]) == abs(i - j):  # diagonal
                h += 1
    return h


# -----------------------------
# Generate Neighbors
# -----------------------------
def get_neighbors(board):
    neighbors = []
    for col in range(8):
        for row in range(8):
            if row != board[col]:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors


# ======================================================
# 1️⃣ First-Choice Hill Climbing
# ======================================================
def first_choice_hill_climb(board):
    steps = 0
    current = board

    while True:
        current_h = heuristic(current)
        neighbors = get_neighbors(current)
        random.shuffle(neighbors)

        moved = False

        for neighbor in neighbors:
            if heuristic(neighbor) < current_h:
                current = neighbor
                steps += 1
                moved = True
                break

        if not moved:
            return current, heuristic(current), steps


# ======================================================
# 2️⃣ Random Restart Hill Climbing
# ======================================================
def random_restart(max_restarts=100):
    total_steps = 0

    for restart in range(max_restarts):
        board = random_board()
        current = board
        steps = 0

        while True:
            current_h = heuristic(current)
            neighbors = get_neighbors(current)
            next_board = min(neighbors, key=heuristic)
            next_h = heuristic(next_board)

            if next_h >= current_h:
                break

            current = next_board
            steps += 1

        total_steps += steps

        if heuristic(current) == 0:
            return current, 0, total_steps, restart+1

    return current, heuristic(current), total_steps, max_restarts


# ======================================================
# 3️⃣ Simulated Annealing
# ======================================================
def simulated_annealing(board):
    current = board
    T = 100
    cooling = 0.95
    steps = 0

    while T > 0.1:
        current_h = heuristic(current)

        if current_h == 0:
            return current, 0, steps

        neighbors = get_neighbors(current)
        next_board = random.choice(neighbors)
        next_h = heuristic(next_board)

        delta = next_h - current_h

        if delta < 0:
            current = next_board
        else:
            probability = math.exp(-delta / T)
            if random.random() < probability:
                current = next_board

        T *= cooling
        steps += 1

    return current, heuristic(current), steps


# ======================================================
# RUN 50 EXPERIMENTS
# ======================================================
if __name__ == "__main__":

    print("FIRST CHOICE HILL CLIMBING")
    print("----------------------------------")

    for i in range(50):
        board = random_board()
        initial_h = heuristic(board)

        final_board, final_h, steps = first_choice_hill_climb(board)
        status = "Solved" if final_h == 0 else "Fail"

        print(i+1, initial_h, final_h, steps, status)

    print("\nRANDOM RESTART HILL CLIMBING")
    print("----------------------------------")

    for i in range(50):
        final_board, final_h, steps, restarts = random_restart()
        status = "Solved" if final_h == 0 else "Fail"

        print(i+1, "Final h:", final_h, "Steps:", steps,
              "Restarts:", restarts, status)

    print("\nSIMULATED ANNEALING")
    print("----------------------------------")

    for i in range(50):
        board = random_board()
        initial_h = heuristic(board)

        final_board, final_h, steps = simulated_annealing(board)
        status = "Solved" if final_h == 0 else "Fail"

        print(i+1, initial_h, final_h, steps, status)
