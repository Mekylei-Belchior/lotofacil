from random import choices


DEZENAS = [d for d in range(1, 26)]


def sortear_numeros(n_pesos: list, n_numero_peso: dict, dz=DEZENAS, n_dz=15):
    """
    Sorteia as dezenas do jogo.
 
    :param n_pesos: lista de peso das dezenas.
    :param n_numero_peso: dicionário com as dezenas e seus respectivos pesos.
    :param dz: Lista com a relação de dezenas default:{DEZENAS}.
    :param n_dz: Quantidade de dezenas a serem sorteadas default:{15}.
    
    :return: as dezenas sorteadas.
    """

    dezenas = dz[:]
    pesos = n_pesos[:]
    numero_peso = n_numero_peso.copy()

    sorteados = list()

    # Sorteando as dezenas do jogo
    while len(sorteados) != n_dz:
        # Sorteia um número aleatoriamente ponderando o seu peso
        numero_sorteado = choices(dezenas, weights=pesos, k=1)

        # Remove da relação de sorteio os números já sorteados
        dezenas.remove(numero_sorteado[-1])
        p = numero_peso.pop(numero_sorteado[-1])
        pesos.remove(p)

        # Atribui o número sorteado ao vetor
        sorteados.append(numero_sorteado)

    return sorteados

