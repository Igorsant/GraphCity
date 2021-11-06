from graph import Graph
from busca import Busca

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


main = Main()