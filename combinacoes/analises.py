def buscar(lista, elem_ini, elem_fin, valor_busca):
	"""
	Busca binária em uma lista.
	
	
	:param lista: lista que contém os elementos 
	:param elem_ini: Elemento inicial da lista ou sub-lista
	:param elem_fin: Elemento final da lista ou sub-lista
	:param valor_busca: Valor a ser encontrado
	
	return: O elemento buscado, caso ele esteja na lista.
	"""
	if elem_ini <= elem_fin:
		# Elemento do meio da lista
		meio = (elem_ini + elem_fin) // 2

		if valor_busca > lista[meio]:
			return buscar(lista, meio + 1, elem_fin, valor_busca)
		elif valor_busca < lista[meio]:
			return buscar(lista, elem_ini, meio -1, valor_busca)
		else:
			# Encontrou o elemento da busca
			return meio


def verificar(jogo, possibilidades, resultado_concursos):
	"""
	Verifica se o jogo existe na lista de resultados possíveis e
	se ele ainda não foi sorteado.
	
	:param jogo: Jogo criado
	:param possibilidades: Combinações possíveis da Lotofácil
	:param resultado_concursos: Resultado de todos os concursos
	
	return: Retorna False - (Jogo não aceito) e True - (Jogo aceito)	
	"""

	if jogo in possibilidades and jogo not in resultado_concursos:
		return True
	else:
		return False


def remover_resultado_concursos(possibilidades, resultado_concursos):
	"""
	Remove da lista de possibilidades os resultados já sorteados.
	
	:param possibilidades: Combinações possíveis da Lotofácil
	:param resultado_concursos: Resultado de todos os concursos
	
	return:	A lista de possibilidades sem os resultados já sorteados.
	"""
	from pandas import Series

	elem_ini = 0
	elem_fin = len(possibilidades) - 1
	
	indices = [buscar(
                      possibilidades,
                      elem_ini,
                      elem_fin,
                      valor_busca
	                 ) for valor_busca in resultado_concursos]
	
	s_possibilidades = Series(possibilidades)
	removidos = s_possibilidades.drop(indices)

	lista_possibilidades_atualizada = removidos.values 
	
	return lista_possibilidades_atualizada.tolist()


def obter_indices(possibilidades, resultado_concursos):
	"""
	Obtém os índices da lista de possibilidades dos resultados já sorteados.
	
	:param possibilidades: Combinações possíveis da Lotofácil
	:param resultado_concursos: Resultado de todos os concursos
	
	return:	Uma lista com os índice dos resultados já sorteados nos concursos.
	"""
	elem_ini = 0
	elem_fin = len(possibilidades) - 1
	
	indices = [buscar(
                      possibilidades,
                      elem_ini,
                      elem_fin,
                      valor_busca
                     ) for valor_busca in resultado_concursos]

	return indices
