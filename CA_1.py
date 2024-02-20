from collections import deque

# Define the initial state and the goal state
initial_state = (('left', 'left', 'left', 'left'), 'left')  # (Chloe, Lexa, Jon, Chloe's agent, Lexa's agent, Jon's agent, boat)
goal_state = (('right', 'right', 'right', 'right'), 'right')

# Define the actions that can be taken by the boat
actions = [
    (0,),          # Boat crosses with Chloe
    (1,),          # Boat crosses with Lexa
    (2,),          # Boat crosses with Jon
    (3, 4),        # Boat crosses with Chloe and Lexa
    (3, 5),        # Boat crosses with Chloe and Jon
    (4, 5)         # Boat crosses with Lexa and Jon
]

# Check if a state is valid (no trust issues violated)
def is_valid(state):
    # Agents not comfortable leaving their movie star with any other agents
    chloe_pos, lexa_pos, jon_pos, chloe_agent_pos, lexa_agent_pos, jon_agent_pos, boat_pos = state
    if (chloe_agent_pos != lexa_agent_pos) and (chloe_pos != lexa_pos) and (boat_pos == chloe_pos or boat_pos == lexa_pos):
        return False
    if (chloe_agent_pos != jon_agent_pos) and (chloe_pos != jon_pos) and (boat_pos == chloe_pos or boat_pos == jon_pos):
        return False
    if (lexa_agent_pos != jon_agent_pos) and (lexa_pos != jon_pos) and (boat_pos == lexa_pos or boat_pos == jon_pos):
        return False
    return True

# Perform BFS to find the solution
def bfs(initial_state, goal_state, actions):
    visited = set()
    queue = deque([(initial_state, [])])  # Initialize queue with initial state and empty path

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path  # Return the path when goal state is reached

        if state not in visited:
            visited.add(state)
            for action in actions:
                new_state = tuple(state[i] if i not in action else ('left' if state[i] == 'right' else 'right') for i in range(len(state) - 1)) + (state[-1],)
                if is_valid(new_state):
                    new_path = path + [new_state]
                    queue.append((new_state, new_path))
    return None  # No solution found

# Solve the problem
solution = bfs(initial_state, goal_state, actions)

# Print the solution
if solution:
    print("Solution found:")
    for i, state in enumerate(solution):
        print(f"Step {i+1}: {state}")
else:
    print("No solution exists.")
