from collections import deque

# Graph with step costs
graph = {
    "Syracuse": {"Buffalo": 150, "Boston": 312, "Philadelphia": 253},
    "Buffalo": {"Syracuse": 150, "Detroit": 256, "Cleveland": 189, "Pittsburgh": 215},
    "Detroit": {"Chicago": 283, "Buffalo": 256, "Cleveland": 169},
    "Chicago": {"Detroit": 283, "Cleveland": 345, "Indianapolis": 182},
    "Cleveland": {"Chicago": 345, "Detroit": 169, "Buffalo": 189, "Pittsburgh": 134, "Columbus": 144},
    "Indianapolis": {"Chicago": 182, "Columbus": 176},
    "Columbus": {"Indianapolis": 176, "Cleveland": 144, "Pittsburgh": 185},
    "Pittsburgh": {"Buffalo": 215, "Cleveland": 134, "Columbus": 185, "Baltimore": 247, "Philadelphia": 305},
    "Baltimore": {"Pittsburgh": 247, "Philadelphia": 101},
    "Philadelphia": {"Syracuse": 253, "Pittsburgh": 305, "Baltimore": 101, "New York": 97},
    "New York": {"Philadelphia": 97, "Boston": 215, "Providence": 181},
    "Boston": {"Syracuse": 312, "New York": 215, "Providence": 50, "Portland": 107},
    "Providence": {"Boston": 50, "New York": 181},
    "Portland": {"Boston": 107}
}

# DFS
def dfs(graph, current, destination, visited, cost):
    if current == destination:
        print("DFS Step Cost:", cost)
        return

    visited.add(current)

    for neighbour, step_cost in graph[current].items():
        if neighbour not in visited:
            dfs(graph, neighbour, destination, visited, cost + step_cost)

    visited.remove(current)

# BFS
def bfs(graph, source, destination):
    queue = deque()
    queue.append((source, 0, {source}))

    while queue:
        city, cost, visited = queue.popleft()

        if city == destination:
            print("BFS Step Cost:", cost)
            continue

        for neighbour, step_cost in graph[city].items():
            if neighbour not in visited:
                queue.append((neighbour, cost + step_cost, visited | {neighbour}))


source = "Syracuse"
destination = "Chicago"

print("DFS Results:")
dfs(graph, source, destination, set(), 0)

print("\nBFS Results:")
bfs(graph, source, destination)
