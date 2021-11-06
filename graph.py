import random
import copy
import time
import os

class Main:
    graph = {}
    
    def __init__(self):
        print('Trabalho de Inteligência Artificial - AV2')
        print('* Grupo:\n - Divaldo Aderaldo de Oliveira Júnior (1810534)\n - Igor Oliveira dos Santos (1913439)\n')
        
        self.graph = Graph()
        
        choice = {}
        choiceBoolean = False
        validChoices = ['1', '2']
        
        while (choice not in validChoices):
            choice = input("\nQue tipo de grafo deseja criar?\n\n1) Com obstáculos\n2) Sem obstáculos\n\n")
            if (choice not in validChoices):
                print('\nSeleção inválida!')
            elif (choice == '1'):
                choiceBoolean = True
            else:
                choiceBoolean = False
        
        self.graph.generateGraph(choiceBoolean)
        
        self.menu()
                
    def printGraphAndSubtitles(self):
        print('\nGrafo Atual:\n')
        self.graph.printGraph()
        subtitlesText = '\nS -> Ponto de partida (' + str(self.graph.start.x) + ', ' + str(self.graph.start.y) + ')\nE -> Ponto de chegada (' + str(self.graph.end.x) + ', ' + str(self.graph.end.y) + ')\n0 -> Nó vazio e não visitado\n1 -> Nó visitado\n2 -> Caminho escolhido\nX -> Obstáculo'
        print(subtitlesText)
    
    def menu(self):
        self.printGraphAndSubtitles()
        choice = {}
        validChoices = ['1', '2', '3', '4', '5', '6']
        
        while (choice != '6'):
            choice = input('\nO que deseja fazer agora?\n\n1) Efetuar busca\n2) Modificar ponto de partida\n3) Modificar ponto de chegada\n4) Gerar novo grafo com obstáculos\n5) Gerar novo grafo sem obstáculos\n6) Encerrar\n\n')
            
            if (choice not in validChoices):
                print('\nSeleção inválida!')
            elif (choice == '1'):
                self.chooseSearch()
            elif (choice == '2'):
                validRange = False
                
                while (validRange == False):
                    nodeInput = input('\nQuais as novas coordenadas do ponto de partida? (X, Y)\n\n')
                    newNode = nodeInput.split(',')
                    if (len(newNode) == 2 and int(newNode[0]) in range(20) and int(newNode[1]) in range(20)):
                        newNode[0] = int(newNode[0])
                        newNode[1] = int(newNode[1])
                        
                        if (self.graph.matrix[newNode[1]][newNode[0]].value == 'X'):
                            print('\nHá um obstáculo nessa coordenada!')
                        elif(self.graph.matrix[newNode[1]][newNode[0]] == self.graph.end):
                            print('\nO ponto de partida não pode ser igual ao ponto de chegada!')
                        else:
                            self.graph.changeStartingNode(newNode)
                            validRange = True
                            self.printGraphAndSubtitles()
                    else:
                        print('\nSeleção inválida!')
            elif (choice == '3'):
                validRange = False
                
                while (validRange == False):
                    nodeInput = input('\nQuais as novas coordenadas do ponto de chegada? (X, Y)\n\n')
                    newNode = nodeInput.split(',')
                    if (len(newNode) == 2 and int(newNode[0]) in range(20) and int(newNode[1]) in range(20)):
                        newNode[0] = int(newNode[0])
                        newNode[1] = int(newNode[1])
                        
                        if (self.graph.matrix[newNode[1]][newNode[0]].value == 'X'):
                            print('\nHá um obstáculo nessa coordenada!')
                        elif(self.graph.matrix[newNode[1]][newNode[0]] == self.graph.start):
                            print('\nO ponto de chegada não pode ser igual ao ponto de partida!')
                        else:
                            self.graph.changeEndingNode(newNode)
                            validRange = True
                            self.printGraphAndSubtitles()
                    else:
                        print('\nSeleção inválida!')
            elif (choice == '4'):
                self.graph.generateGraph(True)
                self.printGraphAndSubtitles()
            elif (choice == '5'):
                self.graph.generateGraph(False)
                self.printGraphAndSubtitles()
            elif (choice == '6'):
                print('\nEncerrando script...')
                

    def chooseSearch(self):
        buscas = Busca(self.graph)
        restart = ""
        
        while (restart != 'n'):
            restart = ""
            choice = {}
            validChoices = ['1', '2', '3', '4', '5', '6']
            
            while (choice not in validChoices):
                choice = input("\nQue tipo de procura deseja efetuar?\n\n1) Busca em Largura\n2) Busca em Profundidade\n3) Busca de Custo Uniforme\n4) Busca Gulosa pela Melhor Escolha\n5) A*\n6) Retornar\n\n")
                if (choice not in validChoices):
                    print('\nSeleção inválida!')
                elif (choice == '1'):
                    buscas.buscaEmLargura()
                elif (choice == '2'):
                    self.graph.printGraph()
                    buscas.buscaEmProfundidade()
                elif (choice == '3'):
                    print('\nTODO\n')
                elif (choice == '4'):
                    print('\nTODO\n')
                elif (choice == '5'):
                    print('\nTODO\n')
                elif (choice == '6'):
                    self.printGraphAndSubtitles()
                    restart = 'n'
            
            self.graph.resetMatrix()
            
            validChoices = ['s', 'n']
            while (restart.lower() not in validChoices):
                restart = input("\nGostaria de fazer outra busca com esse grafo? (S/N)\n")
                if (restart not in validChoices):
                    print('\nSeleção inválida!')
                else:
                    self.printGraphAndSubtitles()
            
class Busca:
    targetFound = False
    graph = None
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
    
class Node:

    id = -1
    pai = None
    profundidade = None
    value = 0
    x = 0
    y = 0

    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

class Graph:
    
    matrix = []
    cleanMatrix = []
    obstacleWeight = 0.2
    
    start = None
    end = None
    
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
    
    def resetMatrix(self):
        self.matrix = copy.deepcopy(self.cleanMatrix)
        self.start = self.matrix[self.start.x][self.start.y]
        self.end = self.matrix[self.end.x][self.end.y]
        self.placeStartEnd()
        
    def placeStartEnd(self):
        self.start.value = 'S'
        self.start.profundidade = 0
        self.end.value = 'E'
    
    def changeStartingNode(self, nodeCoordinates):
        x = nodeCoordinates[0]
        y = nodeCoordinates[1]
        self.start = self.matrix[x][y]
        self.resetMatrix()
        self.placeStartEnd()
    
    def changeEndingNode(self, nodeCoordinates):
        x = nodeCoordinates[0]
        y = nodeCoordinates[1]
        self.end = self.matrix[x][y]
        self.resetMatrix()
        self.placeStartEnd()
    
main = Main()
        
        