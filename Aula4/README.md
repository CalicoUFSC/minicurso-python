Aula 3 - Classes e Dicionários
===================================================

Conteúdo de aula
----------------

- Classes
- Dicionários

###Classes

Estrutura que abstrai um conjunto de objetos com características similares.

Uma classe é composta de métodos e atributos.

Estrutura básica de uma classe em Python:

```python
class Person:                   # Palavra chave "class" seguida do nome da classe
	def __init__(self, name):   # O método "__init__" é especial, ele serve como construtor da classe.
	                            # O primeiro argumento de um método de uma classe é a instância na qual o método foi chamado
		self.name = name        # Guardando a variável "name" na instância atual

	def greet(self, other):
		return "Hello {}, my name is {}!".format(other, self.name) # Acessando a variável "name" da instância atual
```


Instanciando uma classe:

```python
andre = Person('André')
beatriz = Person('Beatriz')
```

Chamando um método de um objeto:

```python
andre.greet('Carlos')
beatriz.greet('Daniela')
```

Podemos também testar o tipo do objeto recebido como argumento de um método e alterar o comportamento de acordo.

Para isso usamos o método `isinstance`, passando como primeiro argumento o objeto a ser testado e como segundo argumento o tipo suposto.

Por exemplo:

```python
class Person:
	def __init__(self, name):
		self.name = name

	def greet(self, other):
		if isinstance(other, Person):                                       # Se "other" for um objeto do tipo Person
			return "Hello {}, my name is {}!".format(other.name, self.name) # Acessa a variável "name" do objeto "other"
		else:
			return "Hello {}, my name is {}!".format(other, self.name)
```


### Sobrecarga de operadores

Métodos que podem ser sobrescritos:

|Operador|  Método    |
|--------|------------|
|+       | `__add__`  |
|-       | `__sub__`  |
|*       | `__mul__`  |
|/       | `__div__`  |
|<       | `__lt__`   |
|<=      | `__le__`   |
|==      | `__eq__`   |
|!=      | `__ne__`   |
|>=      | `__ge__`   |
|>       | `__gt__`   |
|str()   | `__str__`  |
|len()   | `__len__`  |
|bool()  | `__bool__` |
|int()   | `__int__`  |


Por exemplo:

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def greet(self, other):
			if isinstance(other, Person):
				return "Hello {}, my name is {}!".format(other.name, self.name)
			else:
				return "Hello {}, my name is {}!".format(other, self.name)

	def __add__(self, other):        # Sobrescrevendo o operador "+" para
		return self.age + other.age
```
<!--
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
``` -->

###Dicionários

Um dicionário é uma generalização da lista onde o índice pode ser qualquer valor.

Usado para armazenamento chave-valor.

Também conhecido em outras linguagens como `map`.

Exemplos:


```python
# Chave: Nome
# Valor: Idade

pessoas = { 'Alice' : 10, 'Bernardo' : 20, 'Carla' : 30 }
```

Adicionar e modificar valores:

```python
pessoas['Alice'] = 15
pessoas['Daniel'] = 40
```

Remover um elemento:

```python
del pessoas['Bernardo']
```

Teste de pertinência:

```python
'Alice' in pessoas # Retorna um booleano
```

Iterar sobre dicionário:

```python

for chave in pessoas.keys():
	print(chave)
	print(pessoas[chave])
```

Tamanho do dicionário:
```python
len(pessoas)
```

Exercícios:
----------

###1. Book
Implemente uma classe chamada `Book`.

O construtor dessa classe receberá uma string `name` e um ine `page_count`.

A transformação dessa classe em string deve retornar `name`.

A soma e subtração de dois `Book`s devem retornar respectivamente a soma e subtração de seus `page_count`s.

O operador de comparação `==` deve testar se o `name` e o `page_count` de dois `Book`s são iguais.

E os operadores de comparação `>` e `<` devem operar sobre os `page_count`s.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###2. Vector
Implemente uma classe chamada `Vector`.

O construtor dessa classe receberá uma lista de inteiros.

A soma de dois `Vector`s deve retornar um novo `Vector` com os elementos de cada índice somados. A subtração deve fazer o mesmo, mas subtrair ao invés de somar.

A multiplicação por um escalar deve retornar um novo `Vector` com a lista interna multiplicada pelo dado escalar.

O operador de comparação `==` deve testar se as listas internas são iguais.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###3. Library

Implemente uma classe chamada `Library`.

Esta classe possuirá um dicionário que endereça um código (string) a um objeto `Book` (ex 1).

Os métodos necessários são:

add(cod, book) - Adiciona book no índice cod
get(cod)       - Retorna o book associado
__len___()     - Retorna o tamanho do dicionário

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
