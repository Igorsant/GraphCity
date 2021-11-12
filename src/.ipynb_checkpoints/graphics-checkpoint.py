import pygame
from pygame.locals import *
from sys import exit
from threading import Thread
from graph import Graph

class Graphics(Thread):

    gameInstance = pygame
    
    font = None

    def __init__(self, graph: Graph):
        Thread.__init__(self)
        self.graph = graph

    def run(self):
        self.gameInstance.init()
        self.font = pygame.font.SysFont("Arial", 25)

        largura = 640
        altura = 640
        self.tela = self.gameInstance.display.set_mode((largura, altura))
        self.gameInstance.display.set_caption('Inteligência Artificial')

        
        while True:
            for event in self.gameInstance.event.get():
                if event.type == QUIT:
                    self.gameInstance.quit()
                    exit()
            self.drawRects()
            self.draw_grids()
            self.gameInstance.display.update()

    def drawRects(self):
        for i in range(20):
            for j in range(20):
                #0 1 2 X S E
                color = (0,0,0)
                if self.graph.matrix[i][j].value == 'S':
                    color = (0,0,255)
                if self.graph.matrix[i][j].value == '0':
                    color = (255,255,255)
                if self.graph.matrix[i][j].value == '1':
                    color = (0,255,255)
                if self.graph.matrix[i][j].value == '2':
                    color = (255,255,0)
                if self.graph.matrix[i][j].value == 'X':
                    color = (0,0,0)
                if self.graph.matrix[i][j].value == 'E':
                    color = (255,0,0)

                self.gameInstance.draw.rect(self.tela, color, (i*32, j*32, 32, 32))
                
                if (self.graph.displayCosts):
                    displayText = ""
                    
                    if (self.graph.matrix[i][j].value not in ["S", "E"]):
                        displayText = str(self.graph.matrix[i][j].costValue)
                    
                    text = self.font.render(displayText, True, (0, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (i*32 + 16, j*32 + 16)
                    self.tela.blit(text, textRect)
    
    def draw_grids(self):
        for i in range(20):
            self.gameInstance.draw.line(self.tela, (0, 0, 0), (i*32, 0), (i*32, 640))
        for i in range(20):
            self.gameInstance.draw.line(self.tela, (0, 0, 0), (0, i*32), (640, i*32))

    def quit(self):
        self.gameInstance.event.post(pygame.event.Event(QUIT, message="Finishing game..."))
