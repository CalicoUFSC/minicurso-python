Aula 1 - Listas
===============

Conteúdo de aula
----------------

- Listas
- Estruturas de repetição (for)
- List comprehensions
- Módulos

Métodos mais importantes de list e str
--------------------------------------

###[list](https://docs.python.org/3/tutorial/datastructures.html):
```python
append(x)   # Adiciona x no final da lista
remove(x)   # Remove o x com menor indice
pop([i])    # Remove o elemento no indice i, se i não for especificado, remove o elemento no final da lista
count(x)    # Conta quantos elementos iguais a x estão na lista
index(x)    # Retorna o índice do elemento x na lista, se tornará um erro caso o elemento não estiver na lista
```

###[str](https://docs.python.org/3/library/stdtypes.html):
```python
split([c])                    # Divide a string em todas as ocorrências de c e retorna uma lista com as partes
strip([c])                    # Remove c do inicio e do final da string (pode ser prefixada com l ou r para ser aplicada em apenas um lado)
replace(old, new[, count])    # Substitui 'count' ocorrências de old por new, se count não for definido, substitui todas as ocorrências
join(iterable)                # Retorna uma string
startswith(s)/endswith(s)     # Testa se a string começa/termina com s
```

- Strings podem ser transformadas em listas para facilitar a manipulação

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

A partir de 4 elemenos apenas o número em `2 outros curtiram` aumenta.

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