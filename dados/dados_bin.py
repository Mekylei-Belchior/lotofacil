# -*- coding: utf-8 -*-


from dados.dados import carregar_dados
from itertools import product
import numpy as np

from sklearn.model_selection import train_test_split


def estratificar_dados():
    """
    Carrega os dados da base de dados e gera os atributos e as classes.

    :return: uma lista de atributos e uma lista de classes.
    """

    dados = carregar_dados('Importar_Bin')
    dados = dados.iloc[:, 2:32]

    # Obtém as dezenas em grupos de atributos de 5 elementos
    atributos1 = dados.iloc[:, 0:5].values     # 01 - 05
    atributos2 = dados.iloc[:, 5:10].values    # 06 - 10
    atributos3 = dados.iloc[:, 10:15].values   # 11 - 15
    atributos4 = dados.iloc[:, 15:20].values   # 16 - 20
    atributos5 = dados.iloc[:, 20:25].values   # 21 - 25

    # Armazena os atributos no vetor
    atributos = [atributos1, atributos2, atributos3, atributos4, atributos5]

    # Obtém as colunas dos grupos de classes. Converte os valores para string
    # e preenche os dígitos vazios à esquerda com zeros
    c1 = dados.iloc[:, 25].apply(lambda x: tuple([int(y) for y in str(x).zfill(5)])).values
    c2 = dados.iloc[:, 26].apply(lambda x: tuple([int(y) for y in str(x).zfill(5)])).values
    c3 = dados.iloc[:, 27].apply(lambda x: tuple([int(y) for y in str(x).zfill(5)])).values
    c4 = dados.iloc[:, 28].apply(lambda x: tuple([int(y) for y in str(x).zfill(5)])).values
    c5 = dados.iloc[:, 29].apply(lambda x: tuple([int(y) for y in str(x).zfill(5)])).values

    # Reformulando os dados para gerar as classes
    # 

    # Gera a lista das 32 classes possíveis
    lista_classes = gerar_classes()

    # Converte a sequência de dígitos das 5 colunas em classes
    classe1 = converter_digitos_classe(c1, lista_classes)
    classe2 = converter_digitos_classe(c2, lista_classes)
    classe3 = converter_digitos_classe(c3, lista_classes)
    classe4 = converter_digitos_classe(c4, lista_classes)
    classe5 = converter_digitos_classe(c5, lista_classes)

    # Armazenas as classes no vetor
    classes = [classe1, classe2, classe3, classe4, classe5]

    return atributos, classes


def converter_digitos_classe(coluna, lista_classes):
    """
    Converte a sequência de dígitos em um dígito de referência de classe (0 à 31).
    Em seguida, converte para uma classe dummy que será utilizada no modelo.

    :param coluna: sequência de 0 e 1 que representa uma referência de classe.
    :param lista_classes: lista de classes.
    :return: a classe dummy.
    """

    n_coluna = list()
    array_coluna = list()

    n_coluna.append([col for col in coluna])

    indices = n_coluna[0][:]
    n_coluna.clear()

    for i in range(len(indices)):

        indice = tuple(indices[i])
        valor = lista_classes.index(indice)

        n_coluna.insert(i, valor)

    for valor in n_coluna:
        array_coluna.append(list([1 if valor == i else 0 for i in range(32)]))

    classe = np.array(array_coluna)

    return classe


def gerar_classes(caracteres=(0, 1), elementos=5):
    """
    Gera classes com as combinações possíveis de saída para cada grupo de 5 dezenas.

    Exemplo:

    dezenas do primeiro grupo: (1, 2, 3, 4, 5)
    dezenas sorteadas do primeiro grupo: (1, 4, 5)
    Classe: (1, 0, 0, 1, 1)

    :param caracteres: [0, 1] - 0 : dezena não sorteada | 1 : dezena sorteada.
    :param elementos: quantidade de elementos que a classe possui.
    :return: a lista de classes possíveis.
    """

    classes = []

    combinacoes = product(caracteres, repeat=elementos)

    for combinacao in combinacoes:
        classes.append(combinacao)

    return classes


def dados_treino_teste(tam_teste=0.1, seed=12):
    """
    Divide a base de dados em treino e teste. Default: 90% dos dados para treino e 10% dos dados para teste.

    :param tam_teste: define o percentual de dados para teste.
    :param seed: padroniza a randomização dos dados para replicação do modelo.
    :return: os grupos de dados de treino e teste.
    """

    atributos, classes = estratificar_dados()

    atributos_grupo1 = atributos[0]
    atributos_grupo2 = atributos[1]
    atributos_grupo3 = atributos[2]
    atributos_grupo4 = atributos[3]
    atributos_grupo5 = atributos[4]

    classe_grupo1 = classes[0]
    classe_grupo2 = classes[1]
    classe_grupo3 = classes[2]
    classe_grupo4 = classes[3]
    classe_grupo5 = classes[4]

    x_treino1, x_teste1, y_treino1, y_teste1 = train_test_split(atributos_grupo5, classe_grupo5,
                                                                test_size=tam_teste, random_state=seed)

    x_treino2, x_teste2, y_treino2, y_teste2 = train_test_split(atributos_grupo4, classe_grupo4,
                                                                test_size=tam_teste, random_state=seed)

    x_treino3, x_teste3, y_treino3, y_teste3 = train_test_split(atributos_grupo3, classe_grupo3,
                                                                test_size=tam_teste, random_state=seed)

    x_treino4, x_teste4, y_treino4, y_teste4 = train_test_split(atributos_grupo2, classe_grupo2,
                                                                test_size=tam_teste, random_state=seed)

    x_treino5, x_teste5, y_treino5, y_teste5 = train_test_split(atributos_grupo1, classe_grupo1,
                                                                test_size=tam_teste, random_state=seed)

    grupos_treino_teste = [

        (x_treino1, x_teste1, y_treino1, y_teste1),
        (x_treino2, x_teste2, y_treino2, y_teste2),
        (x_treino3, x_teste3, y_treino3, y_teste3),
        (x_treino4, x_teste4, y_treino4, y_teste4),
        (x_treino5, x_teste5, y_treino5, y_teste5),
    ]

    return grupos_treino_teste


def visualizar_layout():
    """
    Imprime o layout das dezenas.
    :return: impressão
    """

    dados = estratificar_dados()
    linhas = dados[0]

    for linha in linhas:
        for dezena in linha:
            print(f'{str(dezena[1:].zfill(2)):^5}', end='')
        print()


def dimensoes(matriz):
    """
    Imprime as dimensões de uma matriz.

    :param matriz: estrutura a ser analisada.
    :return: impressão das dimensões da matriz.
    """

    tam_matriz = (len(matriz), len(matriz[0]))
    print(f'{tam_matriz[0]} X {tam_matriz[1]}')

