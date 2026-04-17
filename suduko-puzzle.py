from collections import deque
import copy

# -----------------------------
# Parse Sudoku Input
# -----------------------------
grid = [
[0,0,0,0,0,6,0,0,0],
[0,5,9,0,0,0,0,0,8],
[2,0,0,0,0,8,0,0,0],
[0,4,5,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0],
[0,0,6,0,0,3,0,5,0],
[0,0,0,0,0,7,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,2]
]

# -----------------------------
# Variables
# -----------------------------
variables = [(r, c) for r in range(9) for c in range(9)]

# -----------------------------
# Domains
# -----------------------------
domains = {}
for r in range(9):
    for c in range(9):
        if grid[r][c] == 0:
            domains[(r,c)] = set(range(1,10))
        else:
            domains[(r,c)] = {grid[r][c]}

# -----------------------------
# Neighbors (constraints)
# -----------------------------
neighbors = {v: set() for v in variables}

for r in range(9):
    for c in range(9):
        cell = (r,c)

        # Row + Column
        for i in range(9):
            if i != c:
                neighbors[cell].add((r,i))
            if i != r:
                neighbors[cell].add((i,c))

        # 3x3 Box
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if (i,j) != cell:
                    neighbors[cell].add((i,j))

# -----------------------------
# Revise
# -----------------------------
def revise(domains, xi, xj):
    removed = 0
    to_remove = set()

    for x in domains[xi]:
        if not any(x != y for y in domains[xj]):
            to_remove.add(x)

    if to_remove:
        domains[xi] -= to_remove
        removed = len(to_remove)

    return removed

# -----------------------------
# AC-3 Algorithm
# -----------------------------
def ac3(domains, neighbors):
    queue = deque()

    # Generate all arcs
    for xi in variables:
        for xj in neighbors[xi]:
            queue.append((xi, xj))

    total_removed = 0

    while queue:
        xi, xj = queue.popleft()

        removed = revise(domains, xi, xj)

        if removed > 0:
            total_removed += removed

            if len(domains[xi]) == 0:
                return False, total_removed

            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True, total_removed

# -----------------------------
# Run AC-3
# -----------------------------
domains_copy = copy.deepcopy(domains)

consistent, removed_count = ac3(domains_copy, neighbors)

# -----------------------------
# Output Results
# -----------------------------
print("Total values removed:", removed_count)
print("Arc Consistent:", consistent)

print("\nDomain Size Grid:")
for r in range(9):
    row = []
    for c in range(9):
        row.append(str(len(domains_copy[(r,c)])))
    print(" ".join(row))

# Check final condition
all_singleton = all(len(domains_copy[v]) == 1 for v in variables)

if not consistent:
    print("\nResult: ❌ Some domain became EMPTY → Unsolvable")
elif all_singleton:
    print("\nResult: ✅ Fully solved by AC-3")
else:
    print("\nResult: ⚠️ Partially reduced (needs backtracking)")
