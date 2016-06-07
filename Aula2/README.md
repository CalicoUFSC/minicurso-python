Aula 2 - Listas e Strings
===============

Conteúdo de aula
----------------

- Listas
- Strings
- Estruturas de repetição (for)
- Módulos

Métodos mais importantes de list e str
--------------------------------------

###[list](https://docs.python.org/3/tutorial/datastructures.html):
```python
lista.append(x)   # Adiciona x no final da lista
lista.remove(x)   # Remove o x com menor indice
lista.pop([i])    # Remove o elemento no indice i, se i não for especificado, remove o elemento no final da lista
lista.count(x)    # Conta quantos elementos iguais a x estão na lista
lista.index(x)    # Retorna o índice do elemento x na lista, se tornará um erro caso o elemento não estiver na lista
```

-----

###[str](https://docs.python.org/3/library/stdtypes.html):
```python
string.split([c])                    # Divide a string em todas as ocorrências de c e retorna uma lista com as partes
string.strip([c])                    # Remove c do inicio e do final da string (pode ser prefixada com l ou r para ser aplicada em apenas um lado)
string.replace(old, new[, count])    # Substitui 'count' ocorrências de old por new, se count não for definido, substitui todas as ocorrências
string.join(iterable)                # Retorna uma string
string.startswith(s)/endswith(s)     # Testa se a string começa/termina com s
lista = list(string)                 # Transforma a string em uma listas (passa a ser modificável)
```

-----

###Comando [**for**](https://wiki.python.org/moin/ForLoop):

Sintaxe:
```python
for i in iter:
	# Corpo do for
```

Em que `i` é a variável de iteração e `iter` é um **iterável**, como por exemplo uma lista, uma string, uma tupla, um generator ou um dicionário.

Exemplos de for-loops:

####Lista:
```python
lista = [1, 2, 3]
for elemento in lista:
	print(elemento)

```

Imprimirá:

```
1
2
3
```

####String:
```python
string = 'Hello, World!'
for char in string:
	print(char)
```
Imprimirá:

```
H
e
l
l
o
,

W
o
r
l
d
```

####Range:
```python
for i in range(10):
	print(i)
```

Este `for` funciona de maneira idêntica a este outro `for`:

```java
for(int i = 0; i < 10; ++i)
	System.out.println(i);
```

###Utilidades para iteráveis:

####Range:
```python
range(stop)                # Retorna uma sequência de 0 até stop, incrementando em 1 a cada iteração
range(start, stop[, step]) # Retorna uma sequência de start até stop, incrementando em step a cada iteração
```

Obs: o intervalo é sempre [start, stop)

Exemplos:
```python
range(10)        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(3, 7)      # 3, 4, 5, 6
range(5, 100, 5) # 5, 10, 15, 20, 25, 30, 35, 40, 45
range(1, 20, 2)  # 10, 8, 6, 4, 2, 0, -2, -4, -6, -8
```

####Enumerate:

```python
enumerate(iteravel) # Retorna uma sequência de tuplas na forma (index, iteravel[index])
```

Exemplo:
```python
string = 'python'
for index, char in enumerate(string):
	print(index, char)
```

Imprimirá:

```
0 p
1 y
2 t
3 h
4 o
5 n
```

Exercícios:
----------

###1. Quem curte?

Escreva uma função chamada **likes** que recebe uma lista de nomes (strings) e devolve uma string formatada como nos exemplos abaixo:

```python
likes([])                                       # deve retornar: "Ninguém curtiu isso ainda"
likes(["Ana"])                                  # deve retornar: "Ana curtiu isso"
likes(["Bianca", "Carlos"])                     # deve retornar: "Bianca e Carlos curtiram isso"
likes(["Daniel", "Eliana", "Fabio"])            # deve retornar: "Daniel, Eliana e Fabio curtiram isso"
likes(["Giulia", "Heloisa", "Isabela", "João"]) # deve retornar: "Giulia, Heloisa e 2 outros curtiram isso"
```

A partir de 4 elementos apenas o número em `2 outros curtiram` aumenta.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###2. URL

Escreva uma função chamada **domain_name** que receba uma string `url` e retorne o nome do domínio como uma string.

Exemplos:

```python
domain_name("http://github.com/calicoufsc/minicurso-python") == "github"
domain_name("http://www.facebook.com") == "facebook"
domain_name("https://ufsc.br") == "ufsc"
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###3. Elementos repetidos
Escreva uma função chamada **remove_duplicates** que receba uma lista e teste se ela possui mais de um do mesmo elemento. Caso sim remova as que tiverem menor índice.

Exemplo:
```python
remove_duplicates([1,2,1,3,1,2]) == [3, 1, 2]
remove_duplicates([5,4,3,2,1,2,3,4,5]) == [1, 2, 3, 4, 5]
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###4. Paridade diferente

Escreva uma função chamada **different_evenness** que recebe uma string com inteiros separados por espaços.

Todos os inteiros dessa string tem uma mesma paridade, exceto um. Retorne o índice deste inteiro.

Exemplo:
```python
different_evenness("1 2 2") == 0
different_evenness("2 4 7 8 10") == 2
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###5. Pare de retrevni sahnim !sesarf

Escreva uma função chamada **spin_words** que recebe uma frase e inverte todas as palavras que tenham pelo menos 5 letras.

Exemplo:
```python
spin_words('Pare de inverter minhas frases!') == 'Pare de retrevni sahnim !sesarf'
```