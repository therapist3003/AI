from queue import PriorityQueue
import copy

visited = [] # Global list to store all visited states

def calc_heuristic(state_grid): # Calculates no. of misplaced tiles as heuristic
  misplaced = 0
  goal_state_grid = [[0,1,2], [3,4,5], [6,7,8]]
  for i in range(len(state_grid)):
    for j in range(len(state_grid)):
      if state_grid[i][j] != goal_state_grid[i][j] and state_grid[i][j] != 0:
        misplaced += 1

  return misplaced

def findIndexOf_0(state_grid):
  for i in range(len(state_grid)):
    for j in range(len(state_grid)):
      if state_grid[i][j] == 0:
        return [i,j]

def isVisited(state_grid):
  if state_grid not in visited:
    return 0
  else:
    return 1

def generate_children(row, col):
  directions = [[row-1,col], [row,col-1], [row+1,col], [row,col+1]]
  children = []
  for dir in directions:
    if dir[0] in range(3) and dir[1] in range(3):
      children.append(dir)

  return children

def a_star_with_misplaced_tiles(state_grid):
  heuristic_value = calc_heuristic(state_grid)
  queue = PriorityQueue()
  queue.put((heuristic_value, state_grid))

  iteration_count = 0

  while queue:
    (curr_heuristic, curr_state) = queue.get()

    visited.append(curr_state)
    iteration_count += 1

    print('Iteration: ', iteration_count)
    print('Current state:-')
    print(curr_state[0])
    print(curr_state[1])
    print(curr_state[2])

    print('Heuristic value: ', curr_heuristic)

    if curr_heuristic==0:
      print('Goal state reached !!')
      break

    row, col = findIndexOf_0(curr_state)

    children = generate_children(row, col)

    for child in children:
      temp_child = copy.deepcopy(curr_state)
      temp_child[row][col], temp_child[child[0]][child[1]] = temp_child[child[0]][child[1]], temp_child[row][col]
      child_heuristic = calc_heuristic(temp_child)

      if not isVisited(temp_child):
        queue.put((child_heuristic, temp_child))

initial_state = [[7,2,4], [5,0,6], [8,3,1]]
a_star_with_misplaced_tiles(initial_state)