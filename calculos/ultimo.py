# -*- coding: utf-8 -*-


from dados.dados import carregar_dados


def ultimo_jogos():
    """
    Encontra a quantidade de jogos realizados posteriormente ao último ciclo fechado.

    :return: a quantidade de jogos.
    """

    # Carrega a base de dados
    dados = carregar_dados()

    # O maior ciclo fechado
    maior = max(dados['Ciclo'])

    # Índice do último ciclo fechado
    ciclo = int(dados.query(f'Ciclo == {maior}')['Concurso'].index[0])

    # Quantidade de jogos realizados após o último ciclo fechado
    jogos = len(dados.iloc[ciclo + 1:])

    return jogos

