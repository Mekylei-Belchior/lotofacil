from itertools import combinations
from csv import writer
from os import path


# Cabeçalho do arquivo
CABECALHO = ['seq', 'n1', 'n2', 'n3', 'n4', 'n5',
			 'n6', 'n7', 'n8', 'n9', 'n10', 'n11',
			 'n12', 'n13', 'n14', 'n15']

# Lista das 25 dezenas da Lotofácil
DEZENAS = [i for i in range(1, 26)]

# Diretório aonde será salvo o arquivo
DIR = './combinacoes/combinacoes.csv'


def criar_combinacoes_csv(dr=DIR, cb=CABECALHO, dz=DEZENAS, tm=15):
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


if __name__ == '__main__':
	criar_combinacoes_csv()
