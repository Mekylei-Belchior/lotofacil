from dados.dados import carregar_dados


def resultados_ordenados():
	"""
	Estrutura os resultados em ordem crescente.
	
	return: Retorna uma lista com todos os resultados da lotofácil
	em ordem crescente.
	"""
	dados = carregar_dados()

	num_sorteados = dados.iloc[:, 2:17]
	num_ordenados = num_sorteados.values

	for numeros in num_ordenados:
		numeros.sort()

	return num_ordenados.tolist()
