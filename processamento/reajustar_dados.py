from dados.busca import buscar


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
