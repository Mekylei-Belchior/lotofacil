# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
pd.set_option('display.max_columns', None)

import logging
import logging.config
logging.basicConfig(encoding='utf-8', level=logging.INFO)


logger = logging.getLogger(__file__)
logger.info('Init')
# %%
from dados.get_resultados import read_all, download_all, check_all, processa_all


# %%
check_all()
download_all()
df = read_all()
df = processa_all(df)
df


# %%
df['ds'] = df['dezenasSorteadasOrdemSorteio'].apply(lambda x: ','.join(map(str,sorted(x))))


# %%
dezenasSorteadasOrdemSorteio = pd.DataFrame(df['dezenasSorteadasOrdemSorteio'].tolist(),index=df.index)
dezenasSorteadasOrdemSorteio.columns = [ f"B{i+1}" for i in dezenasSorteadasOrdemSorteio.columns ]
dezenasSorteadasOrdemSorteio


# %%
df.loc[:,:'dezenasSorteadasOrdemSorteio']
df.loc[:,'dezenasSorteadasOrdemSorteio':]
df = pd.concat([df.loc[:,:'dezenasSorteadasOrdemSorteio'],dezenasSorteadasOrdemSorteio,df.loc[:,'dezenasSorteadasOrdemSorteio':]],axis=1)
del df['dezenasSorteadasOrdemSorteio']
df


# %%
dezenasFaltantes = pd.DataFrame(df['dezenasFaltantes'].tolist(),index=df.index).fillna(0).astype(int)
dezenasFaltantes.columns = [ f"F{i+1}" for i in dezenasFaltantes.columns ]
dezenasFaltantes


# %%
df.loc[:,:'dezenasFaltantes']
df.loc[:,'dezenasFaltantes':]
df = pd.concat([df.loc[:,:'dezenasFaltantes'],dezenasFaltantes,df.loc[:,'dezenasFaltantes':]],axis=1)
del df['dezenasFaltantes']
df


# %%
df.loc[:,'B1':'B15']


# %%
df.loc[:,'F1':'F10']


# %%
df.reset_index().set_index(['ciclo','jogos','jogo','numero'])


# %%
df.reset_index().rename(
    columns={
        'numero':'Concurso',
        'dataApuracao':'Data Sorteio',
        'ganhou':'Ganhou',
        'falta':'Falta',
        'ciclo':'Ciclo',
        'jogos':'Jogos',
        'jogo':'Jogo'
    }).to_csv('base/base_dados.csv',index=False)


logger.info(' Finish, can you update base\\base_dados.xlsx or play python jogar.py ')
