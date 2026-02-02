start_state = ((7,2,4),(5,0,6),(8,3,1))
goal_state  = ((0,1,2),(3,4,5),(6,7,8))



# Generate neighbours 
def get_neighbours(state):

    neighbours = []

    zero_row, zero_col = -1, -1

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break
        if zero_row != -1:
            break

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nr = zero_row + dx
        nc = zero_col + dy

        if 0 <= nr < 3 and 0 <= nc < 3:

            # convert to list to swap
            new_state = [list(row) for row in state]

            new_state[zero_row][zero_col], new_state[nr][nc] = \
                new_state[nr][nc], new_state[zero_row][zero_col]

            # convert back to tuple (hashable)
            neighbours.append(tuple(tuple(row) for row in new_state))

    return neighbours



# Iterative DFS
def dfs_count(initial, goal):

    stack = [initial]
    visited = set()
    count = 0

    while stack:

        current_state = stack.pop()

        if current_state in visited:
            continue

        visited.add(current_state)
        count += 1

        if current_state == goal:
            return count

        for next_state in get_neighbours(current_state):
            if next_state not in visited:
                stack.append(next_state)

    return count



# Print
count = dfs_count(start_state, goal_state)
print("States visited:", count)
