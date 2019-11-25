from collections import OrderedDict
from random import choice, choices
from dados import carregar_dados

# Carrega a base de dados
dados = carregar_dados()


def gerar_frequencia():
    """
    Gera a frequência que cada número foi sorteado na totalização dos concursos.

    :return: A frequência dos números e a quantidade de sorteios(concursos).
    """

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


def ultimo_jogos():
    """
    Encontra a quantidade de jogos realizados posteriormente ao último ciclo fechado.

    :return: A quantidade de jogos.
    """

    # O maior ciclo fechado
    maior = max(dados['Ciclo'])

    # Índice do último ciclo fechado
    ciclo = int(dados.query(f'Ciclo == {maior}')['Concurso'].index[0])

    # Quantidade de jogos realizados após o último ciclo fechado
    jogos = len(dados.iloc[ciclo + 1:])

    return jogos


def numeros_faltantes_ciclo():
    """
    Obtem o(s) número(s) faltante(s) para fechar o ciclo das dezenas.

    :return: O(s) número(s) faltante(s) sorteado(s) e o percentual de reajuste de peso.
    """

    jogos = ultimo_jogos()
    frequencia = gerar_frequencia()

    maior_peso = 0

    # Obtém o maior peso
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


def calcular_pesos():
    """
    Calcula o peso de cada dezena.

    :return: Lista com os pesos(percentual de ocorrência de cada dezena considerando o ajuste para aquelas
    que são faltantes para completar o ciclo das dezenas).
    """

    frequencia, qtde_sorteios = gerar_frequencia()
    numeros_faltantes = numeros_faltantes_ciclo()

    # Aplicado para uma ocorrência de percentual que já existe
    fator_distincao = [float('0.000' + str(n)) for n in range(100, 10000)]

    l_peso = list()

    # Ações para a relação de números faltantes que não possuem dezena(s) restante(s) para reajuste
    if len(numeros_faltantes) == 2:
        faltantes = numeros_faltantes[:]

        numeros = faltantes[0]
        ajuste = faltantes[1]

        for i in range(1, 26):
            # Verifica se a dezena está contida na relação de números faltantes
            if i in numeros:
                peso = (frequencia[i] // 2 + ajuste) / qtde_sorteios

                # Verifica se o peso gerado está contido na relação de pesos
                if peso in l_peso:
                    l_peso.append(peso + choice(fator_distincao))
                else:
                    l_peso.append(peso)

            # Executa se a dezena não estiver contida na relação de números faltantes
            else:
                peso = frequencia[i] / qtde_sorteios

                if peso in l_peso:
                    l_peso.append(peso + choice(fator_distincao))
                else:
                    l_peso.append(peso)

    # Ações para a relação de números faltantes que possuem dezena(s) restante(s) para reajuste
    else:
        faltantes = numeros_faltantes[0:2]
        restante = numeros_faltantes[2:4]

        num_faltantes = faltantes[0]
        ajuste_faltantes = faltantes[1]

        num_restante = restante[0]
        ajuste_restante = restante[1]

        for i in range(1, 26):
            if i in num_faltantes:
                peso = (frequencia[i] // 2 + ajuste_faltantes) / qtde_sorteios

                if peso in l_peso:
                    l_peso.append(peso + choice(fator_distincao))
                else:
                    l_peso.append(peso)

            elif i in num_restante:
                peso = (frequencia[i] // 2 + ajuste_restante) / qtde_sorteios

                if peso in l_peso:
                    l_peso.append(peso + choice(fator_distincao))
                else:
                    l_peso.append(peso)

            else:
                peso = frequencia[i] / qtde_sorteios

                if peso in l_peso:
                    l_peso.append(peso + choice(fator_distincao))
                else:
                    l_peso.append(peso)

    return l_peso


def calcular_numero_pesos():
    """
    Gera um dicionário contendo os números e os seus pesos.

    :return: A relação de números com os seus pesos.
    """

    peso = calcular_pesos()

    n_peso = dict()

    for i in range(1, 26):
        n_peso[i] = peso[i - 1]

    return peso, n_peso

