__author__ = 'maxhofer'

from GraphBFSRecursive import *  # requires GraphBFSRecursive to be in same working directory
import networkx as nx
import matplotlib.pyplot as plt
import random

class boardSquare(Vertex):
    def __init__(self, label, index):
        Vertex.__init__(self, label=label, index=index)
        self.squareNumber = int(label)
        y = (self.squareNumber-1)//10
        x = (self.squareNumber-y*10) if y%2 == 0 else 11 - (self.squareNumber-y*10)
        self.xyPosition = (x,y)

class SnakesAndLadders(Graph):
    def __init__(self):
        Graph.__init__(self)
        for i in range(1,100):
            self.addEdge(str(i),str(i+1))
        # add snakes and ladders - ladders have the lower number first
        self.addEdges("3-21,8-30,28-84,52-29,57-40,58-77,62-22,\
                        75-86,80-100,88-18,90-91,95-51,97-79")
        self.getVertex("1").occupied = True
        self.xyPlotPositions = dict([(s.label,s.xyPosition) for s in self.vertices])
        self.currentSquare = 1
        self.currentSquare1 =1

    def addVertex(self,label):
        v = self.getVertex(label)
        if v == None:
            self.number_vertices +=1
            v = boardSquare(label=label, index=self.number_vertices)
            self.vertices.append(v)
        return v

    def addVertex1(self,label):
        v1 = self.getVertex(label)
        if v1 == None:
            self.number_vertices +=1
            v1 = boardSquare(label=label, index=self.number_vertices)
            self.vertices.append(v1)
        return v1

    def drawBoard(self):
        # for this version I have eliminated all the G1 related code
        # both players are displayed using just one board
        # clears the display
        plt.clf()
        G=nx.DiGraph()
        for v in self.vertices:
            G.add_node(v.label)
        for e in self.edges:
            G.add_edge(e.startVertex.label, e.endVertex.label)
        edgeColours = []
        for e in G.edges_iter():
            edgeColours.append('grey' if int(e[0])==int(e[1])-1 else ('red' if int(e[0]) > int(e[1]) else 'green'))
        nodeSizes = []
        nodeColours = []
        for n in G.nodes_iter():
            # added new code for currentSquare1 as well
            nodeSizes.append(500 if int(n)==self.currentSquare or int(n)==self.currentSquare1 else 0)
            # now set the node colours - easiest to set all nodes to red except currentSquare1
            nodeColours.append("blue" if int(n)==self.currentSquare1 else "red")
        nx.draw(G, pos=self.xyPlotPositions, arrows = False, node_size=nodeSizes, node_color=nodeColours, with_labels=True,
                font_size=20, edge_color = edgeColours)
        plt.draw()
        plt.show(block=False)
        time.sleep(0.5)

    def playGame(self, interactive=True):
        numberMoves = 0
        numberMoves1 = 0
        self.currentSquare = 1
        self.currentSquare1 = 1
        winner = 2  # set the initial value of the winner to 2, for player 2
        while self.currentSquare<100 or self.currentSquare1<100:
            if interactive: self.drawBoard()
            if self.currentSquare < 100:
                numberMoves += 1
                self.nextMove(interactive)
            if self.currentSquare1 <100:
                numberMoves1 += 1
                self.nextMove1(interactive)
        if numberMoves < numberMoves1: winner = 1  # change winner to player 1 if true
        if interactive: print("Well done, player", winner,",you won! Game over")
        return numberMoves, numberMoves1


    def nextMove(self, interactive):
        dice = random.choice([1,2,3,4,5,6])
        self.currentSquare += dice
        self.currentSquare = min(self.currentSquare,100)
        if interactive: print("Player 1 moved to square ", self.currentSquare)
        boardSquare = self.getVertex(str(self.currentSquare))
        for e in self.edges:
            if e.startVertex is boardSquare:
                if e.endVertex.squareNumber > boardSquare.squareNumber + 1:
                    if interactive: print("Player 1: Up a ladder to ", e.endVertex.squareNumber)
                    self.currentSquare = e.endVertex.squareNumber
                    break
                elif e.endVertex.squareNumber < boardSquare.squareNumber:
                    if interactive: print("Player 1: Down a snake to ", e.endVertex.squareNumber)
                    self.currentSquare = e.endVertex.squareNumber
                    break

    def nextMove1(self, interactive):
        dice1 = random.choice([1,2,3,4,5,6])
        self.currentSquare1 += dice1
        self.currentSquare1 = min(self.currentSquare1,100)
        if interactive: print("Player 2 moved to square ", self.currentSquare1)
        boardSquare1 = self.getVertex(str(self.currentSquare1))
        for e in self.edges:
            if e.startVertex is boardSquare1:
                if e.endVertex.squareNumber > boardSquare1.squareNumber + 1:
                    if interactive: print("Player 2: Up a ladder to ", e.endVertex.squareNumber)
                    self.currentSquare1 = e.endVertex.squareNumber
                    break
                elif e.endVertex.squareNumber < boardSquare1.squareNumber:
                    if interactive: print("Player 2: Down a snake to ", e.endVertex.squareNumber)
                    self.currentSquare1 = e.endVertex.squareNumber
                    break

game = SnakesAndLadders()
print(game.playGame(interactive=True))
