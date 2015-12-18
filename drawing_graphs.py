__author__ = 'andrewwhiter'
# comments = Max

import csv
def getEdgeListFromCSVfile(filename):
    ''' returns a list of graph edges eg [("A","B"),("A","C"),("B","E")] '''
    with open(filename, newline='') as f:
        return list(csv.reader(f))

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, showLabels = True):

    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # create network graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # draw graph 1
    pos = nx.shell_layout(G)
    nx.draw(G, pos)
    plt.figure()

    # draw graph 2
    # labels are now on top of the nodes
    nx.draw_random(G)
    plt.figure()
    nx.draw_spring(G, node_size=100, with_labels=showLabels, font_size=16, edge_color="grey", width=0.5)

    # draw graph 3 and save
    plt.savefig("fig1.png")
    plt.show()

# draw example
graph = getEdgeListFromCSVfile("/Users/maximilianhofer/PycharmProjects/LecturesSeminars/FacebookEdgeData.csv")
draw_graph(graph, showLabels=False)
