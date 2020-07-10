from itertools import combinations
from csv import writer
from os import path


# Cabeçalho do arquivo
CABECALHO = ['seq', 'n1', 'n2', 'n3', 'n4', 'n5',
			 'n6', 'n7', 'n8', 'n9', 'n10', 'n11',
			 'n12', 'n13', 'n14', 'n15']

# Lista com as 25 dezenas da Lotofácil
DEZENAS = [i for i in range(1, 26)]

# Diretório
DIR = './combinacoes/combinacoes.csv'

# Quantidade de dezenas
TM = 15


def criar_combinacoes_csv(dr=DIR, cb=CABECALHO, dz=DEZENAS, tm=TM):
	"""
	Cria um arquivo CSV com todos as combinações possíveis da Lotofácil. 
	
	:param dr: Diretório aonde será salvo o arquivo (default: {DIR})
	:param cb: Cabeçalho do arquivo CSV (default: {CABECALHO})
	:param dz: Dezenas da Lotofácil (default: {DEZENAS})
	:param tm: Quantidade de dezenas para a combinação (default: {15})
	"""

	if not path.exists(dr):
		with open(dr, 'w', newline='') as arquivo:
			add = writer(arquivo, delimiter=';')

			add.writerow(cb)
			indice = 1

			for combinacao in combinations(dz, tm):
				linha = list(combinacao)
				linha.insert(0, indice)
				
				add.writerow(linha)

				indice += 1



def criar_combinacoes(dz=DEZENAS, tm=TM):
	"""
	Cria uma lista com todos as combinações possíveis da Lotofácil de acordo
	com a quantidade de dezenas para a combinação. 
	
	:param dz: Dezenas da Lotofácil (default: {DEZENAS})
	:param tm: Quantidade de dezenas para a combinação (default: {15})
	"""

	combinacoes = list()

	for combinacao in combinations(dz, tm):
		combinacoes.append(list(combinacao))

	return combinacoes


if __name__ == '__main__':	
	criar_combinacoes_csv()
