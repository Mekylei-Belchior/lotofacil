# -*- coding: utf-8 -*-

from collections import OrderedDict
from dados.dados import carregar_dados


def gerar_frequencia():
    """
    Gera a frequência que cada número foi sorteado na totalização dos concursos.

    :return: a frequência dos números e a quantidade de sorteios(concursos).
    """
    # Carrega a base de dados
    dados = carregar_dados()

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

