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

    # Seta uma nova lista de vertices
    def setListVertices(self, vertices):
        self.vertices = vertices

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

    # Ordena os vertices de acordo com quem tem o maior grau
    def rateSort(self):

        greaterRate = 1
        newList = []

        # Procura pelo maior grau
        for i in range(self.getAmountV()):
            currentRate = len(self.getVertices()[i].getNeighbor())
            if currentRate > greaterRate:
                greaterRate = currentRate

        # Procura pelos vertices que tem o mesmo grau do maior grau ate chegar no valor de 1 grau
        for i in range(greaterRate, 1, -1):
            for j in range(self.getAmountV()):
                if len(self.getVertices()[j].getNeighbor()) == i:
                    newList.append(self.getVertices()[j])

        return newList


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