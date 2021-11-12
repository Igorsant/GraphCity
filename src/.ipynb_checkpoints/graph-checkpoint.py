import random
import copy
from node import Node

class Graph:
    obstacleWeight = 0.2
    
    displayCosts = False

    def generateGraph(self, obstacles):
        self.start = None
        self.end = None
        self.matrix = []
        self.cleanMatrix = []
        for x in range(20):
            self.matrix.append([])
            self.cleanMatrix.append([])
            for y in range(20):
                value = '0'
                if (obstacles):
                    value = random.choices(population=['0', 'X'], weights=[0.8, 0.2], k=1)[0]

                self.matrix[x].append(Node(value, x, y))
                self.cleanMatrix[x].append(Node(value, x, y))

                if (value != 'X'):
                    self.end = self.matrix[x][y]
                    if (self.start == None):
                        self.start = self.matrix[x][y]

        # Fallback se uma matrix tiver apenas X ou um único nó disponível (quase impossível)
        if (self.start == None or self.end == None or self.start == self.end):
            self.generateGraph(obstacles)
        else:
            self.placeStartEnd()

    def buildGraph(self):
        graph = ''
        for y in range(20):
            for x in range(20):
                graph = graph + str(self.matrix[x][y].value) + ' '
            graph = graph + '\n'
        return graph


    def printGraph(self):
        print(self.buildGraph())

    def resetMatrix(self, placeStartEnd = True):
        self.matrix = copy.deepcopy(self.cleanMatrix)
        self.start = self.matrix[self.start.x][self.start.y]
        self.end = self.matrix[self.end.x][self.end.y]
        if (placeStartEnd):
            self.placeStartEnd()

    def placeStartEnd(self):
        self.start.value = 'S'
        self.start.profundidade = 0
        self.end.value = 'E'

    def changeStartingNode(self, nodeCoordinates):
        x = nodeCoordinates[0]
        y = nodeCoordinates[1]
        self.resetMatrix(False)
        self.start = self.matrix[x][y]
        self.placeStartEnd()

    def changeEndingNode(self, nodeCoordinates):
        x = nodeCoordinates[0]
        y = nodeCoordinates[1]
        self.resetMatrix(False)
        self.end = self.matrix[x][y]
        self.placeStartEnd()
