# -- coding: utf-8 --

# Importacao de bibliotecas
import sys

class Graph:

    # Construtor da classe
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.amountV = 0
        self.amountE = 0

    # Seta o vertice na lista de vertices do grafo
    def setVertices(self, vertex):
        self.vertices.append(vertex)

    # Pega os vertices do grafo
    def getVertices(self):
        return self.vertices

    # Seta a aresta na lista de arestas do grafo
    def setEdges(self, edge):
        self.edges.append(edge)

    # Pega as arestas do grafo
    def getEdges(self):
        return self.edges

    # Seta a quantidade de vertices que tem no grafo
    def setAmountV(self, amountV):
        self.amountV = amountV

    # Pega a quantidade de vertices que tem no grafo
    def getAmountV(self):
        return self.amountV

    # Seta a quantidade de arestas que tem no grafo
    def setAmountE(self, amountE):
        self.amountE = amountE

    # Pega a quantidade de arestas que tem no grafo
    def getAmountE(self):
        return self.amountE

    # Seta os vertices adjacentes a cada vertice do grafo
    def adjacentVertices(self):
        # Retorna a lista de vertices
        nodes = self.getVertices()

        # Retorna a lista dos pares de vertices, indicando a existencia de uma ligacao, uma aresta
        connections = self.getEdges()

        for e in range(0, self.getAmountE(), 1):
            nodes[int(connections[e][0])-1].setNeighbor(int(connections[e][1])-1)
            nodes[int(connections[e][1])-1].setNeighbor(int(connections[e][0])-1)

    # Imprime na tela os atributos do grafo
    def toString(self):
        string = "Qtde Vértices: [" + str(self.amountV) + "]\n"
        string += "Qtde Arestas: [" + str(self.amountE) + "]\n\n"
        
        if len(self.edges) == 0:
            string += "Não tem ligações"
        else:
            string += "--Ligações--\n"
            for e in self.edges:
                string += "[" + e[0] + "]--[" + e[1] + "]"

        return string