# import networkx as nx
# import matplotlib.pyplot as plt
# import random
#
# # Set up a graph with random edges and weights
#
# G = nx.barabasi_albert_graph(6, 2, seed= 3214562)
# for u,v in G.edges():
#     G[u][v]['weight'] = int(random.random() * 10)
#
# pos = nx.spring_layout(G)
#
# nx.draw(G, pos)
# nx.draw_networkx_edge_labels(G,pos)
# plt.show()
import matplotlib.pyplot as plt
import networkx as nx

# Define a graph
G = nx.Graph()




G.add_edges_from([(1,2,{'weight':10, 'val':0.1}),
                  (1,4,{'weight':30, 'val':0.3}),
                  (2,3,{'weight':50, 'val':0.5}),
                  (2,4,{'weight':60, 'val':0.6}),
                  (3,4,{'weight':80, 'val':0.8})])
# generate positions for the nodes
pos = nx.spring_layout(G, weight=None)

# create the dictionary with the formatted labels
edge_labels = {i[0:2]:'${}'.format(i[2]['weight']) for i in G.edges(data=True)}

# create some longer node labels
node_labels = {n:"this is node {}".format(n) for n in range(1,5)}


# draw the graph
nx.draw_networkx(G, pos=pos, with_labels=False)

# print(pos.iteritems())

# a = {k:[v[0],v[1]+0.4]}

# # draw the custom node labels
# shifted_pos = {k:[v[0],v[1]+.04] for k,v in list(pos.keys())}
shifted_pos = {k:[v[0],v[1]+.04] for k,v in pos.items()}
node_label_handles = nx.draw_networkx_labels(G, pos=shifted_pos,
        labels=node_labels)

# add a white bounding box behind the node labels
[label.set_bbox(dict(facecolor='white', edgecolor='none')) for label in
        node_label_handles.values()]

# add the custom egde labels
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)

# Axes settings (make the spines invisible, remove all ticks and set title)
ax = plt.gca()
[sp.set_visible(False) for sp in ax.spines.values()]
ax.set_xticks([])
ax.set_yticks([])

plt.show()
