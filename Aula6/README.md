Aula 5 - Decorators, Exceptions e Context managers
===================================================

Conteúdo de aula
----------------
- Decorators
- Exceptions
- Context managers
- Biblioteca padrão:
	- functools
	- json
	- pickle

###Exceptions
Iniciar uma exceção:

```python
raise Exception()
```

Ou:

```python
raise Exception('descrição do erro')
```

`Exception` pode ser alterada pra qualquer subclasse de Exception.

Tratar uma exceção:

```python
try:
	# código que potencialmente gera uma exceção
except Exception:
	# tratamento da exceção
```

Pode-se recuperar a o objeto da exceção utilizando:

```python
try:
	# código que potencialmente gera uma exceção
except Exception as e:
	# tratamento da exceção
```

Deste modo o objeto da exceção será guardado em `e`.

`Exception` pode ser alterada pra qualquer subclasse de Exception, fazendo com que todas as exceções que não forem subclasse da dada subclasse passem pelo `try-except` sem tratamento.

Também é possivel se assegurar que um bloco de código execute havendo ou não exceção usando `finally`.

```python
try:
	# código que potencialmente gera uma exceção
except Exception as e:
	# tratamento da exceção
finally:
	# sempre será executado
```

Por exemplo, este código sempre fechará o arquivo, evitando um [resource leak](https://en.wikipedia.org/wiki/Resource_leak):

```python
f = open('file')
try:
	# código que usa o arquivo
finally:
	f.close()
```


###Decorator
Jeito conveniente de estender a funcionalidade de uma função sem alterar seu código.

Sem decorator:

```python
def bold(func):
	def wrapper(name):
		return "<b>{}</b>".format(func(name))
	return wrapper

def greet(name):
   return "Hello, {}!".format(name)

greet = bold(greet)

print(greet("Maria"))  # <b>Hello, Maria!</b>```

Com decorator:
```python
def bold(func):
	def wrapper(name):
		return "<b>{}</b>".format(func(name))
	return wrapper

@bold
def greet(name):
   return "Hello, {}!".format(name)

print(greet("Maria")) # <b>Hello, Maria!</b>```
```

Pode-se usar vários decorators em uma única função. A ordem de avaliação dos decorators é top-down.

```python
def bold(func):
	def wrapper(name):
		return "<b>{}</b>".format(func(name))
	return wrapper

def italic(func):
	def wrapper(name):
		return "<i>{}</i>".format(func(name))
	return wrapper

@bold
@italic
def greet(name):
   return "Hello, {}!".format(name)

print(greet("Maria")) # <b><i>Hello, Maria!</i></b>
```

###Context managers

Provê alocação/desalocação segura de recursos (arquivos, sockets de rede, etc), garantindo a desalocação ao final do bloco.

Exemplo usando arquivos:

```python
with open('file') as arquivo:
	# código que manipula a variável arquivo
```

Para utilizar outra função ao invés de open, o objeto retornado pela função deve ter os métodos `__enter__` e `__exit__` definidos.

##functools
```python
lru_cache(maxsize=128, typed=False)       # decorator que memoriza os resultados da função de acordo com o input

partial(func, *args, **kwargs)            # retorna uma nova função que, quando chamada, se comportará como func(*args, **kwargs)

partialmethod(func, *args, **kwargs)      # igual a partial, mas feito para métodos e não funções

reduce(function, iterable[, initializer]) # aplica uma função de dois argumentos cumulativamente aos itens de iterable até reduzir a sequência em um único valor
                                          # se initializer for passado, é colocado antes de todos os elementos no calculo
```
Exemplos:


```python
from time import clock
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
	total = 1
	while n > 0:
		total *= n
		n -= 1
	return total

start_time = clock()

factorial(100000)

first_call = clock()

factorial(100000)

second_call = clock()

print("First call to factorial:", first_call-start_time)
print("Second call to factorial:", second_call-first_call)

# First call to factorial: 3.228427
# Second call to factorial: 2.9999999999752447e-06
```

```python
from functools import partial
basetwo = partial(int, base=2) # transforma uma string de zeros e uns em um int
basetwo('10010')               # retorna 18
```


```python
from functools import partialmethod
class Cell(object):
	def __init__(self):
		self.alive = False

	def set_state(self, state):
		self.alive = bool(state)

	set_alive = partialmethod(set_state, True)
	set_dead = partialmethod(set_state, False)

c = Cell()

c.alive # False

c.set_alive()

c.alive # True
```

###json e pickle

Sevem para transferir informação entre programas ou guardar informação em arquivos.

Ambos os módulos possuem as funções `dumps` e `loads`.

`dumps` transforma o objeto passado como argumento em uma string que pode ser enviada pela rede ou escrita em um arquivo.

`loads` transforma uma string carregada de um arquivo ou transferida pela rede em um objeto python.

####json
#####Vantagens:
- É legivel para humanos
- Compatível com quase todas as linguagens

#####Desvantagens:
- Só funciona com tipos padrões

####pickle
#####Vantagens:
- Ilegivel para humanos
- Compatível penas com a mesma versão de Python que foi feito o `dumps`

#####Desvantagens:
- Funciona com qualquer tipo
