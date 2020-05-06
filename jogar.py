from calculos.pesos import calcular_numero_pesos
from sorteios.sortear import sortear_numeros
from modelos.modelo import criar_modelo

import pandas as pd


# Inicialização das variáveis
sorteados = list()
probabilidade = 0.00
procurando = 0
predicao_alvo = 0.00

# probabilidade desejada
prob_alvo = 100.0

# Obtém os pesos de cada dezena e um dicionários com as dezenas e seus pesos
peso, numero_pesos = calcular_numero_pesos()

# Obtém o modelo e sua acuracidade
modelo, pontuacao = criar_modelo()

# Replica até que a probabilidade atual seja igual à probabilidade desejada
while probabilidade < prob_alvo:

    # Atribui a sequência dos números sorteados
    sorteados = sortear_numeros(peso, numero_pesos)

    # Cria o dataframe com os números sorteados para realizar a predição
    y_alvo = pd.DataFrame(sorteados)
    y_alvo = y_alvo.iloc[:, 0].values
    y_alvo = y_alvo.reshape(1, 15)

    # Faz a predição da Classe/Alvo
    predicao_alvo = modelo.predict_classes(y_alvo)

    # Achando a probabilidade
    predict_proba = modelo.predict_proba(y_alvo)
    probabilidade = round((predict_proba[0][0] * 100), 1)

    # Conta quantas vezes procurou a sequência até atingir a probabilidade desejada
    procurando += 1

    # Formata a sequência de números sorteados para ser imprimida
    sequencia = [str(numero[0]).zfill(2) for numero in sorteados]

    # Imprime as informações obtidas no ciclo atual de execução enquanto a probabilidade desejada não foi encontrada
    print(f'Alvo = ({prob_alvo}%) - ACURAC.: {round((pontuacao * 100), 1)}% - Rep.: {str(procurando).zfill(7)}'
          f' - Prob. Enc.: ({str(probabilidade).zfill(2)}%) Sequência: [ ', end='')

    print(*sequencia, ']')

# Resultados
print(f'\nAcuracidade do Modelo: {round((pontuacao * 100), 1)}%')

print('\n0 = Não tem chance de ganhar | 1 = Tem chance de ganhar')
print(f'Resultado: (Previsão Modelo) = {predicao_alvo[0][0]}')

print(f'\nProbabilidade das dezenas sairem: {probabilidade}%')

# Números sorteados (em ordem de sorteio e em ordem crescente)
print(f'\nNúmeros sorteados:  {[numeros[0] for numeros in sorteados]}')
print(f'\nNúmeros ordenados:  {sorted([numeros[0] for numeros in sorteados])}')
