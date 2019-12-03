import random

class GRASP:
	# Construtor
	def __init__(self, graph):
		# A variavel solucao, inicialmente eh passada como None, vazia
		self.solution = []
		# ListColors, inicialmente eh passada como uma lista de tamanho = qtdVertices no grafo do tipo boolean com todas as posicoes com valor False, indicando que a cor nao foi totalmente verificada no RCL
		self.listColors = self.initListColors(graph)

		# Roda o GRASP
		self.runGrasp(graph)

	# Resetar as cores dos vertices do grafo com incolor (-1)
	def resetGraph(self, graph):
		for v in range(0, graph.getAmountV(), 1):
			graph.getVertices()[v].setColor(-1)

	# Inicializa a lista de cores boolean
	def initListColors(self, graph):
		boolean = []

		for _ in range(0, graph.getAmountV(), 1):
			boolean.append(False)

		return boolean

	# Fase construtiva GRASP
	def constructivePhase(self, graph):
		# Vertices nao coloridos
		candidatos = []
		# Os vertices na lista de candidatos de maior grau/maior grau dos vizinhos nao coloridos
		rcl = []
		# Dicionario para salvar a quantidade de vizinhos descoloridos em cada candidato
		vizDescoloridos = {}
		
		# Copia os vertices nao coloridos para serem os candidatos
		for v in range(0, graph.getAmountV(), 1):
			if(graph.getVertices()[v].getColor() == -1):
				# Adiciona o candidato na lista de candidatos e cria um id no dicionario conforme sua posicao no grafo
				candidatos.append(graph.getVertices()[v])
				vizDescoloridos[v] = -1
		
		# Se nao houver candidatos, retorna a solucao que encontrou
		if(candidatos == []):
			return self.solution

		# Passa todos os id's no dicionario para uma lista, facilitando o passeio no for abaixo
		listAux = list(vizDescoloridos)

		# Seta a quantidade de vizinhos descoloridos de cada candidato -- criterio de separacao de melhores
		for v in range(0, len(candidatos), 1):
			qtdVizDescoloridos = 0

			for n in range(0, len(graph.getVertices()[v].getNeighbor()), 1):
				if(graph.getVertices()[n].getColor() == -1):
					qtdVizDescoloridos += 1
			
			vizDescoloridos[listAux[v]] = qtdVizDescoloridos
		
		# Seta o RCL como sendo os melhores a partir do criterio de verificacao na lista de candidatos
		maior = -1
		
		for v in range(0, len(candidatos), 1):
			if(vizDescoloridos[listAux[v]] > maior):
				maior = vizDescoloridos[listAux[v]]
				rcl = []
				rcl.append(graph.getVertices()[listAux[v]])
			elif(vizDescoloridos[listAux[v]] == maior):
				rcl.append(graph.getVertices()[listAux[v]])
		
		paletaCores = graph.getAmountV()

		while (rcl != []):
			#Pega um vertice aleatotio dentro da RCL
			escolhido = random.choice(rcl)

			for n in escolhido.getNeighbor():
				if(graph.getVertices()[n].getColor() != -1):
					self.listColors[graph.getVertices()[n].getColor()] = True

			for c in range(0, len(self.listColors), 1):
				if(self.listColors[c] == False):
					break
			
			# Pega o indice do vertice escolhido
			indice = graph.getVertices().index(escolhido)
			graph.getVertices()[indice].setColor(c)
			
			self.solution.append(graph.getVertices()[indice])
			
			# Remove seus vizinhos
			for n in escolhido.getNeighbor():
				if(graph.getVertices()[n] in rcl):
					rcl.remove(graph.getVertices()[n])
			
			# Remove o escolhido da RCL
			rcl.remove(escolhido)
		
		# Seta a cor como usada
		self.listColors[c] = True
		# Chama recursivamente a fease construtiva
		self.constructivePhase(graph)
	
	def runGrasp(self, graph):
		# Reseta as cores do grafo
		self.resetGraph(graph)
		# Chama a fase construtiva do GRASP
		self.constructivePhase(graph)

		# Escreve a solucao inicial da fase construtiva
		for noh in self.solution:
			print(noh.getColor())