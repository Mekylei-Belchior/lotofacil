import pandas as pd

from itertools import product

caminho = 'C:\\Users\\mekyl\\Documents\\GitHub\\lotofacil\\base_dados.xlsx'
planilha = pd.ExcelFile(caminho)
base = pd.read_excel(planilha, 'Importar_Bin')


def gerar_classes(caracteres=(0, 1), elementos=5):
    """
    Gera classes com as combinações possíveis de saída para cada grupo de 5 dezenas.

    Exemplo:

    dezenas do primeiro grupo: (1, 2, 3, 4, 5)
    dezenas sorteadas do primeiro grupo: (1, 4, 5)
    Classe: (1, 0, 0, 1, 1)

    :param caracteres: [0, 1] - 0 : dezena não sorteada | 1 : dezena sorteada.
    :param elementos: quantidade de elementos que a classe possui.
    :return: a lista de classes possíveis.
    """

    classes = [[]]

    combinacoes = product(caracteres, repeat=elementos)

    for combinacao in combinacoes:
        classes[0].append(combinacao)

    return classes


dados = base.iloc[:, 2:32]

classes = gerar_classes()

novo_c1 = []
c1 = dados.iloc[:, 25].apply(lambda x: list([int(y) for y in str(x).zfill(5)])).values
novo_c1.append([c for c in c1])

indices = novo_c1[0][:]
novo_c1.clear()

for i in range(len(indices)):

    indice = tuple(indices[i])
    valor = classes[0].index(indice)

    novo_c1.insert(i, valor)

print(novo_c1)

