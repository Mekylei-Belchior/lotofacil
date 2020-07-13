from calculos.frequencia import gerar_frequencia
from random import choice, choices


def ultimo_jogos(base_dados):
    """
    Encontra a quantidade de jogos realizados posteriormente ao último ciclo fechado.

    :param base_dados: DataFrame da base de dados.

    :return: a quantidade de jogos.
    """

    # Carrega a base de dados
    dados = base_dados.copy()

    # O maior ciclo fechado
    maior = max(dados['Ciclo'])

    # Índice do último ciclo fechado
    ciclo = int(dados.query(f'Ciclo == {maior}')['Concurso'].index[0])

    # Quantidade de jogos realizados após o último ciclo fechado
    jogos = len(dados.iloc[ciclo + 1:])

    return jogos


def numeros_faltantes_ciclo(base_dados):
    """
    Obtem o(s) número(s) faltante(s) para fechar o ciclo das dezenas.

    :param base_dados: DataFrame da base de dados.

    :return: o(s) número(s) faltante(s) sorteado(s) e o percentual de reajuste de peso.
    """

    dados = base_dados.copy()
    jogos = ultimo_jogos(dados)
    frequencia = gerar_frequencia(dados)

    maior_peso = 0

    # Obtém o maior peso (maior frequência na relação de dezenas)
    for chave, valor in frequencia[0].items():
        maior_peso = valor
        break

    # Obtém as dezenas faltantes
    relacao_numeros = list(dados.iloc[-1, 22:32].values)
    num_faltantes = [numero for numero in relacao_numeros if numero > 0]
    numeros = num_faltantes[:]

    # Quantidade de dezenas ainda não sorteadas. Utilizado a partir de jogo >= 2
    qtde_faltantes = len(numeros)

    pesos = list()
    peso = dict()
    jogo = list()

    faltantes = list()

    if jogos == 1:
        # Existem 10 dezenas que ainda não foram sorteadas para completar o ciclo

        for i in range(1, 8):
            jogo.append(i)
            peso[i] = len(dados.query(f'Jogo == 2 & Falta == {i}'))

        for k, v in peso.items():
            pesos.append(v)

        # Define o número de dezenas das que não foram sorteadas para terem seus pesos reajustados
        n_dz = choices(jogo, weights=pesos, k=1)

        for j in range(n_dz[0]):

            # Sorteia um número aleatoriamente
            numero_sorteado = choice(numeros)

            # Remove da relação de sorteio o número já sorteado
            numeros.remove(numero_sorteado)

            # Atribui o número sorteado ao vetor
            faltantes.append(numero_sorteado)

        # Demais números faltantes que não foram sorteados
        restantes = [numero for numero in num_faltantes if numero not in faltantes]

        return faltantes, maior_peso, restantes, maior_peso // 2

    elif jogos == 2:

        for i in range(0, qtde_faltantes + 1):
            jogo.append(i)
            peso[i] = len(dados.query(f'Jogo == 3 & Falta == {i}'))

        for k, v in peso.items():
            pesos.append(v)

        n_dz = choices(jogo, weights=pesos, k=1)

        for j in range(n_dz[0]):

            # Sorteia um número aleatoriamente
            numero_sorteado = choice(numeros)

            # Remove da relação de sorteio o número já sorteado
            numeros.remove(numero_sorteado)

            # Atribui o número sorteado ao vetor
            faltantes.append(numero_sorteado)

        if qtde_faltantes == n_dz[0] or n_dz[0] == 0:
            # Considera que todos os números faltantes serão sorteados no próximo sorteio
            return num_faltantes, maior_peso

        elif 1 < qtde_faltantes != n_dz[0] and n_dz[0] > 0:
            # Demais números faltantes que não foram sorteados
            restantes = [numero for numero in num_faltantes if numero not in faltantes]

            return faltantes, maior_peso, restantes, maior_peso // 2

    elif jogos == 3:

        for i in range(0, qtde_faltantes + 1):
            jogo.append(i)
            peso[i] = len(dados.query(f'Jogo == 4 & Falta == {i}'))

        for k, v in peso.items():
            pesos.append(v)

        n_dz = choices(jogo, weights=pesos, k=1)

        for j in range(n_dz[0]):

            # Sorteia um número aleatoriamente
            numero_sorteado = choice(numeros)

            # Remove da relação de sorteio o número já sorteado
            numeros.remove(numero_sorteado)

            # Atribui o número sorteado ao vetor
            faltantes.append(numero_sorteado)

        if qtde_faltantes == n_dz[0] or n_dz[0] == 0:
            # Considera que todos os números faltantes serão sorteados no próximo sorteio
            return num_faltantes, maior_peso

        elif 1 < qtde_faltantes != n_dz[0] and n_dz[0] > 0:
            # Demais números faltantes que não foram sorteados
            restantes = [numero for numero in num_faltantes if numero not in faltantes]

            return faltantes, maior_peso, restantes, maior_peso // 2

    elif jogos == 4:

        for i in range(0, qtde_faltantes + 1):
            jogo.append(i)
            peso[i] = len(dados.query(f'Jogo == 5 & Falta == {i}'))

        for k, v in peso.items():
            pesos.append(v)

        n_dz = choices(jogo, weights=pesos, k=1)

        for j in range(n_dz[0]):

            # Sorteia um número aleatoriamente
            numero_sorteado = choice(numeros)

            # Remove da relação de sorteio o número já sorteado
            numeros.remove(numero_sorteado)

            # Atribui o número sorteado ao vetor
            faltantes.append(numero_sorteado)

        if qtde_faltantes == n_dz[0] or n_dz[0] == 0:
            # Considera que todos os números faltantes serão sorteados no próximo sorteio
            return num_faltantes, maior_peso

        elif 1 < qtde_faltantes != n_dz[0] and n_dz[0] > 0:
            # Demais números faltantes que não foram sorteados
            restantes = [numero for numero in num_faltantes if numero not in faltantes]

            return faltantes, maior_peso, restantes, maior_peso // 2

    # Para jogos igual ou maior que 5, retorna a dezena que ainda não foi sorteada
    else:
        return num_faltantes, maior_peso

