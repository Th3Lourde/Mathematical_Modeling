import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# nodes = [A,B,C,D,E,F,G,H]

G.add_nodes_from("ABCDEFGH")

# e = ('A', 'B', {'weight':1})

G.add_edge('A', 'B', distance=1)

# print(G.number_of_nodes())

# print(G.edges)

pos = nx.spring_layout(G)


nx.draw(G, pos)
nx.draw_networkx(G, pos=pos, with_labels=False)
nx.draw_networkx_edge_labels(G,pos)
plt.show()
