from pandas import read_csv


URL = './base/resultados.csv'
DEZENAS = [i for i in range(1, 26)]


def criar_nao_sorteados(dz=DEZENAS,
						base_url=URL,
						base_lista=None,
						atualizar_base_resultados=False):
	"""
	Cria uma lista com todos as dezenas não sorteadas em cada concurso.

	:param dz: Lista com as dezenas da lotofácil (default: {DEZENAS})
	:param base_url: CSV com todos os resultados da lotofácil (default: {URL})
	:param base_lista: Recebe uma lista com os resultados (default: {None}) 
	:param atualizar_resultado: True atualiza a base, do contrário, não.
	(default: {False})
	
	return: Lista com as dezenas não sorteadas de cada concurso.	
	"""

	if not base_lista == None and type(base_lista) is list:
		nao_sorteados = list()

		for resultado in base_lista:
			resultado.sort()
			diferenca = set(dz).difference(resultado)
			nao_sorteados.append(list(diferenca))

		return nao_sorteados

	if atualizar_base_resultados:
		# Atualiza o CSV com todos os resultados dos sorteios já realizados
		from dados import scrapping_resultados

	dados = read_csv(base_url, sep=';', encoding='utf-8')
	resultados = dados.iloc[:, 2:17].values

	nao_sorteados = list()

	for resultado in resultados:
		resultado.sort()
		diferenca = set(dz).difference(resultado)
		nao_sorteados.append(list(diferenca))

	return nao_sorteados
