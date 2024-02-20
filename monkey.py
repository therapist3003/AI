class State:
    def __init__(self, position, on_floor, box_position, has):
        self.position = position
        self.on_floor = on_floor
        self.box_position = box_position
        self.has = has

def grasp(state):
    return State(state.position, state.on_floor, state.box_position, "has")

def climb(state):
    return State(state.position, "onbox", state.position, state.has)

def drag(state, new_position):
    return State(new_position, "onfloor", new_position, state.has)

def walk(state, new_position):
    return State(new_position, "onfloor", state.box_position, state.has)

def canget(state, path=None):
    if path is None:
        path = []
    if state.has == "has":
        path.append(state)
        return True, path
    for action in [grasp, climb, drag, walk]:
        next_state = action(state)
        found, path = canget(next_state, path)
        if found:
            path.append(state)
            return True, path
    return False, path

# Example usage
initial_state = State("middle", "onbox", "middle", "hasnot")
found, path = canget(initial_state)
if found:
    print("Steps to get the object:")
    for step in reversed(path):
        print(f"Position: {step.position}, On Floor: {step.on_floor}, Box Position: {step.box_position}, Has: {step.has}")
else:
    print("Object cannot be obtained.")
