from calculos.frequencia import gerar_frequencia
from calculos.faltantes import numeros_faltantes_ciclo

from random import choice


def calcular_pesos(base_dados):
    """
    Calcula o peso de cada dezena.

    :param base_dados: DataFrame da base de dados.

    :return: lista com os pesos(percentual de ocorrência de cada dezena considerando o ajuste para aquelas
    que são faltantes para completar o ciclo das dezenas).
    """

    frequencia, qtde_sorteios = gerar_frequencia(base_dados)
    numeros_faltantes = numeros_faltantes_ciclo(base_dados)

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


def calcular_numero_pesos(base_dados):
    """
    Gera um dicionário contendo os números e os seus pesos.

    :param base_dados: DataFrame da base de dados.

    :return: a relação de números com os seus pesos.
    """

    peso = calcular_pesos(base_dados)

    n_peso = dict()

    for i in range(1, 26):
        n_peso[i] = peso[i - 1]

    return peso, n_peso

