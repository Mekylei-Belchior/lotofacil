from random import choices


def sortear_numeros(n_pesos: list, n_numero_peso: dict):
    """
    Sorteia as quinze dezenas do jogo.

    :param n_pesos: lista de peso das dezenas.
    :param n_numero_peso: dicionário com as dezenas e seus respectivos pesos.
    :return: as dezenas sorteadas.
    """

    # Dezenas do jogo (1 à 25)
    dz = [d for d in range(1, 26)]

    dezenas = dz[:]
    pesos = n_pesos[:]
    numero_peso = n_numero_peso.copy()

    sorteados = list()

    # Sorteando as 15 dezenas do jogo
    while len(sorteados) != 15:
        # Sorteia um número aleatoriamente de acordo com o seu peso
        numero_sorteado = choices(dezenas, weights=pesos, k=1)

        # Remove da relação de sorteio os números já sorteados
        dezenas.remove(numero_sorteado[-1])
        p = numero_peso.pop(numero_sorteado[-1])
        pesos.remove(p)

        # Atribui o número sorteado ao vetor
        sorteados.append(numero_sorteado)

    return sorteados

