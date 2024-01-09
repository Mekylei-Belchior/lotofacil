import pandas as pd
import ssl

def xls_resultados(url):
    """
    Obtém os dados de todos os sorteios da lotofácil.
    
    :param url: Endereço para obter o arquivo XLS
    com os dados dos sorteios da lotofácil
    
    :returns: DataFrame com os dados do arquivo XLS

    """
    ssl._create_default_https_context = ssl._create_unverified_context
    dados = pd.read_excel(url)
    return dados

# URL do arquivo XLS
URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotof%C3%A1cil"

# Obtém os dados do arquivo XLS
base = xls_resultados(URL)

# Remove dados duplicados
base = base.drop_duplicates('Concurso')

# Renomeia as colunas do DataFrame
colunas = {'Bola1': 'B1', 'Bola2': 'B2', 'Bola3': 'B3', 'Bola4': 'B4', 'Bola5': 'B5',
           'Bola6': 'B6', 'Bola7': 'B7', 'Bola8': 'B8', 'Bola9': 'B9', 'Bola10': 'B10',
           'Bola11': 'B11', 'Bola12': 'B12', 'Bola13': 'B13', 'Bola14': 'B14', 'Bola15': 'B15',
           'Ganhadores_15_Números': 'Ganhou'}

base.rename(columns=colunas, inplace=True)

# Exporta os dados em arquivo CSV
base.to_csv('./base/resultados.csv', sep=';', encoding='utf8', index=False)


if __name__ == '__main__':

	# Informações
	concurso = base['Concurso'].max()
	data = str(base[base['Concurso'] == concurso]['Data Sorteio'])[8:18]

	print(f'\n\033[1;32mTODOS OS RESULTADOS DOS CONCURSOS DA LOTOFÁCIL FORAM BAIXADOS COM SUCESSO!\033[m')
	print(f'\n\n\033[1;36mÚltimo sorteio:\033[m {data}\n\033[1;36mConcurso:\033[m {concurso}')

	print(f'\n\n\033[1;35mArquivo salvo em:\033[m \033[1;33m./base/resultados.csv\033[m')
