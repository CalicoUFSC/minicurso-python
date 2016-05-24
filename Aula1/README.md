Aula 1 - Tipos primitivos, estruturas de controle/repetição e funções
=====================================================================

Conteúdo de aula
----------------

- Variáveis

- Print/input

- Tipos primitivos

<!-- - Palavras reservadas -->

- Operações lógicas e aritméticas

- Funções

- Indentação

- Estruturas de controle

- Estruturas de repetição

Exercícios:
----------

###1. Fatorial

Escreva uma função chamada **factorial** que receba um valor 'n' e retorne **n!**.

Lembre-se que:

```python
factorial(0) == 1
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###2. Série de Fibonacci

Escreva uma função chamada **fibonacci** que receba um valor 'n' e retorne o n-ésimo termo da Sequência de Fibonacci

Lembre-se que:

```python
fibonacci(0) == 0
fibonacci(1) == 1
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###3. Números Primos

Um número natural é primo se é divisível apenas por 1 e por si mesmo.
Isto sugere o seguinte algoritmo:

```
'n' é o número que desejamos testar a primalidade.
Se 'n' é 1, então 'n' não é primo.
Se 'n' é 2, então 'n' é primo.
Caso contrário,
Seja 'd' um possível divisor, cujo valor é inicialmente 2.

Repetir enquanto d < n:
    Se o resto da divisão de 'n' por 'd' é zero, então 'n' não é primo.
    Caso contrário,
    Incrementar 'd'.
Se 'd' é igual ou maior que 'n', então terminar repetição diagnosticando 'n' como primo.
```

Escreva uma função chamada **is_prime** que implemente o algoritmo acima, recebendo um número positivo e retornando `True` se 'n' for primo e `False` caso contrário.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###4. Algarismos romanos

Escreva uma função chamada **to_roman** que receba um número maior que zero e menor que 3999 e retorne sua representação em algarismos romanos.

Exemplo:
```python
to_roman(1985) == 'MCMLXXXV'
```