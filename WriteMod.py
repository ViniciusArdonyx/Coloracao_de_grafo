# -- coding: utf-8 --

class WriteMod:

    # Construtor
    def __init__(self, grafo, H):
        self.arquivo(grafo, H)

    # Escreve no arquivo AMPL que sera gerado as variaveis binarias Wi
    def setar_variaveisWi(self, file, H):
        # Evitar lixo de memoria
        varWi = ''

        # Variaveis binarias para o Wi
        for i in range(0, H, 1):
            varWi = varWi +'var w'+ str(i+1) +' binary;\n'

        file.write(varWi)

    # Escreve no arquivo AMPL que sera gerado as variaveis binarias Xvi
    def setar_variaveisXvi(self, file, H, V):
        # Evitar lixo de memoria
        varXvi = ''

        # Variaveis binarias para o Xvi
        for v in range(0, V, 1):
            for i in range(0, H, 1):
                varXvi = varXvi +'var x'+ str(v+1)+'v'+ str(i+1) +'c binary;\n'
            
        file.write(varXvi)

    # Escreve no arquivo AMPL que sera gerado a funcao objetiva do problema de coloracao
    def calc_objetivo(self, file, colors, H):
        objetivo = 'minimize NumCores: '

        # Salva o nome da funcao objetiva para ser utilizada no display posteriormente
        colors.append("NumCores")

        for i in range(0, H, 1):
            if(i == (H-1)):
                # Se for o ultimo Wi a ser inserido, acrescenta o ";"
                objetivo = objetivo +'w'+ str(i+1) +';'
            else:
                # Enquanto nao for o ultimo Wi, finaliza com o sinal de "+"
                objetivo = objetivo +'w'+ str(i+1) +' + '
            
            # Salva as cores para ser utilizada no display posteriormente
            colors.append('w'+ str(i+1))

        file.write(objetivo + '\n')

    # Escreve no arquivo AMPL que sera gerado o primeiro conjunto de restricoes do problema de coloracao
    def conj_restricoes1(self, file, H, V):
        # Evitar lixo de memoria
        restricao = ''

        for v in range(0, V, 1):
            # Nome da restricao, dada para cada vertice do grafo, indicando que podera receber apenas uma cor
            restricao = 'vert'+ str(v+1) +': '

            for i in range(0, H, 1):
                if(i == (H-1)):
                    # Se for o ultimo Xvi a ser inserido, acrescenta "= 1;"
                    restricao = restricao+ 'x'+ str(v+1)+'v'+ str(i+1) +'c = 1;'
                else:
                    # Enquanto nao for o ultimo Xvi, finaliza com o sinal de "+"
                    restricao = restricao+ 'x'+ str(v+1)+'v'+ str(i+1) +'c + '
            	
            file.write(restricao + '\n')

    # Escreve no arquivo AMPL que sera gerado o segundo conjunto de restricoes do problema de coloracao
    def conj_restricoes2(self, file, H, grafo):
        # Evitar lixo de memoria
        restricao = ''

        # Retorna os pares de vertices, indicando a existencia de uma ligacao, uma aresta
        arestas = grafo.getEdges()

        for e in range(0, grafo.getAmountE(), 1):
            for i in range(0, H, 1):
                # Nome da restricao, indicando que os vizinhos nao podem compartilhar da mesma cor
                restricao = 'viz'+ str(arestas[e][0])+'p'+ str(arestas[e][1])+'c'+ str(i+1) +': '

                # Xui + Xvi - Wi <= 0
                restricao = restricao +'x'+ str(arestas[e][0])+'v'+ str(i+1) + 'c + x'+ str(arestas[e][1])+'v' + str(i+1) +'c - w'+ str(i+1) +' <= 0;'
                file.write(restricao + '\n')

    # Gera o arquivo AMPL
    def arquivo(self, grafo, H):
        colors = []

        # Cria o arquivo
        file = open('Coloracao.mod','w')

        # Insere as declaracoes de variaveis no arquivo AMPL
        self.setar_variaveisWi(file, H)
        self.setar_variaveisXvi(file, H, grafo.getAmountV())
        file.write("\n")

        # Insere a funcao objetivo no arquivo AMPL
        self.calc_objetivo(file,colors,H)
        
        # Insere as retricoes que fazem parte do problema no arquivo AMPL
        file.write("subject to\n")
        self.conj_restricoes1(file, H, grafo.getAmountV())
        self.conj_restricoes2(file, H, grafo)
        file.write("\n")

        # Insere o que deve retornar de resultado no terminal no arquivo AMPL
        file.write("solve;\n")
        file.write("display ")

        for i in range(0, len(colors)- 1, 1):
            file.write(colors[i] + ',')

        file.write(colors[len(colors) - 1] + ';')
        file.close()