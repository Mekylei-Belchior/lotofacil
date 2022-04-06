import json
import codecs
import logging
from pathlib import Path
import requests
import pandas as pd
from os.path import join, isfile
from os import makedirs, listdir, remove
from time import sleep
from shutil import rmtree
from operator import itemgetter

logger = logging.getLogger(__file__)

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
	files = [ join('dados','resultados',f"{last['numero']}.json")]
	with codecs.open(files[0], 'w', encoding='utf-8') as f:
		json.dump(last, f, indent=2, ensure_ascii=False)

	for numero in range(1,last['numero']):
		filepath = join('dados','resultados',f"{numero}.json")
		finished = False
		while not isfile(filepath) and not finished :
			try:
				logger.info(f"Requesting lotofacil nº {numero}")
				concurso = download(numero)
				assert concurso['numero']
				
				with codecs.open(filepath, 'w', encoding='utf-8') as f:
					json.dump(concurso, f, indent=2, ensure_ascii=False)

				finished = True
			except:
				logger.error(f"Requesting lotofacil nº {numero}")
				sleep(5)
				pass
		
			sleep(1)
		
		files.append(filepath)

	return files
	
def check_all():
	files = [ join('dados','resultados',filepath) for filepath in sorted(filter(lambda f: '.json' in str(f),map(Path,listdir(join('dados','resultados')))), key=lambda f: int(f.stem))]
	for filepath in files:
		try:
			logger.info(f"Check lotofacil {filepath}")
			with codecs.open(filepath, 'r', encoding='utf-8') as f:
				concurso = json.load(f)
		except:
			logger.error(f"Check lotofacil {filepath}")
			remove(filepath)
			raise

def read_all():
	files = [ join('dados','resultados',f) for f in sorted(listdir(join('dados','resultados'))) if '.json' in f ]
	results = [ json.load(codecs.open(f, 'r', encoding='utf-8')) for f in files ]
	list_tuples = [ itemgetter(*result.keys())(result) for result in results ]
	return pd.DataFrame(data=list_tuples, columns=results[0].keys()).set_index('numero').sort_index()

def processa_all(df):
	df = df.copy()
	df['dezenasSorteadasOrdemSorteio'] = df['dezenasSorteadasOrdemSorteio'].apply(lambda l: [int(i) for i in l])
	df['ganhou'] = df['listaRateioPremio'].apply(lambda x: x[0]['numeroDeGanhadores'])

	df = df[['dataApuracao','dezenasSorteadasOrdemSorteio','ganhou']]
	df[['ciclo','jogos','jogo','falta']] = 0
	df['dezenasFaltantes'] = None

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


