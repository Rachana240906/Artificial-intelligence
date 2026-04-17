from collections import deque
import copy

# Variables
variables = ["P1", "P2", "P3", "P4", "P5", "P6"]

# Domains
domains = {
    "P1": {"R1", "R2", "R3"},
    "P2": {"R1", "R2", "R3"},
    "P3": {"R1", "R2", "R3"},
    "P4": {"R1", "R2", "R3"},
    "P5": {"R1", "R2", "R3"},
    "P6": {"R1", "R2", "R3"}
}

# Constraints (neighbors)
constraints = {
    "P1": ["P2", "P3", "P6"],
    "P2": ["P1", "P3", "P4"],
    "P3": ["P1", "P2", "P5"],
    "P4": ["P2", "P6"],
    "P5": ["P3", "P6"],
    "P6": ["P1", "P4", "P5"]
}

# Constraint: Xi != Xj
def is_consistent(x, y):
    return x != y


# REVISE function
def revise(domains, xi, xj):
    revised = False
    to_remove = set()

    for x in domains[xi]:
        # Check if there exists y in Dj such that x != y
        if not any(is_consistent(x, y) for y in domains[xj]):
            to_remove.add(x)

    if to_remove:
        domains[xi] -= to_remove
        revised = True

    return revised


# AC-3 Algorithm
def ac3(domains, constraints, trace_limit=5):
    queue = deque()

    # Initialize queue with all arcs
    for xi in constraints:
        for xj in constraints[xi]:
            queue.append((xi, xj))

    trace_count = 0

    while queue:
        xi, xj = queue.popleft()

        if trace_count < trace_limit:
            print(f"Checking Arc ({xi}, {xj})")

        if revise(domains, xi, xj):
            if trace_count < trace_limit:
                print(f" → Domain of {xi} revised: {domains[xi]}")
            if not domains[xi]:
                return False  # Failure

            for xk in constraints[xi]:
                if xk != xj:
                    queue.append((xk, xi))

        else:
            if trace_count < trace_limit:
                print(" → No change")

        trace_count += 1

    return True


# -----------------------------
# RUN 1: Without assignment
# -----------------------------
print("=== AC-3 without assignment ===")
domains_copy = copy.deepcopy(domains)
result = ac3(domains_copy, constraints)

print("\nFinal Domains:", domains_copy)
print("Arc Consistent:", result)


# -----------------------------
# RUN 2: With P1 = R1
# -----------------------------
print("\n=== AC-3 with P1 = R1 ===")
domains_copy2 = copy.deepcopy(domains)
domains_copy2["P1"] = {"R1"}

result2 = ac3(domains_copy2, constraints)

print("\nFinal Domains:", domains_copy2)
print("Arc Consistent:", result2)
