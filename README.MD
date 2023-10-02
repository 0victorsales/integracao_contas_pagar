## integracao_contas_pagar

## Bibliotecas
- 1. json: Biblioteca integrada do Python usado para converter dados em formato JSON em Python.
- 2. requests: Realizar solicitações HTTP, permitindo interações com servidores web, APIs e comunicação na internet.
- 3. Pandas: Manipula e analisa dados em Python, oferecendo estruturas de dados e ferramentas para lidar com tabelas e séries temporais.
- 4. datetime: é utilizada para trabalhar com datas e horas, fornecendo classes e funções para criar, manipular e formatar informações de tempo.
- 5. base64: oferece métodos para codificar e decodificar dados em formato de caracteres ASCII, frequentemente usado para converter dados binários em uma forma textual, por exemplo, para transmissão em canais de comunicação de texto.
- 6. io: fornece classes para operações de entrada e saída, permitindo manipular fluxos de dados de forma similar a arquivos, útil para tratar dados em memória ou interfaces personalizadas.
- 7. numpy: oferece suporte para arrays multidimensionais e funções matemáticas de alto desempenho, essenciais para cálculos numéricos e científicos eficientes.
- 8. random: possibilita a geração de números aleatórios e amostras aleatórias, sendo útil para simulações e seleções aleatórias em programação.

## Credenciais API:
- app key e app secret para os ambientes (Matriz, Filial 1, Filial 2) utilizados na autenticação com a API.

###Endpoints 
- endpoint_incluir_contas_pagar: Necessário para a inclusão de contas a pagar
- endpoint_contas_pagar: Necessário  para listar contas a pagar
- endpoint_listar_clientes: Necessário para listar clientes Omie
- endpoint_contas_corrente: Necessário para listar contas correntes do Omie 

## Links Importantes
Documentação Omie - [Omie API Docs](https://developer.omie.com.br/service-list/)



## Funções
#### dic_clientes_matriz / dic_clientes_base_1 / dic_clientes_base_2
- A API de listagem de clientes do Omie é invocada. A partir disso, uma lista é criada para armazenar informações, como o CNPJ e o código do cliente. A seguir, é criado um dicionário chamado "dicionario_clientes_matriz", composto por listas, onde a chave é representada pelo nome do cliente, e o valor é uma lista contendo o CNPJ e o código correspondente desse cliente no sistema Omie.

#### dic_contas_correntes_matriz / dic_contas_correntes_filial_1 / dic_contas_correntes_filial_2
A partir de um JSON que contém a relação das contas correntes da base, a função cria um dicionário em que a chave é a descrição da conta e o valor é o código da conta.

## Trigger Piperdream
Um webhook é criado no Omie, de modo que quando um contas a pagar é gerado na Matriz, é ativado um trigger no Piperdream, iniciando a execução do código.

## Carregamento de dados
Após a ativação do trigger, o código carrega seis dicionários. Destes, três contêm os dados das contas correntes da Matriz, Filial 1 e Filial 2, outros três contêm os dados dos clientes.

## Verificando contas a pagar
**Protegido por direitos autorais**

## Criando dicionário
Após passar pelas condicionais o código cria um dicionário, contendo alguns dados que foram retornados da API de consultar contas a pagar, listar clientes da matriz e listar contas correntes da filial.

## Criando contas a pagar
Após a criação do dicionário, é realizado um loop para a criação das contas a pagar. Dentro desse loop, encontra-se a função denominada "incluir_conta_pagar", que recebe como parâmetro o dicionário contendo os dados previamente obtidos.

## Requisitos
- Cliente está cadastrado no Omie
- Conta corrente está cadastrada no Omie
- Deve haver um departamento denomidado "Filial 1" ou "Filial 2"