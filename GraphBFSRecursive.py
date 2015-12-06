__author__ = 'andrewwhiter'

# THIS VERSION OF THE BREADTH FIRST SEARCH CODE INCLUDES A RECURSIVELY DEFINED BFS ALGORITHM

# THIS VERSION HAS ALSO HAS BEEN REFACTORED TO FIND AND STORE NEIGHBOURING VERTICES AS THE GRAPH IS
# FIRST CONSTRUCTED. NOT HAVING TO CALCULATE NEIGHBOURS EACH TIME LEADS TO A X1000 PERFORMANCE IMPROVEMENT

import csv, time, numpy

class Vertex(object):
    def __init__(self, label="", index=None, level=0):
        self.label = label
        self.index = index
        self.level = level
        self.neighbours = set()     # added neighbours attribute - x1000 performance increase!
#   ------------------------------

    def __repr__(self):
        # return "{}({})".format(self.label,self.index)
        return "{}".format(self.label)
#   ------------------------------

    def getChildren(self):   # added to take advantage of new neighbour attribute and for recursive BFS
        children = set()
        for v in self.neighbours:
            if v.level == None:
                v.level = 1 + self.level
                children.add(v)
            if v.level == 1 + self.level:
                children.add(v)
        return children
 #   ------------------------------

    def getParent(self):    # added to take advantage of new neighbour attribute and for recursive BFS
        for v in self.neighbours:
            if v.level == self.level - 1:
                return v
        else:
            return None
#   ------------------------------

    def clearLevel(self):   # added for recursive BFS
        self.level = None

#################################################################

class Edge(object):
    def __init__(self, startVertex, endVertex, weight=1):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight
#   ------------------------------

    def __repr__(self):
        return "{}-{}-{}".format(self.startVertex.label, ("" if self.weight==1 else self.weight), self.endVertex.label)

#################################################################

class Graph(object):
    def __init__(self):
        self.edges = []
        self.vertices = []
        self.number_vertices = 0
#------------------------------

    def getVertex(self,label):
        search = [v for v in self.vertices if v.label == label]
        if search == []:
            return None
        else:
            return search[0]
#------------------------------

    def addVertex(self,label):
        v = self.getVertex(label)
        if v == None:
            self.number_vertices +=1
            v = Vertex(label=label, index=self.number_vertices)
            self.vertices.append(v)
        return v
#------------------------------

    def addEdge(self,startLabel,endLabel,weight=1):
        startVertex = self.addVertex(startLabel)
        endVertex = self.addVertex(endLabel)
        self.edges.append(Edge(startVertex ,endVertex, weight=weight))
        startVertex.neighbours.add(endVertex)  # REFACTORED HERE - new line
        endVertex.neighbours.add(startVertex)  # REFACTORED HERE - new line
        return self
 #------------------------------

    def __repr__(self):
        return "<graph: vertices={}, edges={}>".format(self.vertices.__repr__(),self.edges.__repr__())
 #------------------------------

    def addEdges(self,edgeListStr):
        for edgeStr in edgeListStr.split(sep=","):
            startLabel, endLabel = edgeStr.split("-")
            self.addEdge(startLabel.strip(),endLabel.strip())
 #------------------------------

    def addEdgesFromCSVfile(self,filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                startLabel, endLabel = row
                self.addEdge(startLabel.strip(),endLabel.strip())
  #------------------------------

    def findPathBFS(self,startVertex, goalVertex):

        ##### CLEAR LEVELS BEFORE STARTING SERACH  ######
        for v in self.vertices:
            v.clearLevel()
        startVertex.level = 1

        ##### NOW USE RECURSIVE FUNCTION TO PERFORM THE SEARCH ######
        return self.recursiveBFS(set([startVertex]),goalVertex)
  #------------------------------

    def recursiveBFS(self,levelVertexSet,goalVertex):
        ''' returns a shortest path from one of vertices in levelVertexSet to goalVertex '''

        ##### BASES CASES ######
        nextLevelSet = set()
        for v in levelVertexSet:
            children = v.getChildren()
            for c in children:
                if c is goalVertex:
                    return [v, c]     # <- BASE CASE 1: Goal is found!
            nextLevelSet.update(children)

        if len(nextLevelSet)==0:
            return []  # <- BASE CASE 2: there are no more children - no path exists

        ##### RECURSIVE CALL ######
        path = self.recursiveBFS(nextLevelSet,goalVertex)
        if path == []:
            return []  # NO PATH TO GOAL FOUND
        else:
            return [path[0].getParent()]+ path   # ADD PARENT OF 1ST VERTEX IN PATH TO GOAL

def main():
    # All the following test rely on the following loaded Facebook data
    g=Graph()
    g.addEdgesFromCSVfile("FacebookEdgeData.csv")
    # Test 1: Find a known 9-node shortest path - from vertex 212 to 783
    # Test 2: Prints the first 10 shortest paths of length 8 or more
    # Test 3: Find the mean time to find the 9 length path from 212 to 783

if __name__ == '__main__':
    main()
