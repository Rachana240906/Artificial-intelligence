import random

# Environment
rooms = {
    "A": random.choice(["Clean", "Dirty"]),
    "B": random.choice(["Clean", "Dirty"]),
    "C": random.choice(["Clean", "Dirty"])
}

location = "A"
performance = 0


# Rule Table
rules = {
    ("A", "Dirty"): "SUCK",
    ("B", "Dirty"): "SUCK",
    ("C", "Dirty"): "SUCK",

    ("A", "Clean"): "RIGHT",
    ("B", "Clean"): "RIGHT",
    ("C", "Clean"): "LEFT"
}


# Actuator
def move(loc, action):
    if action == "RIGHT":
        if loc == "A": return "B"
        if loc == "B": return "C"
    if action == "LEFT":
        if loc == "C": return "B"
        if loc == "B": return "A"
    return loc


# Simulation
print("Initial Rooms:", rooms)
print()

for step in range(5):

    percept = (location, rooms[location])

    action = rules[percept]

    print(f"Step {step}")
    print("Percept:", percept, " Action:", action)

    if action == "SUCK":
        rooms[location] = "Clean"
        performance += 1
    else:
        location = move(location, action)
        performance -= 1

    print("New Location:", location)
    print("Rooms:", rooms)
    print("Performance:", performance)

print("\nFinal Performance Score:", performance)
