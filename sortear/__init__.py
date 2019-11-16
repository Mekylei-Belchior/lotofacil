from random import choices


def sortear_numeros(n_pesos: list, n_numero_peso: dict):

    dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    dezenas = dz[:]
    pesos = n_pesos[:]
    numero_peso = n_numero_peso.copy()

    sorteados = []

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
