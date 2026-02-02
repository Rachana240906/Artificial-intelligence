import random
from collections import deque
names = ["Raj", "Sunil", "NehaOrange", "Priya", "Aarav", "Akash", "Sneha", "Rahul", "ArjunMan", "Maya","ArjunChild", "Pooja", "NehaPink"]

graph = {
    "Raj": ["Sunil", "NehaO"],
    "Priya": ["Raj", "Aarav", "Akash"],
    "Aarav": ["NehaO", "NehaP", "ArjunMan"],
    "Sunil": ["Sneha", "Maya", "Akash", "Raj"],
    "Akash": ["Sunil", "Priya"],
    "NehaO": ["Akash", "Aarav", "Raj", "Sneha"],
    "NehaP": ["NehaO", "Rahul", "Priya", "Aarav", "ArjunMan"],
    "Sneha": ["Rahul", "Maya", "Sunil", "NehaO"],
    "Rahul": ["Sneha", "NehaP", "NehaO", "ArjunMan", "Pooja"],
    "ArjunMan": ["NehaP", "Rahul", "Aarav"],
    "Maya": ["Sunil", "Rahul","Sneha", "ArjunChild"],
    "ArjunChild": ["Pooja", "Maya"],
    "Pooja": ["ArjunMan", "ArjunChild", "Rahul"]
}

# BFS
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    print("BFS Tree (Parent -> Child):")
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
                print(f"{u} -> {v}")

# DFS
def dfs(graph, start):
    visited = set()
    print("\nDFS Tree (Parent -> Child):")
    dfs_util(graph, start, visited)

def dfs_util(graph, u, visited):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            print(f"{u} -> {v}")
            dfs_util(graph, v, visited)

start_node = random.choice(names)
bfs(graph, start_node)
dfs(graph, start_node)
