import time
import os

class Busca:
    targetFound = False
    arestasPercorridas = 0
    
    def __init__(self, graph):
        self.graph = graph
        self.graph.resetMatrix()
                                                                                                                      
    def checkNode(self, node, previousNode, delay = 0.005):
        if (node.value == '0'):
            node.value = '1'
            node.pai = previousNode
            node.profundidade = previousNode.profundidade + 1
            time.sleep(delay)
            
            # Pula linhas até as anteriores estarem fora de vista e reprinta o grafo, dando ilusão de animação (Só funciona no cmd, não no Jupyter Lab)
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            self.graph.printGraph()
            self.arestasPercorridas = self.arestasPercorridas + 1
            return True
        elif (node.value == 'E'):
            node.pai = previousNode
            node.profundidade = previousNode.profundidade + 1
            self.targetFound = True
            self.arestasPercorridas = self.arestasPercorridas + 1
            return True
        elif (node.value == '1'):
            if (node.profundidade > previousNode.profundidade + 1):
                node.pai = previousNode
                node.profundidade = previousNode.profundidade + 1
            return False
        elif (node.value == 'X'):
            return False
    
    def traceBestPath(self):
        currentNode = self.graph.end
        
        while (currentNode.pai != None and currentNode.pai != self.graph.start):
            currentNode = currentNode.pai
            currentNode.value = '2'
        
        # Pula linhas até as anteriores estarem fora de vista e reprinta o grafo, dando ilusão de animação (Só funciona no cmd, não no Jupyter Lab)
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        self.graph.printGraph()
        
    def showResult(self):
        self.traceBestPath()
        if (self.targetFound):
            print("\nNó alvo encontrado!")
        else:
            print("\nNó alvo não encontrado!")

        print("\nArestas percorridas: " + str(self.arestasPercorridas))

        print("\nProfundidade do caminho escolhido: " + str(self.graph.end.profundidade))
        
    
    def buscaEmLargura(self):
        
        self.graph.printGraph()
        self.targetFound = False
        self.arestasPercorridas = 0
        
        delay = 0.005
        
        nextNodes = [self.graph.start]
        
        if (self.graph.start == self.graph.end):
            self.targetFound = True
        
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
        
        if (self.graph.start == self.graph.end):
            self.targetFound = True
        
        # Left Node
        if (currentNode.x > 0 and not self.targetFound):
            leftNode = self.graph.matrix[currentNode.x - 1][currentNode.y];
            if (self.checkNode(leftNode, currentNode, delay)):
                 self.buscaEmProfundidade(leftNode)
    
        # Right Node
        if (currentNode.x < 19 and not self.targetFound):
            rightNode = self.graph.matrix[currentNode.x + 1][currentNode.y];
            if (self.checkNode(rightNode, currentNode, delay)):
                self.buscaEmProfundidade(rightNode)
    
        # Up Node
        if (currentNode.y > 0 and not self.targetFound):
            upNode = self.graph.matrix[currentNode.x][currentNode.y - 1];
            if (self.checkNode(upNode, currentNode, delay)):
                self.buscaEmProfundidade(upNode)
    
        # Down Node
        if (currentNode.y < 19 and not self.targetFound):
            downNode = self.graph.matrix[currentNode.x][currentNode.y + 1];
            if (self.checkNode(downNode, currentNode, delay)):
                self.buscaEmProfundidade(downNode)
        
        # Apenas mostra as mensagens de finalização na função inicial da recursão
        if (currentNode == self.graph.start):
            self.showResult()