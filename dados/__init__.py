import numpy as np
import pandas as pd

from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split


def carregar_dados():
    """
    Importando os dados da planilha do Excel gerando o dataframe da base de dados.

    :return: a base de dados.
    """

    caminho = 'base_dados.xlsx'
    planilha = pd.ExcelFile(caminho)
    dados = pd.read_excel(planilha, 'Importar')

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


def dividir_dados(teste=0.3):
    """
    Divide a base de dados em treino e teste. Default: 70% dos dados para treino e 30% dos dados para teste.

    :param teste: define o percentual de dados para teste.
    :return: os dados de treino, teste e o total de atributos contido na base de dados.
    """

    atributos, classe = preparar_dados()
    total_atributos = atributos.shape[1]

    # Geração da seed para replicação do modelo
    seed = 12
    np.random.seed(seed)

    # Dividindo os dados em treino e teste
    x_treino, x_teste, y_treino, y_teste = train_test_split(
                                                            atributos,
                                                            classe,
                                                            test_size=teste,
                                                            random_state=seed
                                                            )

    return x_treino, x_teste, y_treino, y_teste, total_atributos


def criar_modelo(entrada=2, segunda_camada=8, saida=1, periodo=100, reajuste=10):
    """
    Cria o modelo sequêncial com três camadas ocultas.

    :param entrada: camada de entrada utilizando a função retificadora (relu). Default: 2 neurônios.
    :param segunda_camada: segunda camada utilizando a função retificadora(relu). Default: 8 neurônios.
    :param saida: camada de saída utilizando a função de ativação (sigmoid). Default: 1 neurônio.
    :param periodo: quantidade de iterações para ajuste do modelo.
    :param reajuste: ajuste do número de instâncias.
    :return: o modelo gerado e a sua acurracidade.
    """

    x_treino, x_teste, y_treino, y_teste, atributos = dividir_dados()

    # Criando o modelo
    modelo = Sequential()
    modelo.add(Dense(entrada, input_dim=atributos, activation='relu'))
    modelo.add(Dense(segunda_camada, activation='relu'))
    modelo.add(Dense(saida, activation='sigmoid'))

    # Compilando o modelo
    modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Treinando o modelo
    modelo.fit(x_treino, y_treino, epochs=periodo, batch_size=reajuste)

    # Avaliação do modelo
    pontuacao = modelo.evaluate(x_teste, y_teste)

    return modelo, pontuacao

