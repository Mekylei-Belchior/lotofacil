from combinacoes.analises import remover_resultado_concursos
from combinacoes.possibilidades import obter_possibilidades
from combinacoes.resultados import resultados_ordenados
from calculos.pesos import calcular_numero_pesos
from sorteios.sortear import sortear_numeros
from modelo.modelo import criar_modelo

from pandas import DataFrame


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

print()
print(f'\033[1;33mCarregando e reajustando os demais dados...\033[m')
print()

possibilidades = obter_possibilidades()
resultado_concursos = resultados_ordenados()
possibilidades_atualizada = remover_resultado_concursos(
                                                        possibilidades, 
                                                        resultado_concursos
                                                        )
jogo_aceito = False

# Replica até que a probabilidade atual seja igual à probabilidade desejada
while probabilidade < prob_alvo and not jogo_aceito:

    # Atribui a sequência dos números sorteados
    sorteados = sortear_numeros(peso, numero_pesos)
    jogo = sorted([numeros[0] for numeros in sorteados])

    # Cria o dataframe com os números sorteados para realizar a predição
    y_alvo = DataFrame(sorteados)
    y_alvo = y_alvo.iloc[:, 0].values
    y_alvo = y_alvo.reshape(1, 15)

    # Faz a predição da Classe/Alvo
    predicao_alvo = modelo.predict(y_alvo)

    # Achando a probabilidade
    predict_proba = modelo.predict(y_alvo)
    probabilidade = round((predict_proba[0][0] * 100), 1)

    # Verifica se o jogo é possível e se ainda não foi sorteado em algum concurso
    if probabilidade >= prob_alvo:
        jogo_aceito = [True if jogo in possibilidades_atualizada else False]
        
        if jogo_aceito:
            if jogo != [2, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 21, 23, 24, 25]:
                jogo_aceito = False
    else:
        jogo_aceito = False

    # Conta quantas vezes procurou a sequência até atingir a probabilidade desejada
    procurando += 1

    # Formata a sequência de números sorteados para ser imprimida na tela
    sequencia = [str(numero[0]).zfill(2) for numero in sorteados]

    # Imprime as informações obtidas no ciclo atual de execução enquanto a probabilidade desejada não foi encontrada
    print(f'Alvo = ({prob_alvo}%) - ACURAC.: {round((pontuacao * 100), 1)}% - Rep.: {str(procurando).zfill(7)}'
          f' - Prob. Enc.: ({str(probabilidade).zfill(2)}%) Sequência: [ ', end='')

    print(*sequencia, ']')

    if not jogo_aceito:
        probabilidade = 0.0


# Resultados
print(f'\nAcuracidade do Modelo: {round((pontuacao * 100), 1)}%')

print('\n0 = Não tem chance de ganhar | 1 = Tem chance de ganhar')
print(f'Resultado: (Previsão Modelo) = {predicao_alvo[0][0]}')

print(f'\nProbabilidade das dezenas sairem: {probabilidade}%')

# Números sorteados (em ordem de sorteio e em ordem crescente)
print(f'\nNúmeros sorteados:  {[numeros[0] for numeros in sorteados]}')
print(f'\nNúmeros ordenados:  {jogo}')
