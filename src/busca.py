import time
import os
import math
from graph import Graph

class Busca:
    targetFound = False
    arestasPercorridas = 0
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.graph.resetMatrix()



    def checkNode(self, node, previousNode, delay = 0.005):
        if (node.value == '0'):
            node.value = '1'
            self.checkShortcut(node, previousNode)
            time.sleep(delay)

            self.arestasPercorridas = self.arestasPercorridas + 1
            return True
        elif (node.value == 'E'):
            node.pai = previousNode
            node.profundidade = previousNode.profundidade + 1
            self.targetFound = True
            self.arestasPercorridas = self.arestasPercorridas + 1
            return True
        elif (node.value == 'X'):
            return False

    def checkShortcut(self, node, previousNode):
        if (node.value != 'X' and (node.profundidade == None or node.profundidade > previousNode.profundidade + 1)):
            node.pai = previousNode
            node.profundidade = previousNode.profundidade + 1
        elif (node.value != 'X' and (previousNode.profundidade > previousNode.profundidade + 1 and node.pai != previousNode)):
            previousNode.pai = node
            previousNode.profundidade = node.profundidade + 1

    def traceBestPath(self):
        currentNode = self.graph.end

        while (currentNode.pai != None and currentNode.pai != self.graph.start):
            currentNode = currentNode.pai
            currentNode.value = '2'


    def showResult(self):
        self.traceBestPath()
        if (self.targetFound):
            print("\nNó alvo encontrado!")
        else:
            print("\nNó alvo não encontrado!")

        print("\nArestas percorridas: " + str(self.arestasPercorridas))

        if (self.targetFound):
            print("\nProfundidade do caminho escolhido: " + str(self.graph.end.profundidade))

    def buscaEmLargura(self):

        self.targetFound = False
        self.arestasPercorridas = 0

        delay = 0.005

        nextNodes = [self.graph.start]

        while (len(nextNodes) > 0 and not self.targetFound):
            currentNode = nextNodes[0]
            # Left Node
            if (currentNode.x > 0 and not self.targetFound):
                leftNode = self.graph.matrix[currentNode.x - 1][currentNode.y];
                if (self.checkNode(leftNode, currentNode, delay)):
                    nextNodes.append(leftNode)

            # Right Node
            if (currentNode.x < 19 and not self.targetFound):
                rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y];
                if (self.checkNode(rightNode, currentNode, delay)):
                    nextNodes.append(rightNode)

            # Up Node
            if (currentNode.y > 0 and not self.targetFound):
                upNode = self.graph.matrix[currentNode.x][currentNode.y - 1];
                if (self.checkNode(upNode, currentNode, delay)):
                    nextNodes.append(upNode)

            # Down Node
            if (currentNode.y < 19 and not self.targetFound):
                downNode = self.graph.matrix[currentNode.x][currentNode.y + 1];
                if (self.checkNode(downNode, currentNode, delay)):
                    nextNodes.append(downNode)

            nextNodes.pop(0)

        self.showResult()

    def buscaEmProfundidade(self, currentNode = None):
        if (currentNode == None):
            self.targetFound = False
            currentNode = self.graph.start
            self.arestasPercorridas = 0

        delay = 0.001

        upNode = None
        rightNode = None
        downNode = None
        leftNode = None

        if (currentNode.y > 0):
            upNode = self.graph.matrix[currentNode.x][currentNode.y - 1]
            self.checkShortcut(upNode, currentNode)

        if (currentNode.x < 19):
            rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y]
            self.checkShortcut(rightNode, currentNode)

        if (currentNode.y < 19):
            downNode = self.graph.matrix[currentNode.x][currentNode.y + 1]
            self.checkShortcut(downNode, currentNode)

        if (currentNode.x > 0):
            leftNode = self.graph.matrix[currentNode.x - 1][currentNode.y]
            self.checkShortcut(leftNode, currentNode)

        # Up Node
        if (currentNode.y > 0 and not self.targetFound and self.checkNode(upNode, currentNode, delay)):
            self.buscaEmProfundidade(upNode)

        # Right Node
        if (currentNode.x < 19 and not self.targetFound and self.checkNode(rightNode, currentNode, delay)):
            self.buscaEmProfundidade(rightNode)

        # Down Node
        if (currentNode.y < 19 and not self.targetFound and self.checkNode(downNode, currentNode, delay)):
            self.buscaEmProfundidade(downNode)

        # Left Node
        if (currentNode.x > 0 and not self.targetFound and self.checkNode(leftNode, currentNode, delay)):
            self.buscaEmProfundidade(leftNode)

        # Apenas mostra as mensagens de finalização na função inicial da recursão
        if (currentNode == self.graph.start):
            self.showResult()
    
    def busca_gulosa(self):
        self.targetFound = False
        self.arestasPercorridas = 0
        
        delay = 0.005
        
        nextNodes = [self.graph.start]
        
        if (self.graph.start == self.graph.end):
            self.targetFound = True
        
        while (len(nextNodes) > 0 and not self.targetFound):
            if len(nextNodes) == 0:
                print('busca impossível')
                break
            currentNode = nextNodes.pop(0)
            # Left Node
            if (currentNode.x > 0 and not self.targetFound):
                leftNode = self.graph.matrix[currentNode.x - 1][currentNode.y];
                leftNode.sortValue = self.distance(leftNode.x, leftNode.y, self.graph.end.x, self.graph.end.y)
                if (self.checkNode(leftNode, currentNode, delay)):
                    nextNodes.append(leftNode)
        
            # Right Node
            if (currentNode.x < 19 and not self.targetFound):
                rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y];
                rightNode.sortValue = self.distance(rightNode.x, rightNode.y, self.graph.end.x, self.graph.end.y)
                if (self.checkNode(rightNode, currentNode, delay)):
                    nextNodes.append(rightNode)
        
            # Up Node
            if (currentNode.y > 0 and not self.targetFound):
                upNode = self.graph.matrix[currentNode.x][currentNode.y - 1];
                upNode.sortValue = self.distance(upNode.x, upNode.y, self.graph.end.x, self.graph.end.y)
                if (self.checkNode(upNode, currentNode, delay)):
                    nextNodes.append(upNode)
        
            # Down Node
            if (currentNode.y < 19 and not self.targetFound):
                downNode = self.graph.matrix[currentNode.x][currentNode.y + 1];
                downNode.sortValue = self.distance(downNode.x, downNode.y, self.graph.end.x, self.graph.end.y)
                if (self.checkNode(downNode, currentNode, delay)):
                    nextNodes.append(downNode)
            
            nextNodes.sort(key= lambda x: x.sortValue)
            
        self.showResult()
    
    def distance(self, sourceX, sourceY, destX, destY):
        return math.fabs(sourceX-destX)+math.fabs(sourceY-destY)
