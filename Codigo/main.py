##################################################################
# Gerador de modelo em AMPL do Problema de Coloração de Vértices #
#                                                                #
# Desenvolvedores: Jefferson Alves                               #
#                  Vinícius Araújo                               #
#                  Vinícius Morais                               #
# Como Executar(Ex):                                             #
#	python3 main.py ./Instâncias/myciel5.col 9 2                 #
#                                                                #
# Gera um arquivo de saida dentro da pasta Instâncias com a      #
# quantidade de cores usadas e o tempo da execução da heurística,#
# além claro de gerar o modelo AMPL.
##################################################################

# -- coding: utf-8 --

# Importacao de bibliotecas
import sys
import ReadFile
import WriteMod
import Heuristic
import Metaheuristic

# Pega todos os parametros informados por linha de comando
param = sys.argv[1:]

# Url da instancia
url = param[0]

# Quantidade de cores
amountC = param[1]
# Opcao 1: Heuristica com o vetor sendo sequencial
# Opcao 2: Heuristica com o vetor sendo aleatorio
# Opcao 3: Heuristica com o vetor sendo ordenado do vertice com maior grau para o vertice com menor grau

#            OU

# Opcao 1: Metaheuristica GRASP
# Opcao 2: Metaheuristica SA
# Opcao 3: Metaheuristica BRKGA
option = param[2]

# Executar a Heuristica ou a Metaheuristica
method = param[3]

# Realiza a leitura do benchmark
graph = ReadFile.readFile(url)

# Escreve o arquivo AMPL
#WriteMod.WriteMod(graph, int(amountC))

# Seta os vizinhos de cada vertice
graph.adjacentVertices()

# Metodo a ser usado
if method == "-h":
	# Usa uma das 3 heuristicas para resolver o problema
	heuristic = Heuristic.Heuristic(url, graph, int(amountC), int(option))
	heuristic.Start()
elif method == "-m":
	# Usa uma das 3 meta-heuristicas para resolver o problema
	metaHeuristic = Metaheuristic.Metaheuristic(url, graph, int(amountC), int(option))
	metaHeuristic.Start()
else:
	print("O método nao foi passado corretamente (-h: Heurística, -m: Metaheurística)")