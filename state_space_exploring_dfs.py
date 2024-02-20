import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, goal, visited, stack):
    stack.append(start)
    visited.append(start)
    
    while stack:
        explore_node = stack.pop()
        #print('Explore node: ', explore_node)
        if explore_node == goal:
            #visited.append(explore_node)
            break
        
        for neighbor in G.neighbors(explore_node):
            if neighbor not in visited:
                #print('Unvisited neighbor: ', neighbor)
                stack.append(neighbor)
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
stack = []      

dfs(G, 'DSL', 'Canteen', visited, stack)