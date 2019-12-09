# -- coding: utf-8 --

# Importacao de bibliotecas
import random
import time
import timeit
import os.path

class Heuristic:

	def __init__(self, url, graph, H, option, incolor=-1):
		self.url = url
		self.graph = graph
		self.H = H
		self.option = option
		self.incolor = incolor

	def Start(self):
		if self.option == 1:
			return self.Sequential()
		elif self.option == 2:
			return self.Random()
		elif self.option == 3:
			return self.Rate()

	# Heuristica: "Coloracao Sequencial"
	# A ordem do vetor eh de 0 ate o numero de vertices
	def Sequential(self):

	    begin = timeit.default_timer()

	    # Cores usadas ate o momento, coloracao parcial valida
	    cores_usadas = 0

	    # Uma lista para controlar a disponibilidade das cores. H eh a quantidade maxima de cores a serem utilizadas
	    disponivel = [True]*self.H

	    # Seta todos os vertices do grafo como incolor
	    for v in range(0, self.graph.getAmountV(), 1):
	        self.graph.getVertices()[v].setColor(self.incolor)

	    for v in range(0, self.graph.getAmountV(), 1):
	        i = 0
	        if(cores_usadas != 0):
	            # Inicialmente, suponhe-se que as cores ja usadas estejam disponivel
	            for i in range(0, cores_usadas, 1):
	                disponivel[i] = True

	        # Pega a lista de vizinhos do vertice v
	        listneighbor = self.graph.getVertices()[v].getNeighbor()

	        if(listneighbor != []):
	            # Se o vizinho estiver pintado com alguma cor, informa que aquela cor nao esta disponivel
	            for n in range(0, len(listneighbor), 1):
	                i = self.graph.getVertices()[(listneighbor[n])].getColor()

	                # Se o vertice vizinho esta colorido
	                if(i != self.incolor):
	                    disponivel[i] = False

	        i = 0
	        # Percorre entre as cores ja usadas no grafo, em busca de uma cor que esteja disponivel
	        for i in range(0, self.H, 1):
	            if(disponivel[i]):
	                break

	        if(i < (cores_usadas-1)):
	            self.graph.getVertices()[v].setColor(i)
	        else:
	            self.graph.getVertices()[v].setColor(cores_usadas)
	            cores_usadas= cores_usadas + 1

	        # Se a quantidade de cores usadas para colorir o grafo for maior 
	        # que o tamanho da paleta de cores dada inicialmente, termina a execucao
	        if(cores_usadas > self.H):
	            print("\t* Aviso: A quantidade de cores usadas no grafo excedeu o tamanho da paleta de cores H.\n")
	            break

	    end = timeit.default_timer()

		# Gera o arquivo de saida
	    self.outFile(cores_usadas, (end - begin))

    # Heuristica: "Coloracao Aleatoria"
    # A ordem do vetor eh randomica
	def Random(self):
		
		begin = timeit.default_timer()

		# Cores usadas ate o momento, coloracao parcial valida
		cores_usadas = 0

		# Uma lista para controlar a disponibilidade das cores. H eh a quantidade maxima de cores a serem utilizadas
		disponivel = [True]*self.H

		listV = []
		listAux = []

		# Seta todos os vertices do grafo como incolor
		for v in range(0, self.graph.getAmountV(), 1):
		    self.graph.getVertices()[v].setColor(self.incolor)
		    listV.append(v)

		for v in range(0, self.graph.getAmountV(), 1):
		    i = 0
		    if(cores_usadas != 0):
		        # Inicialmente, suponhe-se que as cores ja usadas estejam disponivel
		        for i in range(0, cores_usadas, 1):
		            disponivel[i] = True

            # Randomiza um vertice
		    num = random.choice(listV)

		    # Randomiza soh os vertices que ainda nao foram usados
		    while num in listAux:
		    	num = random.choice(listV)
		    listAux.append(num)

		    # Pega a lista de vizinhos do vertice num
		    listneighbor = self.graph.getVertices()[num].getNeighbor()

		    if(listneighbor != []):
		        # Se o vizinho estiver pintado com alguma cor, informa que aquela cor nao esta disponivel
		        for n in range(0, len(listneighbor), 1):
		            i = self.graph.getVertices()[(listneighbor[n])].getColor()

		            # Se o vertice vizinho esta colorido
		            if(i != self.incolor):
		                disponivel[i] = False

		    i = 0
		    # Percorre entre as cores ja usadas no grafo, em busca de uma cor que esteja disponivel
		    for i in range(0, self.H, 1):
		        if(disponivel[i]):
		            break

		    if(i < (cores_usadas-1)):
		        self.graph.getVertices()[v].setColor(i)
		    else:
		        self.graph.getVertices()[v].setColor(cores_usadas)
		        cores_usadas= cores_usadas + 1

		    # Se a quantidade de cores usadas para colorir o grafo for maior 
		    # que o tamanho da paleta de cores dada inicialmente, termina a execucao
		    if(cores_usadas > self.H):
		        print("\t* Aviso: A quantidade de cores usadas no grafo excedeu o tamanho da paleta de cores H.\n")
		        break
		
		end = timeit.default_timer()

		# Gera o arquivo de saida
		self.outFile(cores_usadas, (end - begin))

	# Heuristica: "Coloracao de Grau"
	# A ordem do vetor eh do vertice com maior grau ate o vertice com menor grau
	def Rate(self):
		
	    begin = timeit.default_timer()

		# Cores usadas ate o momento, coloracao parcial valida
	    cores_usadas = 0

	    # Uma lista para controlar a disponibilidade das cores. H eh a quantidade maxima de cores a serem utilizadas
	    disponivel = [True]*self.H

	    # Seta todos os vertices do grafo como incolor
	    for v in range(0, self.graph.getAmountV(), 1):
	        self.graph.getVertices()[v].setColor(self.incolor)

        # Ordena os vertices de acordo com quem tem o maior grau        	
	    self.graph.setListVertices(self.graph.rateSort());

	    for v in range(0, self.graph.getAmountV(), 1):
	        i = 0
	        if(cores_usadas != 0):
	            # Inicialmente, suponhe-se que as cores ja usadas estejam disponivel
	            for i in range(0, cores_usadas, 1):
	                disponivel[i] = True

	        # Pega a lista de vizinhos do vertice v
	        listneighbor = self.graph.getVertices()[v].getNeighbor()

	        if(listneighbor != []):
	            # Se o vizinho estiver pintado com alguma cor, informa que aquela cor nao esta disponivel
	            for n in range(0, len(listneighbor), 1):
	                i = self.graph.getVertices()[(listneighbor[n])].getColor()

	                # Se o vertice vizinho esta colorido
	                if(i != self.incolor):
	                    disponivel[i] = False

	        i = 0
	        # Percorre entre as cores ja usadas no grafo, em busca de uma cor que esteja disponivel
	        for i in range(0, self.H, 1):
	            if(disponivel[i]):
	                break

	        if(i < (cores_usadas-1)):
	            self.graph.getVertices()[v].setColor(i)
	        else:
	            self.graph.getVertices()[v].setColor(cores_usadas)
	            cores_usadas= cores_usadas + 1

	        # Se a quantidade de cores usadas para colorir o grafo for maior 
	        # que o tamanho da paleta de cores dada inicialmente, termina a execucao
	        if(cores_usadas > self.H):
	            print("\t* Aviso: A quantidade de cores usadas no grafo excedeu o tamanho da paleta de cores H.\n")
	            break
        
	    end = timeit.default_timer()

		# Gera o arquivo de saida
	    self.outFile(cores_usadas, (end - begin))

	# Gera o arquivo de saida
	def outFile(self, cores_usadas, timeOut):
		
		fileOut = self.url.replace('.col', '.txt')

		# Se o arquivo nao existe cria, se existe apenas da o append
		if os.path.isfile(fileOut):
			arq = open(fileOut, 'a')
		else:
			arq = open(fileOut, 'w')

		texto = []
		texto.append(str(cores_usadas) + '\t')
		texto.append(str(timeOut) + '\n')
		arq.writelines(texto)
		arq.close()