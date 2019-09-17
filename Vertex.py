# -- coding: utf-8 --

# Importacao de bibliotecas
import sys

class Vertex:

    # Construtor da classe
    def __init__(self):
        self.color = 0
        self.neighbor = []

    # Seta a cor do vertice
    def setColor(self, color):
        self.color = color

    # Pega a cor do vertice
    def getColor(self):
        return self.color

    # Seta o vizinho do vertice na lista de vizinhos
    def setNeighbor(self, idneighbor):
        self.neighbor.append(idneighbor)

    # Pega os vizinhos do vertice
    def getNeighbor(self):
        return self.neighbor
