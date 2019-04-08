
'''
Prompt:
Moving Rocks

Evacuating three sites (yield):
A 150
B 400
C 325

Filling four sites (need):
D 175
E 125
F 225
G 450

If we need more dirt:
We can buy dirt from source H at $5 per cubic yard

Cost of shipping dirt = $20 per mile
Amount of dirt being shipped: 10 cubic yards

Table of distances between sources and destinations:

Source     D(5)    E(6)    F(7)     G(8)
A = 1       5       2       6       10
B = 2       4       5       7       5
C = 3       7       6       4       4
H = 4       9       10      6       2

A = 1
B = 2
C = 3
H = 4
D = 5
E = 6
F = 7
G = 8

What the graph should show:
Source      D(5)      E(6)    F(7)     G(8)
A = 1       100       40      120      200
B = 2       80        100     140      100
C = 3       140       120     80       80
H = 4       180       200     120      40



'''



import matplotlib.pyplot as plt
import pulp as lp
import networkx as nx

def test():
    # Define a graph
    G = nx.Graph()

    # G=nx.fast_gnp_random_graph(20,0.2)

    source_nodes = [1,2,3]
    money_source_nodes = [4]
    deposit_nodes = [5,6,7,8]

    G.add_edges_from([(1,5,{'weight':5, 'val':0.05}),
                      (1,6,{'weight':2, 'val':0.02}),
                      (1,7,{'weight':6, 'val':0.06}),
                      (1,8,{'weight':10, 'val':0.10}),
                      (2,5,{'weight':4, 'val':0.04}),
                      (2,6,{'weight':5, 'val':0.05}),
                      (2,7,{'weight':7, 'val':0.07}),
                      (2,8,{'weight':5, 'val':0.05}),
                      (3,5,{'weight':7, 'val':0.07}),
                      (3,6,{'weight':6, 'val':0.06}),
                      (3,7,{'weight':4, 'val':0.04}),
                      (3,8,{'weight':4, 'val':0.04}),
                      (4,5,{'weight':9, 'val':0.09}),
                      (4,6,{'weight':10, 'val':0.10}),
                      (4,7,{'weight':6, 'val':0.06}),
                      (4,8,{'weight':2, 'val':0.02}),
                      ])

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G,pos=pos,nodelist=source_nodes, node_color='blue', label='Source')
    nx.draw_networkx_nodes(G,pos=pos,nodelist=money_source_nodes, node_color='black', label='Source Cost')
    nx.draw_networkx_nodes(G,pos=pos,nodelist=deposit_nodes, node_color='green', label='Deposit')
    # nx.draw_networkx_nodes(G,pos=pos,nodelist=yellowgreennodes, node_color='yellowgreen', label='yellowgreen nodes')

    # color map so we can color nodes differently
    color_map = []

    for i in range(8):
        if (i < 3):
            color_map.append('blue')
        if (i == 3):
            color_map.append('black')
        if (i > 3):
            color_map.append('green')

    print(color_map)

    # draw the graph
    nx.draw_networkx(G, pos=pos, with_labels=False, node_color=color_map, size=9)

    edge_labels = {i[0:2]:'${}'.format(i[2]['weight']*20) for i in G.edges(data=True)}

    labels = ["A","B","C","F","D","E","H","G"]

    node_labels = {n:"{}".format(labels[n-1]) for n in range(1, len(labels)+1)}

    # draw the custom node labels
    shifted_pos = {k:[v[0],v[1]+.04] for k,v in pos.items()}
    node_label_handles = nx.draw_networkx_labels(G, pos=shifted_pos,
            labels=node_labels)

    # add a white bounding box behind the node labels
    [label.set_bbox(dict(facecolor='white', edgecolor='black')) for label in
            node_label_handles.values()]


    # print(color_map)
    # nx.draw(G,node_color = color_map,with_labels = True)

    # add the custom edge labels
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, node_color=color_map)

    plt.legend(numpoints = 1)

    ax = plt.gca()
    [sp.set_visible(False) for sp in ax.spines.values()]
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

test()


def main():

    # Define a graph
    G = nx.Graph()

    G.add_edges_from([(1,5,{'weight':5, 'val':0.05}),
                      (1,6,{'weight':2, 'val':0.02}),
                      (1,7,{'weight':6, 'val':0.06}),
                      (1,8,{'weight':10, 'val':0.10}),
                      (2,5,{'weight':4, 'val':0.04}),
                      (2,6,{'weight':5, 'val':0.05}),
                      (2,7,{'weight':7, 'val':0.07}),
                      (2,8,{'weight':5, 'val':0.05}),
                      (3,5,{'weight':7, 'val':0.07}),
                      (3,6,{'weight':6, 'val':0.06}),
                      (3,7,{'weight':4, 'val':0.04}),
                      (3,8,{'weight':4, 'val':0.04}),
                      (4,5,{'weight':9, 'val':0.09}),
                      (4,6,{'weight':10, 'val':0.10}),
                      (4,7,{'weight':6, 'val':0.06}),
                      (4,8,{'weight':2, 'val':0.02}),
                      ])

                      # (,,{'weight':, 'val':}),

    # generate positions for the nodes
    pos = nx.spring_layout(G, weight=None)

    # create the dictionary with the formatted labels
    edge_labels = {i[0:2]:'${}'.format(i[2]['weight']) for i in G.edges(data=True)}

    # create some longer node labels
    # node_labels = {n:"this is node {}".format(n) for n in range(1,5)}

    labels = ["A","B","C","H","D","E","F","G"]

    node_labels = {n:"{}".format(labels[n-1]) for n in range(1, len(labels)+1)}

    # color map so we can color nodes differently
    color_map = []

    for i in range(8):
        if (i < 3):
            color_map.append('blue')
        if (i == 3):
            color_map.append('black')
        if (i > 3):
            color_map.append('green')

    # draw the graph
    nx.draw_networkx(G, pos=pos, with_labels=False, node_color=color_map)

    # draw the custom node labels
    shifted_pos = {k:[v[0],v[1]+.04] for k,v in pos.items()}
    node_label_handles = nx.draw_networkx_labels(G, pos=shifted_pos,
            labels=node_labels)

    # add a white bounding box behind the node labels
    [label.set_bbox(dict(facecolor='white', edgecolor='black')) for label in
            node_label_handles.values()]


    # print(color_map)
    # nx.draw(G,node_color = color_map,with_labels = True)

    # add the custom edge labels
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, node_color=color_map)

    # Axes settings (make the spines invisible, remove all ticks and set title)
    ax = plt.gca()
    [sp.set_visible(False) for sp in ax.spines.values()]
    ax.set_xticks([])
    ax.set_yticks([])

    # plt.legend(('1','2','3','4','5','6','7','8'))
    # ax.scatter(1, 2, c='blue', marker='x')
    # ax.scatter(2, 3, c='red', marker='o')
    # plt.legend(('1','2'), loc = 2, )
    # plt.legend(['A simple line','Another line'], loc = 2)

    plt.show()

# main()
