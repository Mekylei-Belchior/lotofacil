from pandas import read_csv


ARQUIVO = './combinacoes/combinacoes.csv'
SEP = ';'
ENCODING = 'utf-8'


def obter_possibilidades(arq=ARQUIVO, sep=SEP, encoding=ENCODING):
	"""
	Cria uma lista com todas as combinações possíveis da lotofácil
		
	:param arq: Arquivo CSV com as combinações
	:param sep: Separador
	:param encoding: Codificação do arquivo
	
	:return: Uma lista com todas as combinações 
	"""

	df = read_csv(arq, sep=sep, encoding=encoding)
	
	df.drop(columns=['seq'], inplace=True)
	possibilidades = df.values

	return possibilidades.tolist()
