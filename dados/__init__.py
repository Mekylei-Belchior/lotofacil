import pandas as pd


def carregar():
    """
    Importando os dados da planilha do Excel gerando o dataframe da base de dados.

    :return: A base de dados
    """

    caminho = 'base_dados.xlsx'
    planilha = pd.ExcelFile(caminho)
    dados = pd.read_excel(planilha, 'Importar')

    return dados

