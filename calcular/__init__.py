from collections import OrderedDict
import pandas as pd


def gerar_frequencia():

    caminho = 'base_dados.xlsx'
    planilha = pd.ExcelFile(caminho)
    dados = pd.read_excel(planilha, 'Importar')

    sorteios = dados.iloc[:, 2:17].values
    qtde_sorteios = len(sorteios)

    lista_frequencia = list()
    valor = 0

    for i in range(1, 26):
        for sorteio in sorteios:
            for numero in sorteio:
                if numero == i:
                    valor += 1

        lista_frequencia.append(valor)
        valor = 0

    # Cria os índices para a lista de frequência
    lista_frequencia = [[indice + 1, vlr] for indice, vlr in enumerate(lista_frequencia)]

    # Ordena a lista pela maior frequência
    lista_frequencia = sorted([[valor[1], valor] for valor in lista_frequencia], reverse=True)

    # Cria o dicionário das frequências
    # noinspection PyTypeChecker
    frequencia = dict(OrderedDict(frequencia[1] for frequencia in lista_frequencia))

    return frequencia, qtde_sorteios


def calcular_pesos():

    frequencia, qtde_sorteios = gerar_frequencia()

    l_peso = list()

    for i in range(1, 26):
        l_peso.append(frequencia[i] / qtde_sorteios)

    return l_peso


def calcular_numero_pesos():

    frequencia, qtde_sorteios = gerar_frequencia()

    n_peso = dict()

    for i in range(1, 26):
        n_peso[i] = frequencia[i] / qtde_sorteios

    return n_peso

