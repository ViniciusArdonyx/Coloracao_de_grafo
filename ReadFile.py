# -- coding: utf-8 --

# Importacao de bibliotecas
import sys
import Graph
import Vertex

# Lendo o arquivo
def readFile(url):
    # Cria um grafo
    graph = Graph.Graph()

    # Abre o arquivo em modo leitura e copia tudo o que tem la para essa variavel
    file = open(url, 'r')

    # Percorre cada linha
    for line in file:
        # Divide a linha em varias a cada espaco encontrado
        data = line.split()

        # Se o tamanho da linha for 0 quer dizer que nao tem nada nela
        if len(data) == 0:
            continue

        # Se o primeiro caractere for um "c", a linha deve ser ignorada
        if data[0] == "c":
            continue

        # Se o primeiro caractere for um "p", ira ser informado a quantidade de vertices e arestas
        if data[0] == "p":
            # Quantidade de vertices
            if data[2].isdigit():
                if int(data[2]) >= 0:
                    graph.setAmountV(int(data[2]))

            # Quantidade de arestas
            if data[3].isdigit():
                if int(data[3]) >= 0:
                    graph.setAmountE(int(data[3]))

        # Se o primeiro caractere for um "e", ira ser informado as ligacoes
        if data[0] == "e":
            graph.setEdges([data[1], data[2]])

    # Insere os vertices no grafo
    for i in range(graph.getAmountV()):
        # Cria um vertice
        vertex = Vertex.Vertex()

        # Insere ele na lista de vertices do grafo
        graph.setVertices(vertex)

    # Fecha o arquivo apos finalizar a leitura
    file.close()

    return graph
