from sklearn.model_selection import train_test_split

from pandas import ExcelFile, read_excel


def carregar_dados(guia='Importar_Ciclo'):
    """
    Importando os dados da planilha do Excel gerando o dataframe da
    base de dados.

    :return: a base de dados.
    """

    caminho = './base/base_dados.xlsx'
    planilha = ExcelFile(caminho)
    dados = read_excel(planilha, guia)

    return dados


def preparar_dados(base_dados):
    """
    Prepara os dados para gerar o modelo.

    :param base_dados: DataFrame da base de dados.

    :return: os dados de atributos (bolas = x) e os dados
    de classificação (ganhadores = y).
    """

    # Carrega a base de dados
    dados = base_dados.copy()

    # Reajustando a columa de ganhadores para:
    # 1 - concurso com ganhadores | 0 - concurso sem ganhadores
    dados.loc[dados['Ganhou'] > 1, 'Ganhou'] = 1

    # Seleciona todas as linhas mais as colunas das dezenas sorteadas
    # e a coluna de ganhadores
    dados = dados.iloc[:, 2:18]

    # Separando atributos (bolas = x) e classe (ganhadores = y)
    atributos = dados.iloc[:, 0:15].values
    classe = dados.iloc[:, 15].values

    return atributos, classe


def dividir_dados(base_dados, tm_teste=0.1, seed=12):
    """
    Divide a base de dados em treino e teste.
    Default: 90% dos dados para treino e 10% dos dados para teste.

    :param base_dados: DataFrame da base de dados.
    :param tm_teste: define o percentual de dados para teste.
    :param seed: padroniza a randomização dos dados para replicação do modelo.
    :return: os dados de treino, teste e o total de atributos contido na base de dados.
    """

    atributos, classe = preparar_dados(base_dados)
    total_atributos = atributos.shape[1]

    # Dividindo os dados em treino e teste
    x_treino, x_teste, y_treino, y_teste = train_test_split(atributos,
                                                            classe,
                                                            test_size=tm_teste,
                                                            random_state=seed)

    return x_treino, x_teste, y_treino, y_teste, total_atributos

