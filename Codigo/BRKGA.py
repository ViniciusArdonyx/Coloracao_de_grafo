# -- coding: utf-8 --

# Importacao de bibliotecas
import random
import Vertex

class BRKGA:
    TAMPOP  = 50     # Tamanho das populacoes
    QTDGE   = 100    # Quantidade de geracoes
    TAXA    = 0.60   # Probabilidade de pegar do pai na elite
    ELPART  = 0.20   # Porcentagem para enviar para a geracao g+1 da elite(20%)
    MTPART  = 0.15   # Porcentagem para enviar para a geracao g+1 de mutacao(15%)

    #Construtor
    def __init__(self, url, graph, H):
        self.url = url
        self.graph = graph
        self.H = H

        print('Wait, running BRKGA...\n')
        self.brkgaRun()

    # Pega a informacao de quantidade de cores usadas no grafo
    def takeColors(self, individuo):
        return individuo[2]
    
    # Sorteia os pais para o crossover
    def getParents(self, population, tamElit, tamMuta, randKeysSorting, mutacao):
        # Pega um individuo(pai) aleatorio entre a elite da geracao atual
        individuo = random.choice(population[:tamElit])
        pBest = randKeysSorting[individuo[0]]

        if(mutacao):
            # Pega um individuo(pai) aleatorio necessariamente pertencente aos mutantes, piores casos
            individuo = random.choice(population[self.TAMPOP-tamMuta:])
            pRand = randKeysSorting[individuo[0]]
        else:
            # Pega um individuo(pai) aleatorio entre os nao elite da geracao atual
            individuo = random.choice(population[tamElit:])
            pRand = randKeysSorting[individuo[0]]
        
        return (pBest, pRand)

    # Realiza o crossover
    def crossover(self, parent1, parent2):
        child = []

        # Verifica se os pais tem o mesmo tamanho. Se nao houve problema
        if((len(parent1) != len(parent2)) or (len(parent1) != self.graph.getAmountV())
            or (len(parent2) != self.graph.getAmountV())):
            return child

        # Garente que criara um filho do tamanho da quantidade de nohs no grafo
        for i in range(0, self.graph.getAmountV(), 1):
            # Simula moeda, gera um numero aleatorio para ver de quais dos pais pegar o gene i
            coin = random.uniform(0, 1)

            # Verifica o valor gerado da 'moeda'
            if(coin <= self.TAXA):
                child.append(parent1[i])
            else:
                child.append(parent2[i])

        return child

    # Cria um dicionario de listas para as chaves aleatorias
    def getRandomKeysSorting(self):
        randKeysSorting = {} # Dicionario de cada 'membro' da populacao a ser linkado com uma lista

        # Cria um dicionario de listas de cada 'membro' da populacao TAMPOP dos valores de chaves aleatorias de cada gene
        for key in range(0, self.TAMPOP, 1):
            keysSorting = []

            for no in range(0, self.graph.getAmountV(), 1):
                keysSorting.append("%1.3f" % random.uniform(0, 1))

            randKeysSorting[key] = keysSorting
        
        return randKeysSorting
    
    # Funcao para pegar as cores dos vizinhos de um respectivo vertice:
    def getColorAdj(self, vizinhos):
        colorsNeighbors = []

        for v in vizinhos:
            # Adiciono se nao for incolor:
            if self.graph.getVertices()[v].getColor() != -1:
                colorsNeighbors.append(self.graph.getVertices()[v].getColor())
        
        return colorsNeighbors
    
    # Decoder BRKGA:
    def decoder(self, randKeysSorting):
        # Dicionario auxiliar das chaves ordenadas de todos os candidatos
        randAux = {}
        # Guarda a informacao dos vertices(cor e vizinhos) do grafo da populacao
        population = []
        # Transforma em lista os indices do dicionario
        listIndex = list(randKeysSorting)

        # Realiza uma copia das chaves de cada candidato da populacao
        for key in range(0, len(listIndex), 1):
            randAux[listIndex[key]] = randKeysSorting[listIndex[key]].copy()

        # Rodar em cima da lista do candidato atual na lista ordenada das chaves
        for key in range(0, len(listIndex), 1):
            lOriginal = randKeysSorting[listIndex[key]]
            lAuxiliar = randAux[listIndex[key]]
            color = 0
            collided = False
            lVertex = []

            # Adiciona a cor 0 na lista de cores usadas
            usedColors = [0]

            # Ordena as lista de chaves
            lAuxiliar.sort()

            # Limpa o graph(Descolore). Seta todos os vertices do grafo como incolor
            for v in range(0, self.graph.getAmountV(), 1):
                self.graph.getVertices()[v].setColor(-1)

            # Comeca a colorir o grafo do candidato atual analisando cada chave
            for i in range(0, len(lAuxiliar), 1):
                # Retorna o index (qual noh corresponde no grafo)
                indice = lOriginal.index(lAuxiliar[i])
                # Pega indice dos vizinhos
                vizinhos = self.graph.getVertices()[indice].getNeighbor()

                # Pita o vertice com a ultima cor na paleta de cores
                if self.graph.getVertices()[indice].getColor() == -1:
                    self.graph.getVertices()[indice].setColor(color)
                
                # Caso o vertice tenha sido colorido anteriormente, valido se essa cor usada nao é igual a um vertice adj
                # Obs: Isso pq quando verifico um vertice e coloro ele, coloro todos os q nao sao adj, pode ser que 
                # ao fazer isso, eu colora alguns vertices que sao adj entre si, mas nao em questao do vertice analisado
                # no momento:
                coresVizinho = self.getColorAdj(vizinhos)

                if coresVizinho != []:
                    if self.graph.getVertices()[indice].getColor() in coresVizinho:
                        # Tenta reutilizar uma cor existente na paleta de cores que nao colide com nenhuma cor dos vizinhos
                        for c in usedColors:
                            if(not(c in coresVizinho)):
                                collided = False
                                self.graph.getVertices()[indice].setColor(c)
                                break
                            else:
                                collided = True
                        
                        # Se nao pode utilizar nenhuma cor da paleta de cores
                        if(collided):
                            color += 1
                            usedColors.append(color)
                            self.graph.getVertices()[indice].setColor(color)

                for i in range(0, self.graph.getAmountV(), 1):
                    # Se o indice nao estah nos indices dos vizinhos, e o vertice com o respectivo 
                    # indice nao foi colorido adiciono a cor a ele:
                    if (i not in vizinhos) and (self.graph.getVertices()[i].getColor() == -1):
                        self.graph.getVertices()[i].setColor(color)
            
            # Para cada vertece no grafo, cria-se um objeto vertex para guardar as informacoes
            for v in self.graph.getVertices():
                # Cria um vertice
                vertex = Vertex.Vertex()
                # Guarda a cor
                vertex.setColor(v.getColor())

                # Guarda os vizinhos
                for n in range(0, len(v.getNeighbor()), 1):
                    vertex.setNeighbor(v.getNeighbor()[n])
                
                lVertex.append(vertex)
            
            # Cada individuo da populacao eh composto pela: Chave no dicionario; lista de vertices, qtd de cores usadas no grafo
            population.append((listIndex[key], lVertex, len(usedColors)))
        
        return population

    # Procedimento principal para o funcionamento do BRKGA
    def brkgaRun(self):
        g = 0 # Geracao
        tamElit = round(self.TAMPOP * self.ELPART) # Qtd de elementos pertencente a elite
        tamMuta = round(self.TAMPOP * self.MTPART) # Qtd de elementos pertencente a elite

        ### Gera a populacao inicial
        # Dicionario de listas de cada 'membro' da populacao TAMPOP dos valores de chaves aleatorias de cada gene
        randKeysSorting = self.getRandomKeysSorting()

        # Cria os candidatos para a populacao
        population = self.decoder(randKeysSorting)

        while(g < self.QTDGE):
            # A populationG == g+1
            populationG = []

            # Ordena a populacao do melhores(menor numero de cores) resultados para os piores(maior numero de cores)
            population.sort(key=self.takeColors)
            
            # Transforma em lista os indices do dicionario
            listIndex = list(randKeysSorting)
            # Para salvar as chaves no dicionario de chaves aleatorias dos 'membros' elite
            listElite = []
            # Para salvar as chaves no dicionario de chaves aleatorias dos 'membros' mutantes
            listMutantes = []

            # A porcentagem elite(ELPART)
            for i in range(0, tamElit, 1):
                listElite.append(population[i][0])
                listIndex.remove(population[i][0])

            # A porcentagem mutantes(MTPART)
            for i in range((self.TAMPOP - tamMuta), self.TAMPOP, 1):
                listMutantes.append(population[i][0])
                listIndex.remove(population[i][0])

            # Realiza a mutacao
            for i in range(0, tamMuta, 1):
                # Sorteia os pares de pais para a mutacao
                (parentsB, parentsR) = self.getParents(population, tamElit, tamMuta, randKeysSorting, True)

                # Crossover
                child = self.crossover(parentsB, parentsR)

                # Para evitar continuar rodando se houver erro ao gerar um novo candidato para a nova populacao
                # Evitando propagacao de erro
                if(child == []):
                    print('ERRO: tamanho das chaves dos casos pais diferem, impossivel criar um caso filho.')
                    exit()

                # Substitui o antigo membro mutante na posicao i pelo novo membro filho gerado no crossover
                randKeysSorting[listMutantes[i]] = child.copy()

            # Gera o restante da populacao g+1 sendo: (TAMPOP - (tamElit + tamMuta))
            for i in range(0, (self.TAMPOP - (tamElit + tamMuta)), 1):
                # Sorteia os pares de pais
                (parentsB, parentsR) = self.getParents(population, tamElit, tamMuta, randKeysSorting, False)

                # Crossover
                child = self.crossover(parentsB, parentsR)

                # Para evitar continuar rodando se houver erro ao gerar um novo candidato para a nova populacao
                # Evitando propagacao de erro
                if(child == []):
                    print('ERRO: tamanho das chaves dos casos pais diferem, impossivel criar um caso filho.')
                    exit()

                # Substitui o antigo membro nao mutante e nao elite na posicao i pelo novo membro filho gerado no crossover
                randKeysSorting[listIndex[i]] = child.copy()
            
            populationG = self.decoder(randKeysSorting)

            # Atualiza populacao
            population = populationG.copy()

            # Geracao g+1
            g += 1
        
        # Ordena a populacao do melhores(menor numero de cores) resultados para os piores(maior numero de cores)
        population.sort(key=self.takeColors)

        # Mostra qual foi a melhor solucao na populacao final
        print(population[0])
