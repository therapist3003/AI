import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start, goal, visited, queue):
    queue.append(start)
    visited.append(start)
    
    while queue:
        explore_node = queue.popleft()
        #print('Explore node: ', explore_node)
        if explore_node == goal:
            #visited.append(explore_node)
            break
        
        for neighbor in G.neighbors(explore_node):
            if neighbor not in visited:
                #print('Unvisited neighbor: ', neighbor)
                queue.append(neighbor)
                #print(stack)
                visited.append(neighbor)
                #print(visited)
                
    print(visited)

G = nx.Graph()

plt.figure(figsize=(9,12))
G.add_edges_from([ ('DSL','B'), ('DSL','C'), ('B','D'), ('B','E'), ('E','H'), ('E','Canteen'), ('C','F'), ('C','G'), ('G','J')])

plt.subplot(211)
print('Graph: ')

nx.draw_networkx(G)

visited = []
queue = deque()     

bfs(G, 'DSL', 'Canteen', visited, queue)