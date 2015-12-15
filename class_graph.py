__author__ = 'andrewwhiter'

############################################################################
# THIS FILE PROVIDES CODE FOR THE GRAPH, VERTEX AND EDGE CLASSES
# COVERED IN THE WEEK 4 SEMINAR
# Requires you to have Matrix.py saved in your working directory
# EXCEPT FOR Graph.adjacencyMatrix() or Graph.distanceMatrix()
############################################################################

from Matrix import *


class Graph(object):
    def __init__(self):
        self.edges = []
        self.vertices = []
        self.number_vertices = 0   # number of vertices

    def getVertex(self,label):
        search = [v for v in self.vertices if v.label == label]
        if search == []:
            return None
        else:
            return search[0]

    def addVertex(self,label):
        """ Either adds and returns a new vertex or returns the vertex previously added with the same label """
        v = self.getVertex(label)
        if v == None:  # only add a new vertex if it is not already added
            self.number_vertices +=1
            v = Vertex(label=label, index=self.number_vertices)
            self.vertices.append(v)
        return v

    def addEdge(self,startLabel,endLabel,weight=1):
        startVertex = self.addVertex(startLabel)
        endVertex = self.addVertex(endLabel)
        self.edges.append(Edge(startVertex ,endVertex, weight=weight))
        return self

    def adjacencyMatrix(self):
        A = Matrix(n=self.number_vertices,m=self.number_vertices)
        for edge in self.edges:
            A.set(edge.startVertex.index, edge.endVertex.index, edge.weight)
            A.set(edge.endVertex.index, edge.startVertex.index, edge.weight)
        return A

    def distanceMatrix(self):
        A = self.adjacencyMatrix()
        powerA = A
        power = 1
        distanceM = A.copy()
        while distanceM.contains(0):
            powerA = powerA.dot(A)
            power +=1
            for i in range(1,A.n +1):
                for j in range(1,A.n +1):
                    d = distanceM.get(i,j)
                    if d == 0 and powerA.get(i,j)>0:
                        distanceM.set(i,j,power)
        return distanceM

    def __repr__(self):
        return "<graph: vertices={}, edges={}>".format(self.vertices.__repr__(),self.edges.__repr__())


#################################################################

class Edge(object):
    def __init__(self, startVertex, endVertex, weight=1):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight

    def __repr__(self):
        return "{}-{}-{}".format(self.startVertex.label, ("" if self.weight==1 else self.weight), self.endVertex.label)


#################################################################


class Vertex(object):
    def __init__(self, label="", index=None):
        self.label = label
        self.index = index

    def __repr__(self):
        return "{}({})".format(self.label,self.index)


#################################################################


g = Graph()
g.addEdge("A","B")
g.addEdge("A","C")
g.addEdge("A","D")
g.addEdge("B","E")
g.addEdge("B","F")
g.addEdge("C","E")
g.addEdge("C","F")
g.addEdge("D","E")
g.addEdge("D","F")
g.addEdge("E","T")
g.addEdge("F","T")

A=g.adjacencyMatrix()
A2 = A.dot(A)
A3 = A.dot(A.dot(A))

print("",g,"","adjacency matrix (A): ", A,sep="\n")
print("number of length 2 paths (A^2):",A2,"number of length 3 paths (A^3):",A3,sep="\n" )
print("distance matrix:")
print(g.distanceMatrix())

# <graph: vertices=[A(1), B(2), C(3), D(4), E(5), F(6), T(7)], edges=[A--B, A--C, A--D, B--E, B--F, C--E, C--F, D--E, D--F, E--T, F--T]>
#
# adjacency matrix (A):
#   0    1    1    1    0    0    0
#   1    0    0    0    1    1    0
#   1    0    0    0    1    1    0
#   1    0    0    0    1    1    0
#   0    1    1    1    0    0    1
#   0    1    1    1    0    0    1
#   0    0    0    0    1    1    0
#
# number of length 2 paths (A^2):
#   3    0    0    0    3    3    0
#   0    3    3    3    0    0    2
#   0    3    3    3    0    0    2
#   0    3    3    3    0    0    2
#   3    0    0    0    4    4    0
#   3    0    0    0    4    4    0
#   0    2    2    2    0    0    2
#
# number of length 3 paths (A^3):
#   0    9    9    9    0    0    6
#   9    0    0    0   11   11    0
#   9    0    0    0   11   11    0
#   9    0    0    0   11   11    0
#   0   11   11   11    0    0    8
#   0   11   11   11    0    0    8
#   6    0    0    0    8    8    0
#
# distance matrix:
#   2    1    1    1    2    2    3
#   1    2    2    2    1    1    2
#   1    2    2    2    1    1    2
#   1    2    2    2    1    1    2
#   2    1    1    1    2    2    1
#   2    1    1    1    2    2    1
#   3    2    2    2    1    1    2
