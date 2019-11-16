from calcular import calcular_pesos, calcular_numero_pesos
from sortear import sortear_numeros

import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

# Importando os dados da planilha do Excel
# Gerando o dataframe da base de dados

caminho = 'base_dados.xlsx'
planilha = pd.ExcelFile(caminho)
dados = pd.read_excel(planilha, 'Importar')

# Reajustando a columa de ganhadores para: 1 - concurso com ganhadores | 0 - concurso sem ganhadores
dados.loc[dados['Ganhadores'] > 1, 'Ganhadores'] = 1

# Preparando os dados para o modelo
# Seleciona todas as linhas mais as colunas das dezenas sorteadas e a coluna de ganhadores
dados = dados.iloc[:, 2:18]

# Separando atributos (bolas = x) e classe (ganhadores = y)
atributos = dados.iloc[:, 0:15].values
classe = dados.iloc[:, 15].values

# Geração da seed para replicação do modelo
seed = 12
np.random.seed(seed)

# Dividindo os dados em treino (70%) e teste (30%)
X_treino, X_teste, y_treino, y_teste = train_test_split(atributos, classe, test_size=0.3, random_state=seed)

# Criando o modelo
modelo = Sequential()
modelo.add(Dense(2, input_dim=15, activation='relu'))
modelo.add(Dense(8, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))

# Compilando o modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinando o modelo
modelo.fit(X_treino, y_treino, epochs=100, batch_size=10)

# Avaliação do modelo
pontuacao = modelo.evaluate(X_teste, y_teste)

# Inicialização das variáveis
probabilidade = 0.00
prob_alvo = 99.5   # probabilidade desejada
procurando = 0
sorteados = []
predicao_alvo = 00.00

peso = calcular_pesos()
numero_pesos = calcular_numero_pesos()

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
          f' - Prob. Enc.: ({str(probabilidade).zfill(2)}%) Seq: {sequencia}')

# Resultados
print(f'\nAcuracidade do Modelo: {round((pontuacao[1]*100), 5)}%')

print('\n0 = Não tem chance de ganhar | 1 = Tem chance de ganhar')
print(f'Resultado: (Previsão Modelo) = {predicao_alvo[0][0]}')

print(f'\nProbabilidade das dezenas sairem: {probabilidade}%')

# Números sorteados
print(f'\nNúmeros sorteados:  {[numeros[0] for numeros in sorteados]}')
print(f'\nNúmeros ordenados:  {sorted([numeros[0] for numeros in sorteados])}')
