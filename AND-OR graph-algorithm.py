import random

# Possible states for each tile
DIRTY = "Dirty"
CLEAN = "Clean"

class VacuumWorld:
    def __init__(self, state):
        # state is a dict like {"A": "Dirty", "B": "Dirty"}
        self.state = state

    def apply_action(self, action):
        """
        Apply an action (Clean A or Clean B).
        Returns possible nondeterministic outcomes.
        """
        tile = action[-1]  # 'A' or 'B'
        other = "B" if tile == "A" else "A"
        outcomes = []

        if self.state[tile] == DIRTY:
            # Case 1: Cleans the tile
            new_state = self.state.copy()
            new_state[tile] = CLEAN
            outcomes.append(new_state)

            # Case 2: Cleans both tiles
            new_state2 = self.state.copy()
            new_state2[tile] = CLEAN
            new_state2[other] = CLEAN
            outcomes.append(new_state2)

        else:
            # Tile is clean, but dirt may be deposited
            new_state = self.state.copy()
            new_state[tile] = DIRTY
            outcomes.append(new_state)

            # Or nothing changes
            outcomes.append(self.state.copy())

        return outcomes


def goal_test(state):
    return state["A"] == CLEAN and state["B"] == CLEAN


def and_or_graph_search(state, actions, plan=None, visited=None):
    """
    Recursive AND-OR graph search.
    Returns a conditional plan (policy tree).
    """
    if visited is None:
        visited = set()
    if plan is None:
        plan = {}

    # Goal check
    if goal_test(state):
        return "Goal"

    # Avoid loops
    state_tuple = tuple(state.items())
    if state_tuple in visited:
        return None
    visited.add(state_tuple)

    # Try each action
    for action in actions:
        outcomes = VacuumWorld(state).apply_action(action)
        subplans = []
        for outcome in outcomes:
            subplan = and_or_graph_search(outcome, actions, plan, visited)
            if subplan is None:
                break
            subplans.append(subplan)

        # If all outcomes lead to a valid plan, record conditional plan
        if len(subplans) == len(outcomes):
            plan[state_tuple] = (action, subplans)
            return plan

    return None


# Initial state
initial_state = {"A": DIRTY, "B": DIRTY}
actions = ["CleanA", "CleanB"]

plan = and_or_graph_search(initial_state, actions)

print("Conditional Plan (Policy Tree):")
print(plan)
