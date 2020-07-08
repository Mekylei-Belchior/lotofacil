from processamento.possibilidades import obter_possibilidades
from processamento.resultados import resultados_ordenados
from processamento.reajustar_dados import obter_indices

from pandas import read_csv


ARQUIVO = './base/resultados.csv'


def dados_indice(atualizar_base_resultados=False):
	"""
	Cria um DataFrame com algumas informações dos concursos da Lotofácil.

	:param atualizar_base_resultados: True atualiza a base, do contrário, não.
	(default: {False})

	Campos do DataFrame:

	1 - Concursos
	2 - Índice dos concurso na lista de concursos possíveis
	3 - Data do sorteio
	4 - Quantidade de vencedores (15 dezenas) no concurso
	
	return: DataFrame com os dados
	"""

	if atualizar_base_resultados:
		# Atualiza o arquivo com todos os resultados dos sorteios já realizados
		from dados import scrapping_resultados	
	
	resultado_concurso = read_csv(ARQUIVO,
								  sep=';',
								  encoding='utf-8',
								  parse_dates=['Data Sorteio'])

	num_sorteados = resultado_concurso.iloc[:, 2:17]
	num_ordenados = num_sorteados.values

	for numeros in num_ordenados:
		numeros.sort()

	resultados = num_ordenados.tolist()
	possibilidades = obter_possibilidades()
	indices = obter_indices(possibilidades, resultados)

	dados = resultado_concurso[['Concurso', 'Data Sorteio', 'Ganhou']]
	dados.insert(1, 'Indice', indices)

	return dados 
