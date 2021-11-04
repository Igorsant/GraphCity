import random
import copy

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
        subtitlesText = '\nS -> Ponto de partida (' + str(self.graph.start[0]) + ', ' + str(self.graph.start[1]) + ')\nE -> Ponto de chegada (' + str(self.graph.end[0]) + ', ' + str(self.graph.end[1]) + ')\n0 -> Nó vazio e não visitado\n1 -> Nó visitado\n2 -> Caminho escolhido\nX -> Obstáculo'
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
                    print('\nIniciando busca...\n')
                    print("\nBusca finalizada!")
                elif (choice == '2'):
                    print('\nIniciando busca...\n')
                    print("\nBusca finalizada!")
                elif (choice == '3'):
                    print('\nIniciando busca...\n')
                    print("\nBusca finalizada!")
                elif (choice == '4'):
                    print('\nIniciando busca...\n')
                    print("\nBusca finalizada!")
                elif (choice == '5'):
                    print('\nIniciando busca...\n')
                    print("\nBusca finalizada!")
                elif (choice == '6'):
                    restart = 'n'
            
            validChoices = ['s', 'n']
            while (restart.lower() not in validChoices):
                restart = input("\nGostaria de fazer outra busca com esse grafo? (S/N)\n")
                if (restart not in validChoices):
                    print('\nSeleção inválida!')
                else:
                    self.printGraphAndSubtitles()

class Node:

    id = -1
    pai = None
    value = 0

    def __init__(self,value):
        self.value = value

class Graph:
    
    matrix = []
    cleanMatrix = []
    obstacleWeight = 0.2
    
    start = None
    end = None
    
    def generateGraph(self, obstacles):
        self.matrix = [];
        self.cleanMatrix = [];
        for y in range(20):
            self.matrix.append([])
            self.cleanMatrix.append([])
            for x in range(20):
                value = 0
                if (obstacles):
                    value = random.choices(population=['0', 'X'], weights=[0.8, 0.2], k=1)[0]
                self.matrix[y].append(Node(value))
                self.cleanMatrix[y].append(Node(value))
                
                if (value != 'X'):
                    self.end = [x, y]
                    if (self.start == None):
                        self.start = [x, y]
        
        if (self.start == None or self.end == None):
            self.generateGraph(obstacles)
        else:
            self.placeStartEnd()
    
    def printGraph(self):
        counter = 0
        for x in self.matrix:
            for y in x:
                print(y.value, end = ' ')
            print()
    
    def resetMatrix(self):
        self.matrix = copy.deepcopy(self.cleanMatrix)
        
    def placeStartEnd(self):
        self.matrix[self.start[1]][self.start[0]].value = 'S'
        self.matrix[self.end[1]][self.end[0]].value = 'E'
    
    def changeStartingNode(self, newNode):
        self.start = newNode
        self.resetMatrix()
        self.placeStartEnd()
    
    def changeEndingNode(self, newNode):
        self.end = newNode
        self.resetMatrix()
        self.placeStartEnd()
    
main = Main()
        
        