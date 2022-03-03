import json
import codecs
import logging
import requests
import pandas as pd
from os.path import join, isfile
from os import makedirs, listdir
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
	
def read_all():
	files = [ join('resultados',f) for f in sorted(listdir('resultados')) ]
	results = [ json.load(codecs.open(f, 'r', encoding='utf-8')) for f in files ]
	list_tuples = [ itemgetter(*result.keys())(result) for result in results ]
	return pd.DataFrame(data=list_tuples, columns=results[0].keys()).set_index('numero').sort_index()


