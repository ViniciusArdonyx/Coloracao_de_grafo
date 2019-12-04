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

		i = 0

		# Percorre todos os vertices do grafo
		for vertex in graph.getVertices():

			# Todos os vertices teram cores diferentes
			vertex.setColor(i)

			i += 1

		(amountColor, sumOfColor) = graph.checkColor()

		return graph, amountColor, sumOfColor


		# return self.HeuristicRandom(graph)
	#
	# Gera um solucao S' de N(S)
	#
	def generateNewSolution(self, graph, amountColor):

		# Laco ate randomizar um vertice que tenha cores validas
		for aux in range(5):

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

				aux = 0

				# Randomiza uma cor valida
				# color = random.choice(validColors)

				# Pega a menor cor dentre as validas
				color = min(validColors)

				# Adiciona a nova cor ao vertice randomizado
				graph.getVertices()[index].setColor(color)

				# A quantidade de cores pode ter sido alterada
				(amountColor, sumOfColor) = graph.checkColor()

				return graph, amountColor, sumOfColor

		# Nao encontrou um vertice randomizado valido entao percorre todos os vertices procurando um valido
		for vertex in graph.getVertices():

			# Cor deste vertice
			color = vertex.getColor()

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

				aux = 0

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
	# Simulated Annealing para o problema de coloracao de grafos
	#
	def runSa(self, graph, initialTemp, finalTemp, alpha, saMax, pure, solution, objetive):

		# Define a temperatura inicial do sistema
		temp = initialTemp

		# Utiliza o SA puro
		if pure:
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

			# print(temp)

			# Atualiza a temperatura utilizando algum esquema de resfriamento
			# 	Usando o esquema Geometrico
			temp = temp * alpha
		
		# Retorna a quantidade de cores que foi usada para colorir o grafo e o grafo em si
		return objOverall, overall