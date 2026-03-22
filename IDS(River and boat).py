# Queue Implementation
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)   

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
# Possible boat moves
MOVES = [(1,0), (2,0), (0,1), (0,2), (1,1)]

def is_valid(g_left, b_left):
    g_right = 3 - g_left
    b_right = 3 - b_left

    if g_left < 0 or g_left > 3 or b_left < 0 or b_left > 3:
        return False

    if g_left > 0 and b_left > g_left:
        return False

    if g_right > 0 and b_right > g_right:
        return False

    return True


def get_successors(state):
    g_left, b_left, boat = state
    successors = []

    for g, b in MOVES:
        if boat == 'L':
            new_state = (g_left - g, b_left - b, 'R')
        else:
            new_state = (g_left + g, b_left + b, 'L')

        if is_valid(new_state[0], new_state[1]):
            successors.append(new_state)

    return successors
# Depth Limited Search 
def dls(state, goal, limit, path, visited):
    if state == goal:
        return path

    if limit == 0:
        return None

    visited.add(state)

    for successor in get_successors(state):
        if successor not in visited:
            result = dls(successor, goal, limit - 1,
                         path + [successor], visited)
            if result is not None:
                return result

    visited.remove(state)
    return None


# Iterative Deepening Search
def iterative_deepening():
    start = (3,3,'L')
    goal = (0,0,'R')

    depth = 0

    while True:
        print("Trying depth limit:", depth)
        result = dls(start, goal, depth, [start], set())
        if result is not None:
            return result
        depth += 1


result = iterative_deepening()

print("\nIterative Deepening Solution Path:")
for step in result:
    print(step)
