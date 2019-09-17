##################################################################
# Gerador de modelo em AMPL do Problema de Coloração de Vértices #
#                                                                #
# Desenvolvedores: Jefferson Alves                               #
#                  Vinícius Araújo                               #
#                  Vinícius Morais                               #
##################################################################

# -- coding: utf-8 --

# Importacao de bibliotecas
import sys
import ReadFile
import WriteMod
import Coloring
from timeit import default_timer as timer

# Pega todos os parametros informados por linha de comando
param = sys.argv[1:]

url = param[0]
amountC = param[1]

# Realiza a leitura do benchmark
graph = ReadFile.readFile(url)

# Escreve o arquivo AMPL
WriteMod.WriteMod(graph, int(amountC))

# Seta os vizinhos de cada vertice
graph.adjacentVertices()

inicio = None
inicio = timer()

# Heurista de "Coloracao Sequencial"
coloration = Coloring.UGRAPHsequentialColoring(graph, int(amountC))

fim = None
fim = timer()

print("A menor quantidade de cores encontrada: %d" %coloration)
print("Tempo de execucao: %f\n" %(fim-inicio))
