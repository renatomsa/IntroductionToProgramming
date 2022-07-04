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
