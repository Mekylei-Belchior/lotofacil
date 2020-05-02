from dados.dados_bin import dados_treino_teste

from keras.layers import Dense
from keras.models import Sequential


def gerar_modelo(primeira_camada=2, segunda_camada=160, terceira_camada=64, saida=32, periodo=50, lote=5):

    grupos_treino_teste = dados_treino_teste()

    pontuacao = list()

    modelo = Sequential()

    for grupo in grupos_treino_teste:

        x_treino, x_teste, y_treino, y_teste = grupo

        modelo.add(Dense(primeira_camada, input_dim=5, activation='relu'))
        modelo.add(Dense(segunda_camada, activation='relu'))
        modelo.add(Dense(terceira_camada, activation='relu'))
        modelo.add(Dense(saida, activation='softmax'))

        modelo.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        modelo.fit(x_treino, y_treino, epochs=periodo, batch_size=lote, validation_data=(x_teste, y_teste))

        pontuacao.append(modelo.evaluate(x_teste, y_teste))

    return modelo, pontuacao

