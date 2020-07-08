def verificar(jogo: list, possibilidades: list, resultado_concursos: list):
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
