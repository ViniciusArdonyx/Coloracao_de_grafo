# -- coding: utf-8 --

# Importacao de bibliotecas
import random
import time
import timeit
import os.path
# import GRASP
import SA
# import BRKGA

class Metaheuristic:

	def __init__(self, url, graph, H, option, incolor=-1):
		self.url = url
		self.graph = graph
		self.H = H
		self.option = option
		self.incolor = incolor

	def Start(self):
		if self.option == 1:
			return self.GRASP()
		elif self.option == 2:
			return self.SA()
		elif self.option == 3:
			return self.BRKGA()

	# Metaheuristica: Greedy Randomized Adaptive Search Procedure
	def GRASP(self):

		begin = timeit.default_timer()

		# grasp = GRASP.GRASP()
		# cores_usadas = grasp.execute()

		end = timeit.default_timer()

		# Gera o arquivo de saida
		self.outFile(cores_usadas, (end - begin))

	# Metaheuristica: Simulated Annealing
	def SA(self):
		
		begin = timeit.default_timer()

		sa = SA.SA()
		cores_usadas, self.graph = sa.execute(self.graph, 10000, 20, 0.95, 1000)
		
		end = timeit.default_timer()

		# Gera o arquivo de saida
		self.outFile(cores_usadas, (end - begin))

	# Metaheuristica: Biased Random Key Genetic Algorithm
	def BRKGA(self):
		
		begin = timeit.default_timer()

		# brkga = BRKGA.BRKGA()
		# cores_usadas = brkga.execute()
	
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