Aula 3 - List comprehensions, generators e callback
===================================================

Conteúdo de aula
----------------

- List comprehensions
- Generators
- Callback


###List comprehensions:
Oferece uma sintaxe mais elegante para criar listas.

Similar a notação de conjuntos:
[https://en.wikipedia.org/api/rest_v1/media/math/render/svg/0613bcc58e223e12836b2799cf5cf64c024066dc]

Este código:

```python
squares = [i**2 for i in range(10)]
```

é equivalente a:

```python
squares = []
for i in range(10):
	squares.append(i**2)
```

####É possível usar condicionais dentro de uma list comprehension:
```python
cubes = [i**3 for i in range(20) if i**3 % 2 == 0]
```

é equivalente a:

```
cubes = []
for i in range(10):
	if i**3 % 2 == 0:
		cubes.append(i**3)
```

###Também é possível usar mais de um for:
```python
idk = [i**j for i in range(10) for j in range(i)]
```

é equivalente a:

```
idk = []
for i in range(10):
	for j in range(i):
		idk.append(i**j)
```

###Generators:

Usados para gerar valores sob demanda.

Usa a keyword `yield` ao invés de `return`.

Execução é pausada a cada yield e pode ser retornada chamando next(generator) ou iterando usando um `for`.

Exemplo:
```python
def gen():
	i = 0
	while True:
		yield i
		i += 1

g = gen()

for i in g:
	print(i) # imprimirá os números inteiros a partir de 0 infinitamente

```
Exercícios:
----------

###1. Map

Escreva uma função chamada **map** que recebe uma função (func) e uma lista na forma [x1, x2, ..., xn] e retorne uma lista na forma [func(x1), func(x2), ..., func(xn)].

Use list comprehensions.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###2. Zip

Escreva uma função/generator chamada **zip** que recebe uma lista de listas [list1, list2, ..., listn] e na i-ésima chamada de `next` retorne (`yield`) uma **tupla** com os i-ésimos elementos de cada lista (list1[i], list2[i], ..., listn[i]).

Use list comprehensions.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###4. Apply

Escreva uma função chamada **apply** que recebe uma função `f` e um int `n` e retorna outra função que aplica `f` em `x` `n` vezes.

Exemplo:
```python
func = apply(f, 3)

func(x) == f(f(f(x)))
```
