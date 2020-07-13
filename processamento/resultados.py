from dados.dados import carregar_dados


def resultados_ordenados(base_dados):
	"""
	Estrutura os resultados em ordem crescente.

	:param base_dados: DataFrame da base de dados.
	
	return: Retorna uma lista com todos os resultados da lotofácil
	em ordem crescente.
	"""
	dados = base_dados.copy()

	num_sorteados = dados.iloc[:, 2:17]
	num_ordenados = num_sorteados.values

	for numeros in num_ordenados:
		numeros.sort()

	return num_ordenados.tolist()
