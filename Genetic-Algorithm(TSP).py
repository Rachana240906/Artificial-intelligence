import random

cities = ['A','B','C','D','E','F','G','H']

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


# ----------------------------
# Cost Function
# ----------------------------
def tour_cost(tour):
    cost = 0
    for i in range(n-1):
        cost += cost_matrix[tour[i]][tour[i+1]]
    cost += cost_matrix[tour[-1]][tour[0]]
    return cost


# ----------------------------
# Create random chromosome
# ----------------------------
def create_chromosome():
    tour = list(range(n))
    random.shuffle(tour)
    return tour


# ----------------------------
# Selection
# ----------------------------
def selection(population):
    return random.choice(population)


# ----------------------------
# One Point Crossover
# ----------------------------
def one_point_crossover(p1, p2):

    point = random.randint(1,n-2)

    child = p1[:point]

    for city in p2:
        if city not in child:
            child.append(city)

    return child


# ----------------------------
# Two Point Crossover
# ----------------------------
def two_point_crossover(p1,p2):

    p,q = sorted(random.sample(range(n),2))

    child = [-1]*n

    child[p:q] = p1[p:q]

    idx = 0
    for city in p2:
        if city not in child:
            while child[idx] != -1:
                idx += 1
            child[idx] = city

    return child


# ----------------------------
# Mutation
# ----------------------------
def mutate(tour):

    i,j = random.sample(range(n),2)
    tour[i],tour[j] = tour[j],tour[i]

    return tour


# ----------------------------
# Genetic Algorithm
# ----------------------------
def genetic_algorithm(crossover_type="one", pop_size=20, generations=200):

    population = [create_chromosome() for _ in range(pop_size)]

    best_tour = None
    best_cost = float('inf')

    for g in range(generations):

        new_population = []

        for _ in range(pop_size):

            parent1 = selection(population)
            parent2 = selection(population)

            if crossover_type == "one":
                child = one_point_crossover(parent1,parent2)
            else:
                child = two_point_crossover(parent1,parent2)

            if random.random() < 0.1:
                child = mutate(child)

            new_population.append(child)

            cost = tour_cost(child)

            if cost < best_cost:
                best_cost = cost
                best_tour = child

        population = new_population

    return best_tour,best_cost


# ----------------------------
# Run Experiments
# ----------------------------
for method in ["one","two"]:

    best_tour,best_cost = genetic_algorithm(method)

    path = [cities[i] for i in best_tour]
    path.append(path[0])

    print("\nCrossover:",method)
    print("Best Path:", " -> ".join(path))
    print("Cost:",best_cost)
