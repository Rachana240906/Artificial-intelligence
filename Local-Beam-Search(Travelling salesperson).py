import random

# Cities
cities = ['A','B','C','D','E','F','G','H']

# Cost matrix
cost_matrix = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

n = len(cities)


# -------------------------------------------------
# Calculate tour cost
# -------------------------------------------------
def tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += cost_matrix[tour[i]][tour[i+1]]
    cost += cost_matrix[tour[-1]][tour[0]]   # return to start
    return cost


# -------------------------------------------------
# Generate neighbors by swapping two cities
# -------------------------------------------------
def generate_neighbors(tour):
    neighbors = []
    for i in range(1,n):
        for j in range(i+1,n):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            neighbors.append(new_tour)
    return neighbors


# -------------------------------------------------
# Local Beam Search
# -------------------------------------------------
def local_beam_search(k, max_iterations=100):

    # generate k random tours
    beams = []
    for _ in range(k):
        tour = list(range(n))
        random.shuffle(tour)
        beams.append(tour)

    best_tour = None
    best_cost = float('inf')

    for iteration in range(max_iterations):

        all_neighbors = []

        for tour in beams:

            cost = tour_cost(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour

            neighbors = generate_neighbors(tour)
            all_neighbors.extend(neighbors)

        # sort neighbors by cost
        all_neighbors.sort(key=lambda x: tour_cost(x))

        # keep best k states
        beams = all_neighbors[:k]

    return best_tour, best_cost


# -------------------------------------------------
# Run experiments for different beam widths
# -------------------------------------------------
beam_values = [3,5,10]

for k in beam_values:

    best_tour, best_cost = local_beam_search(k)

    city_path = [cities[i] for i in best_tour]
    city_path.append(city_path[0])  # return to start

    print("\nBeam Width k =",k)
    print("Best Tour:", " -> ".join(city_path))
    print("Total Cost:", best_cost)
