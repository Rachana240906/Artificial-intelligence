start_state = ((7,2,4),(5,0,6),(8,3,1))
goal_state  = ((0,1,2),(3,4,5),(6,7,8))


# Generate neighbours
def get_neighbours(state):

    neighbours = []

    zero_row = -1
    zero_col = -1

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break
        if zero_row != -1:
            break

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for x, y in moves:
        new_row = zero_row + x
        new_col = zero_col + y

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_state = [list(row) for row in state]

            new_state[zero_row][zero_col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[zero_row][zero_col]

            neighbours.append(tuple(tuple(row) for row in new_state))

    return neighbours


def bfs_count(initial, goal):

    queue = [initial]     # normal list
    visited = {initial}
    front = 0
    count = 0

    while front < len(queue):

        current_state = queue[front]
        front += 1
        count += 1

        if current_state == goal:
            return count

        for next_state in get_neighbours(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    return count



count = bfs_count(start_state, goal_state)
print("States visited:", count)
