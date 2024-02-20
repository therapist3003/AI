import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, goal, visited, stack, limit):
    stack.append([start, 0])
    visited.append(start)
    
    while stack:
        if stack[-1][1] > limit:
            print('Depth-limit exceeded...')
            break
        explore_node = stack.pop()
        #print('Explore node: ', explore_node)
        if explore_node[0] == goal:
            #visited.append(explore_node)
            break
        depth = explore_node[1] + 1
        for neighbor in G.neighbors(explore_node[0]):
            if neighbor not in visited:
                #print('Unvisited neighbor: ', neighbor)
                stack.append([neighbor, depth])
                #print(stack)
                visited.append(neighbor)
                #print(visited)
                
    print(visited)

G = nx.Graph()

f = plt.figure(1)
G.add_edges_from([ ('S','A'), ('S','B'), ('A','C'), ('A','D'), ('C','E'), ('C','F'), ('D','G'), ('B','I'), ('B','J'), ('I','H')])

#plt.subplot(211)
print('Graph: ')

nx.draw_networkx(G)

visited = []
stack = []      

depth_limit = int(input('Enter depth-limit: '))
dfs(G, 'S', 'J', visited, stack, depth_limit)

g = plt.figure(2)
color_map = []
for node in G:
    if node in visited:
        color_map.append('orange')
    else:
        color_map.append('blue')
        
nx.draw(G, node_color=color_map, with_labels=True)
g.show()