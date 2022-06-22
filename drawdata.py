import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()
readfile=open("vendor.txt", "r")
for line in readfile:
    spline= line.split("==")
    G.add_edge(spline[0], spline[1])
pos = nx.circular_layout(G)
nx.draw(G, pos, node_color='r', with_labels=True)

plt.show()
