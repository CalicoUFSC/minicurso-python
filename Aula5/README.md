Aula 5 - Imports e I/O de arquivos
===================================================

Conteúdo de aula
----------------

- Imports
- I/O de arquivos
- Biblioteca padrão:
	- math
	- random
	- sys

###Imports

Para trabalhar com códigos extensos é interessante dividir o código em vários arquivos.

Um módulo pode acessar o outro através de um `import`.

Por exemplo:

sqrt.py
```python
def square_root(base, expoente=2):
	return base**(1/expoente)
```

main.py
```python
import sqrt

for i in range(10):
	print(sqrt.square_root(i))
```

Também é possível importar apenas partes de um módulo:

main.py
```python
from sqrt import square_root

for i in range(10):
	print(square_root(i))
```


Exercícios:
----------

###1. Problema de Monty Hall ([PT](linkpt)/[EN](linken))

Escreva um programa que implemente uma simulação do Problema de Monty Hall.

O jogo consiste no seguinte:

- Monty Hall (o apresentador) apresenta 3 portas aos concorrentes, sabendo que atrás de uma delas está um carro e que as outras têm cabras.

- O concorrente escolhe uma porta (que ainda não é aberta)

- Em seguida Monty abre uma das outras duas portas que o concorrente não escolheu (nunca será a porta com o carro)

- Agora com duas portas apenas para escolher e sabendo que o carro está atrás de uma delas, o concorrente tem que se decidir se permanece com a porta que escolheu no início do jogo e abre-a ou se muda para a outra porta que ainda está fechada para então a abrir.


O programa deverá receber 2 argumentos pela linha de comando ou pela função `input`: `rounds` (int) e `swap` (bool).

`rounds` determina quantas vezes o jogo será simulado e `swap` determina se o jogador trocará sua escolha após a primeira porta com uma cabra ser aberta.



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###1. Nomes

https://projecteuler.net/problem=22


[linkpt]: https://pt.wikipedia.org/wiki/Problema_de_Monty_Hall
[linken]: https://en.wikipedia.org/wiki/Monty_Hall_problem