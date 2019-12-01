import pandas as pd

from sklearn.model_selection import train_test_split


def carregar_dados():
    """
    Importando os dados da planilha do Excel gerando o dataframe da base de dados.

    :return: a base de dados.
    """

    caminho = 'base_dados.xlsx'
    planilha = pd.ExcelFile(caminho)
    dados = pd.read_excel(planilha, 'Importar_Ciclo')

    return dados


def preparar_dados():
    """
    Prepara os dados para gerar o modelo.

    :return: os dados de atributos (bolas = x) e os dados de classificação (ganhadores = y).
    """

    # Carrega a base de dados
    dados = carregar_dados()

    # Reajustando a columa de ganhadores para: 1 - concurso com ganhadores | 0 - concurso sem ganhadores
    dados.loc[dados['Ganhou'] > 1, 'Ganhou'] = 1

    # Seleciona todas as linhas mais as colunas das dezenas sorteadas e a coluna de ganhadores
    dados = dados.iloc[:, 2:18]

    # Separando atributos (bolas = x) e classe (ganhadores = y)
    atributos = dados.iloc[:, 0:15].values
    classe = dados.iloc[:, 15].values

    return atributos, classe


def dividir_dados(tam_teste=0.2):
    """
    Divide a base de dados em treino e teste. Default: 80% dos dados para treino e 20% dos dados para teste.

    :param tam_teste: define o percentual de dados para teste.
    :return: os dados de treino, teste e o total de atributos contido na base de dados.
    """

    atributos, classe = preparar_dados()
    total_atributos = atributos.shape[1]

    # Dividindo os dados em treino e teste
    x_treino, x_teste, y_treino, y_teste = train_test_split(atributos, classe, test_size=tam_teste, random_state=12)

    return x_treino, x_teste, y_treino, y_teste, total_atributos

