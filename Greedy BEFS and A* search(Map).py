graph = {
    "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
    "Detroit": [("Chicago", 283), ("Cleveland", 169), ("Buffalo", 256)],
    "Cleveland": [("Chicago", 345), ("Detroit", 169), ("Columbus", 144), ("Pittsburgh", 189)],
    "Indianapolis": [("Chicago", 182), ("Columbus", 176)],
    "Columbus": [("Indianapolis", 176), ("Cleveland", 144), ("Pittsburgh", 185)],
    "Pittsburgh": [("Cleveland", 189), ("Columbus", 185), ("Buffalo", 215), ("Philadelphia", 305)],
    "Buffalo": [("Detroit", 256), ("Pittsburgh", 215), ("Syracuse", 150)],
    "Syracuse": [("Buffalo", 150), ("Boston", 312), ("New York", 254)],
    "Boston": [("Syracuse", 312), ("Providence", 50), ("Portland", 107)],
    "Providence": [("Boston", 50), ("New York", 181)],
    "New York": [("Providence", 181), ("Syracuse", 254), ("Philadelphia", 97)],
    "Philadelphia": [("New York", 97), ("Baltimore", 101), ("Pittsburgh", 305)],
    "Baltimore": [("Philadelphia", 101)],
    "Portland": [("Boston", 107)]
}
h = {
    "Boston": 0,
    "Providence": 50,
    "Portland": 107,
    "New York": 215,
    "Philadelphia": 270,
    "Baltimore": 360,
    "Syracuse": 260,
    "Buffalo": 400,
    "Pittsburgh": 470,
    "Cleveland": 550,
    "Columbus": 640,
    "Detroit": 610,
    "Indianapolis": 780,
    "Chicago": 860
}
def greedy_best_first_search(graph, h, start, goal):
    queue = [(start, [start], 0)]
    explored = []
    visited = set()

    while queue:
        min_index = 0
        for i in range(1, len(queue)):
            if h[queue[i][0]] < h[queue[min_index][0]]:
                min_index = i
        current, path, cost = queue.pop(min_index)

        if current not in visited:
            visited.add(current)
            explored.append(current)

        if current == goal:
            return path, cost, explored


        for neighbour, weight in graph[current]:
            if neighbour not in explored:
                queue.append((neighbour, path + [neighbour], cost + weight))

    return None, float('inf'), explored


def a_star_search(graph, h, start, goal):
    open_list = [(start, [start], 0)]   
    g_cost = {start: 0}
    explored = []
    visited = set()

    while open_list:
        # Find node with smallest f(n)
        min_index = 0
        for i in range(1, len(open_list)):
            node_i = open_list[i][0]
            node_min = open_list[min_index][0]

            f_i = g_cost[node_i] + h[node_i]
            f_min = g_cost[node_min] + h[node_min]

            if f_i < f_min:
                min_index = i

        current, path, current_g = open_list.pop(min_index)

        if current not in visited:
            visited.add(current)
            explored.append(current)

            if current == goal:
                return path, current_g, explored

            for neighbor, weight in graph[current]:
                new_g = current_g + weight

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    open_list.append((neighbor, path + [neighbor], new_g))

    return None, float("inf"), explored

greddy_path, greedy_cost, explored = greedy_best_first_search(graph, h, "Chicago", "Boston")
print("Greedy Best-First Search Path:", greddy_path)
print("Greedy Best-First Search Cost:", greedy_cost)
print("Explored Nodes:", explored)

a_star_path, a_star_cost, explored = a_star_search(graph, h, "Chicago", "Boston")
print("A* Search Path:", a_star_path)
print("A* Search Cost:", a_star_cost)
print("Explored Nodes:", explored)
