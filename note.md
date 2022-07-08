# Aula 1

***

## Algoritmo
### uma ideia para a resolução de um programa computacional
conjunto ordenado de passos **executáveis** não ambíguos, definindo um processo que tem um término
* **ordem** é importante
* o primeiro passo é entender o problema para desenvolver uma solução (análise de requisitos --> engenharia de requisitos)
* criar a solução do algoritmo antes de começar a codar
* Definir uma linguagem de programação adequada para a resolução do programa
* Pseudo-algoritmo 
```
leia x 
compute y como (x * 2)
imprima y
```

***

## Variáveis
### Espaço de memória que armazena informações
* nome adequado e intuitivo para alguma variável
* tipos de variáveis
  * conjunto de valores equipado com um canjunto de ações
  * numéricos (integer, float), string (textual), booleanos
* o comando "=" armazena valores em variáveis
  * x = x+1 (**atribuição** (destrutiva: valor anterior não existe mais na memória) de x+1 à variável "x")
```
int x,
x = 4
```

### Regras
* não começar com número
* não conter caracteres especiais e acentuação
* ordem de precedência: prioridade de expressões numéricas e lógicas

### Estruturas de Controle
* Sequência
  * comandos executados um após o outro
* Seleção
  * seleciona entre dois possíveis caminhos
* Repetição
  * executa um conjunto de ações enquanto uma condição for verdadeira
* Validação dos dados de entrada

### Laços de Repetição
```
inteiro x
leia x
enquanto (x > 0) faça
  imprima x
  x = (x -1)
```
```
inteiro n1
inteiro n2
leia n1
leia n2
se n1 >= n2:
  imprima n1
  imprima n2
senão
  imprima n2
  imprima n1
```
* separar a parte da lógica e a parte de testes (impressão) para um código mais limpo

```
inteiro auxiliar
inteiro A
inteiro B
leia A
leia B

se (A > B) então
  auxiliar = B
  B = A
  A = auxiliar
  imprimir A
  imprimir B
```
***

# Aula 2
### Compiladores e Interpretadores
* Python é uma linguagem interpretada
 * Baixar python e testar no cmd `python --version`
* Instalação do ambiente Jupyter `pip install jupyter`
* `jupyter notebook` --> abre o caderno no navegador

## Introdução à Python
* Comandos de entrada e de saída (print)
* **Em outras linguagens de programação, como C e Java, utiliza-se aspas simples '' para caracteres e aspas duplas "" para textos**
### Variáveis para o armazenamento de informações
```
mensagem = 'pyhton é massa'
print (mensagem)
```
* tipagem de dados
```
int(input('Ditite um número: '))
```
* não começar nome de variáveis com número
* não utilizar caracteres especiais
* utilizar _ para separar palavras

# Aula 3
## Tipos primitivos de Python (linguagens de programação já utilizam)
### Tipos estáticos e Tipos dinâmicos

* tipos estáticos
 * define estaticamente o tipo de dado que será armazenado
 * evita erros de atribuição de dados de outro tipo para uma variável
* tipos dinâmicos
 * tipos podem mudar de acordo com as diferentes atribuições
 * programador fica mais livre em relação ao uso de dados

### Tipos Numéricos
* integers : ... -1, -2, 0, 1, 2 ...
* floats: 2.24, 32.2E-5

### Símbolos especiais
* \n - quebrar a linha
* \t - deslocamento de uma tabulação
* \ - não encerra a string quando adicionada uma aspas

### Operadores
* "+" concatenador

### Manipulações com Strings
* var.title() - transforma as primeiras letras da String em Maiúscula
* var.upper() - toda a frase em maiúscula
* var.lower() - toda a frase em minúscula
* var.split() - lista de palavras
* var.join() - junta as palavras

No Jupyter - `%config IPCompleter.greedy=True`

### Formatação de Saída
* Método format
 * Inclui operadores de concatenação
 * Insere os espaços corretamente
 * Converte explicitamente os tipos numéricos para strings
```
nome = 'Augusto'
idade = 18
print('Parabéns, {0}! Hoje você completa {1} anos!'.format(nome,idade))
```
* não é necessário colocar o índice caso queira colocar na ordem em que aparecem as variáveis

```
print(f'Parabéns, {nome}! Hoje você completa {idade} anos!)
```
outro exemplo de utilização do format (no início do print)

* // - deixa a divisão sem resto

# Aula 4
## Expressões Lógicas

```
 if expressao1:
  #bloco 1
 elif expressao2:
  #bloco 2
 else:
  #ultimobloco
```
### Coerção de Tipos
* forçar a conversão de tipos

### Operadores Lógicos e Relacionais
* == (igual), =! (diferente) etc
* abreviações - a =+ 2 == a = a + 2

```
while (#Expressão_booleana):
  #bloco
```
```
for i in range (0,10):
  print i
```
