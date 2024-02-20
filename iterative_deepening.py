import networkx as nx
import matplotlib.pyplot as plt


def depth_lim_search(graph, start, target, maxDepth):
    if start == target :
        return True
 
    if maxDepth <= 0 : #Updated inside next for loop
        return False
 
    for neighbor in G.neighbors(start):
            if(depth_lim_search(neighbor, target, maxDepth-1)):
                return True
    return False
 
def iterative_dfs(graph, start, target, maxDepth):
    for i in range(maxDepth):
        if (depth_lim_search(graph, start, target, i)):
            return True
    return False

G = nx.Graph()

plt.figure(figsize=(9,12))
G.add_edges_from([ ('A','B'), ('A','C'), ('B','D'), ('B','E'), ('D','H'), ('D','I'), ('C','F'), ('C','G'), ('F','K')])

plt.subplot(211)
print('Graph: ')

nx.draw_networkx(G)

iterative_dfs(G, 'A', 'G', 3)