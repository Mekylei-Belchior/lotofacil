from calcular import calcular_numero_pesos
from sortear import sortear_numeros
from dados import criar_modelo
import pandas as pd


# Inicialização das variáveis
probabilidade = 0.00
procurando = 0
sorteados = list()
predicao_alvo = 00.00

# probabilidade desejada
prob_alvo = 100.0

peso, numero_pesos = calcular_numero_pesos()
modelo, pontuacao = criar_modelo()

# Replica até que a probabilidade seja igual à desejada
while probabilidade < prob_alvo:

    # Atribui a sequência dos números sorteados
    sorteados = sortear_numeros(peso, numero_pesos)

    # Criando o dataframe com os números sorteados para realizar a predição
    y_alvo = pd.DataFrame(sorteados)
    y_alvo = y_alvo.iloc[:, 0].values
    y_alvo = y_alvo.reshape(1, 15)

    # Fazendo a predição da Classe/Alvo
    predicao_alvo = modelo.predict_classes(y_alvo)

    # Achando a probabilidade
    predict_proba = modelo.predict_proba(y_alvo)
    probabilidade = round((predict_proba[0][0] * 100), 1)

    # Conta quantas vezes procurou a sequência até atingir a probabilidade desejada
    procurando += 1

    sequencia = [str(numero[0]).zfill(2) for numero in sorteados]

    print(f'Alvo = ({prob_alvo}%) - ACURAC.: {round((pontuacao[1]*100), 1)}% - Rep.: {str(procurando).zfill(7)}'
          f' - Prob. Enc.: ({str(probabilidade).zfill(2)}%) Sequência: [ ', end='')

    print(*sequencia, ']')

# Resultados
print(f'\nAcuracidade do Modelo: {round((pontuacao[1]*100), 1)}%')

print('\n0 = Não tem chance de ganhar | 1 = Tem chance de ganhar')
print(f'Resultado: (Previsão Modelo) = {predicao_alvo[0][0]}')

print(f'\nProbabilidade das dezenas sairem: {probabilidade}%')

# Números sorteados
print(f'\nNúmeros sorteados:  {[numeros[0] for numeros in sorteados]}')
print(f'\nNúmeros ordenados:  {sorted([numeros[0] for numeros in sorteados])}')
