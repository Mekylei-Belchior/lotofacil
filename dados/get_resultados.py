import json
import codecs
import logging
import requests
import pandas as pd
from os.path import join, isfile
from os import makedirs, listdir, remove
from time import sleep
from shutil import rmtree
from operator import itemgetter

def clean_all():
	rmtree('resultados')
	makedirs('resultados')

def download(numero:int=0):
	if numero == 0:
		res = requests.get(f"https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/")
	else:
		res = requests.get(f"https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/{numero}")
		
	return res.json()

def download_all() -> list:
	last = download()
	files = [ join('resultados',f"{last['numero']}.json")]
	with codecs.open(files[0], 'w', encoding='utf-8') as f:
		json.dump(last, f, indent=2, ensure_ascii=False)

	for numero in range(1,last['numero']):
		filepath = join('resultados',f"{numero}.json")
		finished = False
		while not isfile(filepath) and not finished :
			try:
				logging.info(f"Requesting lotofacil nº {numero}")
				concurso = download(numero)
				assert concurso['numero']
				
				with codecs.open(filepath, 'w', encoding='utf-8') as f:
					json.dump(concurso, f, indent=2, ensure_ascii=False)

				finished = True
			except:
				logging.error(f"Requesting lotofacil nº {numero}")
				sleep(5)
				pass
		
			sleep(1)
		
		files.append(filepath)

	return files
	
def check_all():
	files = [ join('resultados',f) for f in sorted(listdir('resultados')) if '.json' in f ]
	for filepath in files:
		try:
			logging.info(f"Check lotofacil {filepath}")
			with codecs.open(filepath, 'r', encoding='utf-8') as f:
				concurso = json.load(f)
		except:
			logging.error(f"Check lotofacil {filepath}")
			remove(filepath)
			raise

def read_all():
	files = [ join('resultados',f) for f in sorted(listdir('resultados')) if '.json' in f ]
	results = [ json.load(codecs.open(f, 'r', encoding='utf-8')) for f in files ]
	list_tuples = [ itemgetter(*result.keys())(result) for result in results ]
	return pd.DataFrame(data=list_tuples, columns=results[0].keys()).set_index('numero').sort_index()

def processa_all(df):
	df = df.copy()
	df['dezenasSorteadasOrdemSorteio'] = df['dezenasSorteadasOrdemSorteio'].apply(lambda l: [int(i) for i in l])
	df['numeroDeGanhadores15acertos'] = df['listaRateioPremio'].apply(lambda x: x[0]['numeroDeGanhadores'])

	df = df[['dataApuracao','dezenasSorteadasOrdemSorteio','numeroDeGanhadores15acertos']]
	df['ganhou'] = (df['numeroDeGanhadores15acertos'] >= 1).apply(lambda x: 1 if x else 0)
	df['ciclo'] = 0
	df['jogos'] = 0
	df['jogo'] = 0
	df['falta'] = 0
	df['dezenasFaltantes'] = df['dezenasSorteadasOrdemSorteio']

	dezenas = list(range(1,26))
	dezenasFaltantes = dezenas
	ciclo = 1
	jogo = 1
	for sorteio in df.index:
		df.at[sorteio,'ciclo'] = ciclo
		df.at[sorteio,'jogo'] = jogo
		dezenasFaltantes = [ dezena for dezena in dezenasFaltantes if not dezena in df.loc[sorteio,'dezenasSorteadasOrdemSorteio'] ]
		df.at[sorteio,'falta'] = len(dezenasFaltantes)
		df.at[sorteio,'dezenasFaltantes'] = dezenasFaltantes
		jogo += 1

		if len(dezenasFaltantes) == 0:
			df.at[sorteio,'jogos'] = jogo
			ciclo += 1
			jogo = 1
			dezenasFaltantes = dezenas

	df['jogos'] = df.groupby('ciclo')['jogo'].transform('count')
	return df


