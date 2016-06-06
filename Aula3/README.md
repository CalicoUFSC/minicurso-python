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

Exercícios:
----------

###1.
<!--
recebe funcao f e int n
roda f(x) n vezes
retorna resultado -->

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
