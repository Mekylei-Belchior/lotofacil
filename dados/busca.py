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
