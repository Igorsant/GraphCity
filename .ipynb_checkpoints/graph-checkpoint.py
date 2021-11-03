import queue
import networkx as nx
import osmnx as ox

ox.config(log_console=True)
ox.__version__

import warnings
warnings.resetwarnings()
warnings.filterwarnings("ignore")

class Main:
    def header(self):
        print('Trabalho de Inteligência Artificial - AV2')
        print('* Grupo:\n - Divaldo Aderaldo de Oliveira Júnior (1810534)\n - Igor Oliveira dos Santos (1913439)')

    def chooseSearch(self):
        graph = Graph()
        choice = input("\nQue tipo de procura deseja efetuar?\n\n1) Busca em Largura\n2) Busca em Profundidade\n3) Busca de Custo Uniforme\n4) Busca Gulosa pela Melhor Escolha\n5) A*\n\n")

        if (choice == '1'):
            print('\nGerando grafo...\n')
            graph.plot()
            print('\nIniciando busca...\n')
        elif (choice == '2'):
            print(choice)
        elif (choice == '3'):
            print(choice)
        elif (choice == '4'):
            print(choice)
        elif (choice == '5'):
            print(choice)
        else:
            print('\nSeleção inválida!')
            self.chooseSearch()

        print("\nBusca finalizada!")

        restart = ""

        while (restart.lower() != 'n' and restart.lower() != 's'):
            restart = input("\nGostaria de fazer outra busca? (S/N)\n")
            if (restart.lower() == 's'):
                self.chooseSearch()
            elif (restart.lower() == 'n'):
                print("\nScript finalizado.")
            else:
                print("\nInput inválido!")

class Graph:
    graph = ox.graph.graph_from_place("Paris, France", network_type="drive")

    def plot(self):
        graph = self.graph
        ox.plot.plot_graph(graph)

class Node:

    id = -1
    pai = None

    def __init__(self,id):
        self.id = id

class Grafo:

    matriz = []
    n = 0
    direcionado = False

    def __init__(self,n,direcionado):
        self.n = n
        self.direcionado = direcionado
        for i in range(n):
            self.matriz.append([0]*n)

    def addAresta(self,s,t):
        if(not self.direcionado):
            self.matriz[t][s]=1
        self.matriz[s][t]=1

    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j],end = ' ')
            print()
        print('##########')
        print()

    def bl(self,s,t):
        q = queue.Queue()

        node = Node(s)
        node.pai = Node(-1)

        q.put(node)

        while(not q.empty()):
            aux = q.get()

            # Teste de Objetivo
            if(aux.id == t):
                return aux
            # Teste de Objetivo

            # Expansão de vizinhos
            for i in range(self.n):
                if(self.matriz[aux.id][i] == 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    q.put(node)
            # Expansão de vizinhos

        return aux

main = Main()
main.header()
main.chooseSearch()
