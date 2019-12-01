from calculos.pesos import calcular_numero_pesos
from sorteios.sortear import sortear_numeros

# Calcula os pesos das dezenas
peso, numero_pesos = calcular_numero_pesos()

cont = 0

while True:

    # Sorteia as 15 dezenas
    sorteados = sortear_numeros(peso, numero_pesos)
    jogo = [[1], [2], [3], [4], [6], [8], [9], [10], [13], [14], [19], [22], [23], [24], [25]]

    # Conta a quantidade de loops realizados
    cont += 1

    # Interrompe o loop se a sequência de números sorteados forem iguais a sequência de números do sorteio da lotofácil
    if sorteados == jogo:

        # Formata os números para impressão
        sorteados = sorted([str(numero[0]).zfill(2) for numero in sorteados])
        jogo = [str(numero[0]).zfill(2) for numero in jogo]

        # Imprime os números
        print(f'({str(cont).zfill(13)}) ', end='')
        print('Sorteados: [ ', *sorteados, end=' ] ')
        print('Jogo Lotofácil: [ ', *jogo, end=' ]')
        print('')

        break

    # Formata os números para impressão
    sorteados = sorted([str(numero[0]).zfill(2) for numero in sorteados])
    jogo = [str(numero[0]).zfill(2) for numero in jogo]

    # Imprime os números
    print(f'\033[1;36m({str(cont).zfill(13)}) \033[m', end='')
    print('Sorteados: \033[1;37m[ ', *sorteados, end=' ]\033[m ')
    print('Jogo Lotofácil: \033[1;31m[ ', *jogo, end=' ]\033[m')
    print('')
