import time
import math
from graph import Graph

class Busca:
    targetFound = False
    arestasPercorridas = 0

    def __init__(self, graph: Graph):
        self.graph = graph
        self.graph.resetMatrix()



    def checkNodeDepth(self, node, previousNode, delay = 0.005):
        if (node.value == '0'):
            node.value = '1'
            self.checkShortcutDepth(node, previousNode)
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

    def checkShortcutDepth(self, node, previousNode):
        if (node.value != 'X' and (node.profundidade == None or node.profundidade > previousNode.profundidade + 1)):
            node.pai = previousNode
            node.profundidade = previousNode.profundidade + 1
        elif (node.value != 'X' and (previousNode.profundidade > node.profundidade + 1)):
            previousNode.pai = node
            previousNode.profundidade = node.profundidade + 1

    def checkNodeCost(self, node, previousNode, delay = 0.005):
        if (node.value == '0'):
            node.value = '1'
            self.checkShortcutCost(node, previousNode)
            time.sleep(delay)
            self.arestasPercorridas = self.arestasPercorridas + 1
            return True
        elif (node.value == 'E'):
            self.checkShortcutCost(node, previousNode)
            self.targetFound = True
            self.arestasPercorridas = self.arestasPercorridas + 1
            return True
        elif (node.value == 'X'):
            return False
        
    def checkShortcutCost(self, node, previousNode):
        if (node.value != 'X' and (node.costSum == None or node.costSum > previousNode.costSum + previousNode.costValue)):
            node.pai = previousNode
            node.profundidade = previousNode.profundidade + 1
            node.costSum = previousNode.costSum + previousNode.costValue
        elif (node.value != 'X' and (previousNode.costSum > node.costSum + node.costValue)):
            previousNode.pai = node
            previousNode.profundidade = node.profundidade + 1
            previousNode.costSum = node.costSum + node.costValue

    def traceBestPath(self):
        currentNode = self.graph.end

        while (currentNode.pai != None and currentNode.pai != self.graph.start):
            currentNode = currentNode.pai
            currentNode.value = '2'

    def showResult(self, hasCost = False):
        self.traceBestPath()
        if (self.targetFound):
            print("\nNó alvo encontrado!")
        else:
            print("\nNó alvo não encontrado!")

        print("\nArestas percorridas: " + str(self.arestasPercorridas))

        if (self.targetFound):
            print("\nProfundidade do caminho escolhido: " + str(self.graph.end.profundidade))
            if (hasCost): 
                print("\nCusto do caminho escolhido: " + str(self.graph.end.costSum + self.graph.end.costValue))

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
                if (self.checkNodeDepth(leftNode, currentNode, delay)):
                    nextNodes.append(leftNode)

            # Right Node
            if (currentNode.x < 19 and not self.targetFound):
                rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y];
                if (self.checkNodeDepth(rightNode, currentNode, delay)):
                    nextNodes.append(rightNode)

            # Up Node
            if (currentNode.y > 0 and not self.targetFound):
                upNode = self.graph.matrix[currentNode.x][currentNode.y - 1];
                if (self.checkNodeDepth(upNode, currentNode, delay)):
                    nextNodes.append(upNode)

            # Down Node
            if (currentNode.y < 19 and not self.targetFound):
                downNode = self.graph.matrix[currentNode.x][currentNode.y + 1];
                if (self.checkNodeDepth(downNode, currentNode, delay)):
                    nextNodes.append(downNode)

            nextNodes.pop(0)

        self.showResult()

    def buscaEmProfundidade(self, currentNode = None):
        if (currentNode == None):
            self.targetFound = False
            currentNode = self.graph.start
            self.arestasPercorridas = 0

        delay = 0.005

        upNode = None
        rightNode = None
        downNode = None
        leftNode = None

        if (currentNode.y > 0):
            upNode = self.graph.matrix[currentNode.x][currentNode.y - 1]
            self.checkShortcutDepth(upNode, currentNode)

        if (currentNode.x < 19):
            rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y]
            self.checkShortcutDepth(rightNode, currentNode)

        if (currentNode.y < 19):
            downNode = self.graph.matrix[currentNode.x][currentNode.y + 1]
            self.checkShortcutDepth(downNode, currentNode)

        if (currentNode.x > 0):
            leftNode = self.graph.matrix[currentNode.x - 1][currentNode.y]
            self.checkShortcutDepth(leftNode, currentNode)

        # Up Node
        if (currentNode.y > 0 and not self.targetFound and self.checkNodeDepth(upNode, currentNode, delay)):
            self.buscaEmProfundidade(upNode)

        # Right Node
        if (currentNode.x < 19 and not self.targetFound and self.checkNodeDepth(rightNode, currentNode, delay)):
            self.buscaEmProfundidade(rightNode)

        # Down Node
        if (currentNode.y < 19 and not self.targetFound and self.checkNodeDepth(downNode, currentNode, delay)):
            self.buscaEmProfundidade(downNode)

        # Left Node
        if (currentNode.x > 0 and not self.targetFound and self.checkNodeDepth(leftNode, currentNode, delay)):
            self.buscaEmProfundidade(leftNode)

        # Apenas mostra as mensagens de finalização na função inicial da recursão
        if (currentNode == self.graph.start):
            self.showResult()

    def buscaDeCustoUniforme(self):
        self.graph.displayCosts = True

        self.targetFound = False
        self.arestasPercorridas = 0
        
        self.graph.start.costSum = 0
        self.graph.start.costValue = 0

        delay = 0.005

        nextNodes = [self.graph.start]
        foundTarget = None

        while (len(nextNodes) > 0 and not self.targetFound):
            currentNode = nextNodes[0]

            upNode = None
            rightNode = None
            downNode = None
            leftNode = None
    
            if (currentNode.y > 0):
                upNode = self.graph.matrix[currentNode.x][currentNode.y - 1]
                self.checkShortcutCost(upNode, currentNode)
                if (upNode == self.graph.end):
                    foundTarget = upNode
    
            if (currentNode.x < 19):
                rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y]
                self.checkShortcutCost(rightNode, currentNode)
                if (rightNode == self.graph.end):
                    foundTarget = rightNode
    
            if (currentNode.y < 19):
                downNode = self.graph.matrix[currentNode.x][currentNode.y + 1]
                self.checkShortcutCost(downNode, currentNode)
                if (downNode == self.graph.end):
                    foundTarget = downNode
    
            if (currentNode.x > 0):
                leftNode = self.graph.matrix[currentNode.x - 1][currentNode.y]
                self.checkShortcutCost(leftNode, currentNode)
                if (leftNode == self.graph.end):
                    foundTarget = leftNode
    
            # Left Node
            if (currentNode.x > 0 and not self.targetFound):
                if (self.checkNodeCost(leftNode, currentNode, delay)):
                    nextNodes.append(leftNode)

            # Right Node
            if (currentNode.x < 19 and not self.targetFound):
                rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y];
                if (self.checkNodeCost(rightNode, currentNode, delay)):
                    nextNodes.append(rightNode)

            # Up Node
            if (currentNode.y > 0 and not self.targetFound):
                upNode = self.graph.matrix[currentNode.x][currentNode.y - 1];
                if (self.checkNodeCost(upNode, currentNode, delay)):
                    nextNodes.append(upNode)

            # Down Node
            if (currentNode.y < 19 and not self.targetFound):
                downNode = self.graph.matrix[currentNode.x][currentNode.y + 1];
                if (self.checkNodeCost(downNode, currentNode, delay)):
                    nextNodes.append(downNode)

            nextNodes.pop(0)
            
            if (foundTarget):
                nextNodes = list(filter(lambda node: node.costSum + node.costValue < foundTarget.costSum, nextNodes))
            
            nextNodes.sort(key=lambda x: x.costSum + x.costValue)

        self.showResult(True)

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
                if (self.checkNodeDepth(leftNode, currentNode, delay)):
                    nextNodes.append(leftNode)

            # Right Node
            if (currentNode.x < 19 and not self.targetFound):
                rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y];
                rightNode.sortValue = self.distance(rightNode.x, rightNode.y, self.graph.end.x, self.graph.end.y)
                if (self.checkNodeDepth(rightNode, currentNode, delay)):
                    nextNodes.append(rightNode)

            # Up Node
            if (currentNode.y > 0 and not self.targetFound):
                upNode = self.graph.matrix[currentNode.x][currentNode.y - 1];
                upNode.sortValue = self.distance(upNode.x, upNode.y, self.graph.end.x, self.graph.end.y)
                if (self.checkNodeDepth(upNode, currentNode, delay)):
                    nextNodes.append(upNode)

            # Down Node
            if (currentNode.y < 19 and not self.targetFound):
                downNode = self.graph.matrix[currentNode.x][currentNode.y + 1];
                downNode.sortValue = self.distance(downNode.x, downNode.y, self.graph.end.x, self.graph.end.y)
                if (self.checkNodeDepth(downNode, currentNode, delay)):
                    nextNodes.append(downNode)

            nextNodes.sort(key= lambda x: x.sortValue)

        self.showResult()

    def a_star(self):
        self.targetFound = False
        self.arestasPercorridas = 0

        delay = 0.005

        nextNodes = [self.graph.start]

        if (self.graph.start == self.graph.end):
            self.targetFound = True

        nextNodes[0].dist_from_father = 0
        while (len(nextNodes) > 0 and not self.targetFound):
            if len(nextNodes) == 0:
                print('busca impossível')
                break
            currentNode = nextNodes.pop(0)
            # Left Node
            if (currentNode.x > 0 and not self.targetFound):
                leftNode = self.graph.matrix[currentNode.x - 1][currentNode.y];
                leftNode.sortValue = self.distance(leftNode.x, leftNode.y, self.graph.end.x, self.graph.end.y)
                leftNode.dist_from_father = currentNode.dist_from_father+1
                if (self.checkNodeDepth(leftNode, currentNode, delay)):
                    nextNodes.append(leftNode)

            # Right Node
            if (currentNode.x < 19 and not self.targetFound):
                rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y];
                rightNode.sortValue = self.distance(rightNode.x, rightNode.y, self.graph.end.x, self.graph.end.y)
                rightNode.dist_from_father = currentNode.dist_from_father+1
                if (self.checkNodeDepth(rightNode, currentNode, delay)):
                    nextNodes.append(rightNode)

            # Up Node
            if (currentNode.y > 0 and not self.targetFound):
                upNode = self.graph.matrix[currentNode.x][currentNode.y - 1];
                upNode.sortValue = self.distance(upNode.x, upNode.y, self.graph.end.x, self.graph.end.y)
                upNode.dist_from_father = currentNode.dist_from_father+1
                if (self.checkNodeDepth(upNode, currentNode, delay)):
                    nextNodes.append(upNode)

            # Down Node
            if (currentNode.y < 19 and not self.targetFound):
                downNode = self.graph.matrix[currentNode.x][currentNode.y + 1];
                downNode.sortValue = self.distance(downNode.x, downNode.y, self.graph.end.x, self.graph.end.y)
                downNode.dist_from_father = currentNode.dist_from_father+1
                if (self.checkNodeDepth(downNode, currentNode, delay)):
                    nextNodes.append(downNode)

            nextNodes.sort(key= lambda x: x.sortValue+x.dist_from_father)

        self.showResult()

    def distance(self, sourceX, sourceY, destX, destY):
        return math.fabs(sourceX-destX)+math.fabs(sourceY-destY)
