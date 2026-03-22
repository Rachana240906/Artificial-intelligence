#Priority Queue

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    # insert
    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    # remove minimum
    def pop(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap)-1)
        item = self.heap.pop()
        self._bubble_down(0)
        return item

    def _bubble_up(self, i):
        parent = (i - 1) // 2

        while i > 0 and self.heap[i][0] < self.heap[parent][0]:
            self._swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def _bubble_down(self, i):
        n = len(self.heap)

        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Grid + Best First Search

grid = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,1,0,0,0,0,0,1],
[1,0,1,1,1,0,0,1,0,1,1,1,0,1],
[1,0,1,0,0,0,0,0,0,0,0,1,0,1],
[1,0,1,0,1,1,1,1,1,1,0,1,0,1],
[1,0,0,0,0,0,0,0,0,1,0,0,0,1],
[1,1,1,1,1,1,1,1,0,1,1,1,0,1],
[1,0,0,0,0,0,0,1,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

rows = len(grid)
cols = len(grid[0])

start = (5,1)
goal  = (1,12)


def h(x, y):
    return abs(x - goal[0]) + abs(y - goal[1])


def best_first():

    visited = [[False]*cols for _ in range(rows)]
    parent  = [[(-1,-1)]*cols for _ in range(rows)]

    pq = PriorityQueue()
    pq.push((h(*start), start))

    explored = 0
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    while not pq.is_empty():

        _, (x,y) = pq.pop()

        if visited[x][y]:
            continue

        visited[x][y] = True
        explored += 1

        if (x,y) == goal:
            break

        for dx, dy in moves:
            nx, ny = x+dx, y+dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    pq.push((h(nx,ny), (nx,ny)))
                    parent[nx][ny] = (x,y)

    # reconstruct path
    path = []
    cur = goal
    while cur != (-1,-1):
        path.append(cur)
        cur = parent[cur[0]][cur[1]]

    path.reverse()

    return path, explored


path, explored = best_first()

print("Evacuation Path:", path)
print("Cells explored:", explored)
