# -- coding: utf-8 --

# Heuristica: "Coloracao Sequencial"
def UGRAPHsequentialColoring(graph, H):
    # Cores usadas ate o momento, coloracao parcial valida
    cores_usadas = 0

    # Uma lista para controlar a disponibilidade das cores. H eh a quantidade maxima de cores a serem utilizadas
    disponivel = [True]*H

    # Seta todos os vertices do grafo como incolor
    for v in range(0, graph.getAmountV(), 1):
        graph.vertices[v].setColor(-1)

    for v in range(0, graph.getAmountV(), 1):
        i = 0
        if(cores_usadas != 0):
            # Inicialmente, suponhe-se que as cores ja usadas estejam disponivel
            for i in range(0, cores_usadas, 1):
                disponivel[i] = True

        # Pega a lista de vizinhos do vertice v
        listneighbor = graph.vertices[v].getNeighbor()

        if(listneighbor != []):
            # Se o vizinho estiver pintado com alguma cor, informa que aquela cor nao esta disponivel
            for n in range(0, len(listneighbor), 1):
                i = graph.vertices[(listneighbor[n])].getColor()

                # Se o vertice vizinho esta colorido
                if(i != -1):
                    disponivel[i] = False

        i = 0
        # Percorre entre as cores ja usadas no grafo, em busca de uma cor que esteja disponivel
        for i in range(0, H, 1):
            if(disponivel[i]):
                break

        if(i < (cores_usadas-1)):
            graph.vertices[v].setColor(i)
        else:
            graph.vertices[v].setColor(cores_usadas)
            cores_usadas= cores_usadas + 1

        # Se a quantidade de cores usadas para colorir o grafo for maior 
        # que o tamanho da paleta de cores dada inicialmente, termina a execucao
        if(cores_usadas > H):
            print("\t* Aviso: A quantidade de cores usadas no grafo excedeu o tamanho da paleta de cores H.\n")
            break

    return cores_usadas
