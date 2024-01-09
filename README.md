# LOTOFÁCIL  

Jogando na Lotofácil utilizando rede neural.  

## INFORMAÇÕES  

**Linguagem utilizada: Python 3 (v3.8.2)**  

### PRINCIPAIS PACOTES UTILIZADOS  

- Pandas  
- Numpy  
- Keras  
- Scikit-learn

### FUNCIONALIDADES  

- Análise de frequência das dezenas sorteadas por concurso  
- Geração de pesos para cada dezena  
- Criação de jogos  
- Análise de probabilidade das dezenas dos jogos serem sorteadas  

# PRINCIPAIS INFORMAÇÕES DO JOGO  

Informações obtidas no site da Caixa Econômica Federal, acessado em: 08/07/2020.  

**Observação**: Para maiores informações acessar o site da [LOTOFÁCIL](http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/).   
  
## Como jogar  
A Lotofácil é, como o próprio nome diz, fácil de apostar e principalmente de ganhar. Você marca entre 15 a 18 números, dentre os 25 disponíveis no volante, e fatura o prêmio se acertar 11, 12, 13, 14 ou 15 números. Pode ainda deixar que o sistema escolha os números para você por meio da Surpresinha, ou concorrer com a mesma aposta por 3, 6, 9 ou 12 concursos consecutivos através da Teimosinha.

### Apostas  

A aposta mínima, de 15 números, custa R$ 2,50.

### Sorteios  

Os sorteios são realizados às segundas, quartas e sextas-feiras, sempre às 20h.

### Premiação  

O prêmio bruto corresponde a 43,35% da arrecadação. Dessa porcentagem, será deduzido o pagamento dos prêmios com valores fixos:

- R$ 5,00 para as apostas com 11 prognósticos certos entre os 15 sorteados;
- R$ 10,00 para as apostas com 12 prognósticos certos entre os 15 sorteados;
- R$ 25,00 para as apostas com 13 prognósticos certos entre os 15 sorteados.

Após a apuração dos ganhadores dos prêmios com valores fixos, o valor restante do total destinado à premiação será distribuído para as demais faixas de prêmios nos seguintes percentuais:

- 65% entre os acertadores de 15 números;
- 20% entre os acertadores de 14 números entre os 15 sorteados.
- 15% ficam acumulados para a primeira faixa (15 acertos) do concurso especial realizado em setembro de cada ano.

Os prêmios prescrevem 90 dias após a data do sorteio. Após esse prazo, os valores são repassados ao Tesouro Nacional para aplicação no FIES - Fundo de Financiamento ao Estudante do Ensino Superior.

### Recebimento de prêmios  

Você pode receber seu prêmio em qualquer casa lotérica credenciada ou nas agências da Caixa. Caso o prêmio líquido seja superior a R$ 1.332,78 (bruto de R$ 1.903,98) o pagamento pode ser realizado somente nas agências da Caixa. Valores iguais ou acima de R$ 10.000,00 são pagos após 2 dias de sua apresentação na agência da Caixa.

### Acumulação  

Não havendo ganhador em qualquer faixa de premiação, o valor acumula para o concurso seguinte, na faixa de prêmio com 15 acertos. Não deixe de conferir o seu bilhete de aposta.

### Tabela de preços  

|     Quantidade de números   |    Valor em R$    |
| :-------------------------: |:-----------------:|
| 15 números                  |       2,50        |
| 16 números                  |       40,00       |
| 17 números                  |       340,00      |
| 18 números                  |       2.040,00    |  

# COMO UTILIZAR

<!--ts-->
   * [Instalação do interpretador Python](##Instalação-do-interpretador-Python)
   * [Criação do ambiente virtual](##Criação-do-ambiente-virtual)
   * [Projeto](##Projeto)
      * [Estrutura do ambiente](###Estrutura-do-ambiente)
      * [Inserir o projeto no ambiente](###Inserir-o-projeto-no-ambiente)
      * [Inicializar o ambiente](###Inicializar-o-ambiente)
      * [Baixar os pacotes e dependências](###Baixar-os-pacotes-e-dependências)
      * [Criar resultados e combinações](###Criar-resultados-e-combinações)
      * [Rodar o projeto](###Rodar-o-projeto)
      * [Dúvidas e sugestões](###Dúvidas-e-sugestões)
   * [Contribuição](##Contribuição)
<!--te-->

## Instalação do interpretador Python  

O projeto utiliza o Python 3 na versão v3.8.2, e para melhor compatibilidade é recomendado que a versão seja mantida.

[Download - Python 3 v3.8.2](https://www.python.org/downloads/release/python-382/)  

## Criação do ambiente virtual  

Após a instalação do interpretador, versão do projeto, atualize o PIP (gerenciador de pacotes). Para tal, abrar o Prompt de comando ou o PowerShell, no caso do Windows, por exemplo, e execute o camando abaixo. Todos os comandos relacionados ao Python, a partir daqui, serão realizados utilizando o PowerShell do Windows.

```
python -m pip install --upgrade pip
```

Após atualizar o PIP, crie o diretório que irá conter o projeto, sendo que o local fica de sua preferência. Esse diretório será o ambiente virtual que irá possuir o interpretador e os pacotes específicos para o projeto. Como exemplo, será utilizado o diretório `C:\ambientevirtual`. No PowerSell, desloque até o diretório raíz `C:\` aonde irá ser criado o ambiente e execute o comando:

```
python -m venv ambientevirtual
```

Ao criar o ambiente virtual, você estará separando as parametrizações do projeto de outras alterações que possam ter no ambiente externo. Basicamente, você irá instalar neste ambiente somente as dependências que o projeto necessita para ser rodado.

## Projeto  

### Estrutura do ambiente  

Ao acessar o ambiente você irá visualizar a estrutura abaixo:

```
C:\ambientevirtual

    \Include
    \Lib
    \Scripts
    pyvenv.cfg
```

Os diretórios principais são `Lib` e `Scripts` onde o primeiro irá armazenar os pacotes/dependências que serão utilizados no projeto e o outro o arquivo do interpretador assim como os arquivos para inicializar o ambiente, basicamente.

### Inserir o projeto no ambiente  

Para os próximos passos foi utilizado o GIT (ferramenta de versionamento). Caso ainda não saiba como utilizá-lo, existem inúmeros tutoriais no Youtube que poderão te auxiliar.

1. Faça um fork deste repositório clicando no botão `Fork` no canto superior da tela.

1. Dentro do diretório do ambiente virtual abra o Bash do GIT e inicialize o repositório local.

    ```
   $ git init
   ```

1. Faça um clone do repositório para a sua estação de trabalho:

   ```
   $ git clone https://github.com/<seu_usuario>/lotofacil
   ```

   Ob.: Será emitido um alerta de erro para o arquivo `lotofacil/base/resultados.csv` ao qual pode ser desconsiderado. O mesmo será criado posteriormente [Criar resultados e combinações](###Criar-resultados-e-combinações).

### Inicializar o ambiente

Agora que o projeto foi baixado para a sua máquina, se faz necessário inicializar o ambiente.

1. No PowerShell, direcione para o diretório `C:\ambientevirtual\Scripts` e execute o comando:

   ```
   .\Activate.ps1
   ```

    Este comando irá inicializar o ambiente virtual. Para se certificar que o ambiente foi inicializado, neste caso, vai aparecer o nome do diretório entre parenteses (ambientevirtual), geralmente na cor verde, antes do caminho do diretório atual.
    
1. Para finalizar o ambiente, quando o mesmo não estiver em uso, é só executar o comando `deactivate` independente do diretório que estiver no PowerShell.

### Baixar os pacotes e dependências

Para instalar os pacotes e dependências que o projeto irá utilizar, inicialize o ambiente e faça:

1. Atualize o PIP [Criação do ambiente virtual](##Criação-do-ambiente-virtual), independente que já o tenha feito antes durante a criação do ambiente. Assim terá a certeza de estar utilizando a versão mais atual do gerenciador.

1. Execute o comando abaixo no diretório raíz do projeto aonde contém o arquivo `requirements.txt`. Esse comando irá instalar os pacotes conforme a relação contida no arquivo.

    ```
    pip install -r requirements.txt
    ```
1. Agora é preciso instalar mais dois pacotes (TensorFlow e o XRLD):

    ```
    pip install tensorflow
    ```
    
    ```
    pip install xlrd==1.2.0
    ```

### Criar resultados e combinações

No PowerShell, vá para o diretório raíz do projeto e execute os comandos.

1. Para criar o arquivo de resultados:

    ```
    python .\dados\scrapping_resultados.py
    ```

2. Para criar o arquivo de combinações:
   Remova o CSV, que está no diretório combinacoes

    ```
    python .\dados\gerar_combinacoes.py
    ```

### Rodar o projeto

Se todos os passos foram realizados e o ambiente está ativo, agora o projeto está pronto para ser executado. Para isso, execute o comando abaixo no diretório raíz do projeto:

```
python .\jogar.py
```

### Dúvidas, bugs e sugestões

Em casos de dúvida, bugs ou queria propror uma melhoria abra uma Issue. Vamos aprender juntos e desenvolver novas soluções.

## Contribuição

Sinta-se livre para contrituir com o projeto. Para tal, faça:

1. Crie um remote apontando para este repositório:

   ```
   $ git remote add upstream https://github.com/Mekylei-Belchior/lotofacil
   ```

1. Uma vez feito o fork, crie um branch de trabalho (por exemplo, "feature-x")

   ```
   $ git checkout -b feature-x
   ```

1. Trabalhe normalmente no branch feature-x. Quando estiver satisfeito com o resultado, faça o commit e em seguida o push:

   ```
   $ git push origin feature-x
   ```

1. O branch usado no "git checkout" tem que casar com o branch usado no "git push".

1. Por fim, entre no github e abra um Pull Request (PR).
