import pygame
from pygame.locals import *
from sys import exit
from threading import Thread
from graph import Graph

class Graphics(Thread):

    gameInstance = pygame

    def __init__(self, graph: Graph):
        Thread.__init__(self)
        self.graph = graph

    def run(self):
        self.gameInstance.init()

        largura = 640
        altura = 640
        self.tela = self.gameInstance.display.set_mode((largura, altura))
        self.gameInstance.display.set_caption('Inteligencia Artificial')

        while True:
            for event in self.gameInstance.event.get():
                if event.type == QUIT:
                    self.gameInstance.quit()
                    exit()
            self.drawRects()
            self.gameInstance.display.update()

    def drawRects(self):
        for i in range(20):
            for j in range(20):
                #0 1 2 X S E
                if self.graph.matrix[i][j].value == 'S':
                    self.gameInstance.draw.rect(self.tela, (0,0,255), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == '0':
                    self.gameInstance.draw.rect(self.tela, (255,255,255), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == '1':
                    self.gameInstance.draw.rect(self.tela, (0,255,255), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == '2':
                    self.gameInstance.draw.rect(self.tela, (255,255,0), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == 'X':
                    self.gameInstance.draw.rect(self.tela, (0,0,0), (i*32, j*32, 32, 32))
                if self.graph.matrix[i][j].value == 'E':
                    self.gameInstance.draw.rect(self.tela, (255,0,0), (i*32, j*32, 32, 32))

    def quit(self):
        self.gameInstance.event.post(pygame.event.Event(QUIT, message="Finishing game..."))
