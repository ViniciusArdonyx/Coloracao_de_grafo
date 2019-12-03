##################################################################
#           Simulated Annealing para Coloração de Grafos         #
#                                                                #
# Desenvolvedores: Jefferson Alves                               #
#                  Vinícius Araújo                               #
#                  Vinícius Morais                               #
##################################################################
# -- coding: utf-8 --

# Importacao de bibliotecas
import math
import random
import Vertex

class SA:
	#
	# Cria a solucao incial do problema, eh usada uma heuristica randomica feita pelo proprio grupo
	#
	def initialSolution(self, graph):
		return self.HeuristicRandom(graph)
	#
	# Gera um solucao S' de N(S)
	#
	def generateNewSolution(self, graph, amountColor):

		# Laco ate randomizar um vertice que tenha cores validas
		while True:

			# Randomiza um vertice do grafo
			index = random.randint(0, graph.getAmountV() - 1)

			# Vertice escolhido
			vertice = graph.getVertices()[index]

			# Cor deste vertice
			color = vertice.getColor()

			# Cores dele dos vizinhos dele
			invalidColors = []

			# Insere a cor do vertice
			invalidColors.append(color)

			# Cores dos vizinhos
			for i in vertice.getNeighbor():
				invalidColors.append(graph.getVertices()[i].getColor())

			# Cores validas
			validColors = [i for i in range(amountColor) if i not in invalidColors]

			# Apenas se tiver cor na lista
			if len(validColors) != 0:

				# Randomiza uma cor valida
				# color = random.choice(validColors)

				# Pega a menor cor dentre as validas
				color = min(validColors)

				# Adiciona a nova cor ao vertice randomizado
				graph.getVertices()[index].setColor(color)

				# A quantidade de cores pode ter sido alterada
				(amountColor, sumOfColor) = graph.checkColor()

				return graph, amountColor, sumOfColor
	#
	# Heuristica: "Coloracao Aleatoria"
    # A ordem do vetor eh randomica
    #
	def HeuristicRandom(self, graph):

		incolor = -1

		# Cores usadas ate o momento, coloracao parcial valida
		cores_usadas = 0

		# Uma lista para controlar a disponibilidade das cores. H eh a quantidade maxima de cores a serem utilizadas
		disponivel = [True] * graph.getAmountV()

		listV = []
		listAux = []

		# Seta todos os vertices do grafo como incolor
		for v in range(0, graph.getAmountV(), 1):
		    graph.getVertices()[v].setColor(incolor)
		    listV.append(v)

		for v in range(0, graph.getAmountV(), 1):
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
		    listneighbor = graph.getVertices()[num].getNeighbor()

		    if(listneighbor != []):
		        # Se o vizinho estiver pintado com alguma cor, informa que aquela cor nao esta disponivel
		        for n in range(0, len(listneighbor), 1):
		            i = graph.getVertices()[(listneighbor[n])].getColor()

		            # Se o vertice vizinho esta colorido
		            if(i != incolor):
		                disponivel[i] = False

		    i = 0
		    # Percorre entre as cores ja usadas no grafo, em busca de uma cor que esteja disponivel
		    for i in range(0, graph.getAmountV(), 1):
		        if(disponivel[i]):
		            break

		    if(i < (cores_usadas-1)):
		        graph.getVertices()[v].setColor(i)
		    else:
		        graph.getVertices()[v].setColor(cores_usadas)
		        cores_usadas= cores_usadas + 1

		    # Se a quantidade de cores usadas para colorir o grafo for maior 
		    # que o tamanho da paleta de cores dada inicialmente, termina a execucao
		    if(cores_usadas > graph.getAmountV()):
		        print("\t* Aviso: A quantidade de cores usadas no grafo excedeu o tamanho da paleta de cores H.\n")
		        break

		(amountColor, sumOfColor) = graph.checkColor()

		return graph, cores_usadas, sumOfColor
	#
	# Simulated Annealing para o problema de coloracao de grafos
	#
	def execute(self, graph, initialTemp, finalTemp, alpha, saMax):

		# Define a temperatura inicial do sistema
		temp = initialTemp

		# Cria a solucao incial do problema
		(solution, objetive, sumOfColor) = self.initialSolution(graph)

		# Melhor grafo encontrado
		overall = solution

		# Melhor quantidade de cores encontrada
		objOverall = objetive

		# Executa o laco principal do metodo (temperatura)
		while temp > finalTemp:

			# Iteracao
			iteration = 0
			
			# Executa o laco secundario do metodo (iteracoes)
			while saMax > iteration:

				# Gera um solucao S' de N(S)
				(solution, objNeighbor, sumOfColor) = self.generateNewSolution(solution, objetive)

				# Calcula o delta
				delta = objNeighbor - objetive

				# Se o delta for negativo, o vizinho eh MELHOR, entao atualiza
				if delta < 0:

					# Atualiza solucao diretamente
					objetive = objNeighbor

					# Se a solucao atual da iteracao for melhor que a overall, atualiza
					if objNeighbor < objOverall:

						# print("\t\t @@@" + str(objNeighbor), str(sumOfColor))

						# Atualiza as melhores solucoes
						objOverall = objNeighbor
						overall = solution

				# Se o delta for positivo, o vazinho eh PIOR, entao ira passar por um criterio para aceitar ou nao
				else:

					# Calcula o criterio
					criterion = math.exp(-delta / temp)

					# Sorteia um numero aleatorio entre 0 e 1
					randomized = random.random()

					# print(str(delta/temp) + "\t" + str(criterion) + "\t" + str(randomized) + "\t" + str(randomized < criterion))

					# Verifica se aceita
					if randomized < criterion:

						# Atualiza solucao diretamente
						objetive = objNeighbor

				# Incrementa a iteracao
				iteration += 1

			# Atualiza a temperatura utilizando algum esquema de resfriamento
			# 	Usando o esquema Geometrico
			temp = temp * alpha
		
		# Retorna a quantidade de cores que foi usada para colorir o grafo e o grafo em si
		return objOverall, overall