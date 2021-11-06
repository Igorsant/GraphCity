import queue

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
        

g = Grafo(10,False)

g.printMatriz()

g.addAresta(0, 2)
g.addAresta(1, 3)
g.addAresta(2, 3)
g.addAresta(3, 5)
g.addAresta(5, 4)
g.addAresta(3, 6)
g.addAresta(6, 9)
g.addAresta(4, 7)
g.addAresta(4, 8)
g.addAresta(8, 9)

g.printMatriz()

objetivo = g.bl(0, 9)
   
while(objetivo.id != -1):
    print(objetivo.id)
    objetivo = objetivo.pai