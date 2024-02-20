from collections import deque

# Possible actions
'''
    1. Fill first jug -> (capacity1, y)
    2. Fill second jug -> (x, capacity2)
    3. Empty first jug -> (0, y)
    4. Empty second jug -> (x, 0)
    5. Pour from second jug to first jug
        Case1: Second becomes empty, completely filling jug1 -> (capacity1, 0)
        Case2: Second has some quantity remaining, completely filling jug1 -> (capacity1, x + y - capacity1)
        Case3: Second becomes empty, partially filling jug1 -> (x+y, 0)
        Case4: Second has some quantity remaining, partially filling jug1 -> (x+y, x+y-capacity1)
    6. Pour from first jug to second jug
        Case1: First becomes empty, completely filling jug2 -> (0, capacity2)
        Case2: First has some quantity remaining, completely filling jug2 -> (x+y-capacity2, capacity2)
        Case3: First becomes empty, partially filling jug2 -> (0, x+y)
        Case4: First has some quantity remaining, partially filling jug2 -> (x+y-capacity2, x+y)
'''
def water_jug_problem(capacity1, capacity2, target):
    # initial state (x, y) where x and y are the amounts of water in the two jugs
    state = (0, 0)
    parent_dict = {}
    queue = deque()
    queue.append(state)
    while queue:
        state = queue.popleft()
        if state == (target, 0):
            # goal state reached
            path = [state]
            while state in parent_dict:
                if state == (0,0):
                    break
                state = parent_dict[state]
                path.append(state)
            path.reverse()
            return path
        x, y = state
        # generate all possible successor states
        states = [(capacity1, y), (x, capacity2), (0, y), (x, 0), (min(x + y, capacity1), max(0, x + y - capacity1)), (max(0, y + x - capacity2), min(y + x, capacity2))]
        for new_state in states:
            if new_state not in parent_dict:
                parent_dict[new_state] = state
                queue.append(new_state)
    return None

# example
capacity1 = 4
capacity2 = 3
target = 2
path = water_jug_problem(capacity1, capacity2, target)

if path is None:
    print("No solution found.")
else:
    for state in path:
        print(state)