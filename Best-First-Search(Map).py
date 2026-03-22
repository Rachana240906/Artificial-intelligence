#Priority Queue 

class PriorityQueue:
    def __init__(self):
        self.data = []  

    def empty(self):
        return len(self.data) == 0

    # INSERT
    def put(self, item):
        self.data.append(item)
        self._bubble_up(len(self.data) - 1)

    # REMOVE MIN
    def get(self):
        if self.empty():
            return None

        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._bubble_down(0)
        return item

    # HEAP HELPERS
    def _bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i][0] < self.data[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _bubble_down(self, i):
        n = len(self.data)

        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if left < n and self.data[left][0] < self.data[smallest][0]:
                smallest = left

            if right < n and self.data[right][0] < self.data[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]


INF = 10**9

# 1. City table (state space)
cities = [
    "Chicago","Indianapolis","Columbus","Cleveland","Detroit","Buffalo",
    "Pittsburgh","Baltimore","Philadelphia","Syracuse",
    "New York","Boston","Providence","Portland"
]

n = len(cities)

# 2. Cost table (Adjacency Matrix)
# cost[i][j] = distance
# 0 means no edge
cost = [[0]*n for _ in range(n)]

def add(u, v, w):
    cost[u][v] = w
    cost[v][u] = w


add(0,4,283); add(0,3,345); add(0,1,182)
add(1,2,176)
add(2,3,144); add(2,6,185)
add(3,4,169); add(3,5,189); add(3,6,134)
add(4,5,256)
add(5,9,150)
add(6,7,247); add(6,8,305)
add(7,8,101)
add(8,10,97); add(8,9,253)
add(9,10,254); add(9,11,312)
add(10,11,215); add(10,12,181)
add(11,12,50); add(11,13,107)

# 3. Heuristic table h(n) (estimate to Boston)
def compute_heuristic(goal):

    dist = [INF]*n
    dist[goal] = 0

    pq = PriorityQueue()
    pq.put((0, goal))   
    while not pq.empty():

        d, u = pq.get()

        if d > dist[u]:
            continue

        for v in range(n):
            if cost[u][v] != 0:
                new_dist = d + cost[u][v]

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    pq.put((new_dist, v))

    return dist  

def best_first_search(start, goal, h):

    visited = [False]*n
    parent = [-1]*n

    frontier = PriorityQueue()
    frontier.put((h[start], start))

    explored_count = 0

    while not frontier.empty():

        _, state = frontier.get()

        if visited[state]:
            continue

        visited[state] = True
        explored_count += 1

        if state == goal:
            break

        for next_state in range(n):

            if cost[state][next_state] != 0 and not visited[next_state]:

                frontier.put((h[next_state], next_state))

                if parent[next_state] == -1:
                    parent[next_state] = state


    # reconstruct path 
    path = []
    cur = goal
    total_cost = 0

    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    for i in range(len(path)-1):
        total_cost += cost[path[i]][path[i+1]]

    return path, total_cost, explored_count


start = 0      
goal  = 11    

h = compute_heuristic(goal)

path, dist, explored = best_first_search(start, goal, h)

print("Heuristic values:")
for i in range(n):
    print(cities[i], ":", h[i])

print("\nPath:")
for p in path:
    print(cities[p], end=" -> ")

print("\nTotal distance:", dist, "miles")
print("Nodes explored:", explored)
