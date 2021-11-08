import pygame
from pygame.locals import *
from sys import exit
import time
from threading import Thread
from graph import Graph

class Graphics(Thread):
    
    def __init__(self, graph: Graph):
        Thread.__init__(self)
        self.graph = graph
        
    def run(self):
        pygame.init()

        largura = 640
        altura = 640
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Inteligencia Artificial')

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            self.drawRects()
            pygame.display.update()

    def drawRects(self):
        for i in range(20):
            for j in range(20):
                #0 1 2 X S E
                if self.graph.matrix[i][j].value == 'S':
                    pygame.draw.rect(self.tela, (0,0,255), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == '0':
                    pygame.draw.rect(self.tela, (255,255,255), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == '1':
                    pygame.draw.rect(self.tela, (0,255,255), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == '2':
                    pygame.draw.rect(self.tela, (255,255,0), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == 'X':
                    pygame.draw.rect(self.tela, (0,0,0), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == 'E':
                    pygame.draw.rect(self.tela, (255,0,0), (i*32, j*32, 32, 32))
                    



       
        


