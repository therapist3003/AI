def transfer(state, source, target):
    # Assumption: source, target 0..2, source != target
    s = state[:] # clone
    if s[source] == 0 or s[target] == capacity[target]:
        return s  # source empty or target full
    free = capacity[target] - s[target]
    if s[source] <= free: # source has enough space in target
        s[target] += s[source]
        s[source] = 0
    else:  # target is filled-up
        s[target] = capacity[target]
        s[source] -= free
    return s

def getNeighbours(node):
# returns list of neighbours
    neighbours = []
    t = transfer(node, 0, 1) # from 0 to 1
    if t not in neighbours:
       neighbours.append(t)
    t = transfer(node, 0, 2) # from 0 to 2
    if t not in neighbours:
        neighbours.append(t)
    t = transfer(node, 1, 0) # from 1 to 0
    if  t not in neighbours:
        neighbours.append(t)
    t = transfer(node, 1, 2) # from 1 to 2
    if t not in neighbours:
        neighbours.append(t)
    t = transfer(node, 2, 0) # from 2 to 0
    if t not in neighbours:
        neighbours.append(t)
    t = transfer(node, 2, 1) # from 2 to 1
    if t not in neighbours:
        neighbours.append(t)
    return neighbours

def search(node):
    global nbSolution    
    visited.append(node)

    # Check for solution
    if node == targetNode:
        nbSolution += 1
        print (nbSolution, ". Route:", visited, ". Length:", len(visited))
        
    for s in getNeighbours(node):
        if s not in visited: 
            search(s)
    visited.pop() 
 
capacity = [8, 5, 3]
startNode = [8, 0, 0]
targetNode = [4, 4, 0]
nbSolution = 0
visited = []
search(startNode)
print("Done. Find the best  solution!")