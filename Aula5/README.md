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

###I/O de arquivos:

Para abrir arquivos em disco utilizamos a função `open`, que retorna um objeto usado para ler e escrever no arquivo escolhido.

A função open recebe vários parâmetros. Os mais importantes são os dois primeiros, que se referem ao nome do arquivo e ao `mode`

Os possíveis valores de `mode` mais importantes:
```python
'r' # open for reading (default)
'w' # open for writing, truncating the file first
'x' # open for exclusive creation, failing if the file already exists
'a' # open for writing, appending to the end of the file if it exists
```

Exemplo:
```python
txt = open(filename)

text = txt.read()

print(text)

txt.close()
```

```python
txt = open(filename)

for i in range(10):
	txt.write(i)

txt.close()
```

Além destes métodos também existe o `readlines`, que retorna todo o conteúdo do arquivo na forma de uma lista, em que cada elemento é o conteúdo de uma linha do arquivo.

###Biblioteca Padrão:

####[math][https://docs.python.org/3/library/math.html]
```python
log(x[, base])  # Retorna o logaritmo de x na base e. Se a variável base for definida, ela será usada no lugar de e
exp(x)          # Retorna e**x
ceil(x)         # Retorna o menor inteiro maior ou igual a x
floor(x)        # Retorna o maior inteiro menor ou igual a x
factorial(x)
gcd(a, b)       # Retorna mdc(a, b)
sqrt(x)
sin(x)          # Retorna o valor da funcão seno em radianos
cos(x)          # Retorna o valor da funcão cosseno em radianos
tan(x)          # Retorna o valor da funcão tangente em radianos
degrees(x)      # Converte radianos para graus
radians(x)      # Converte graus para radianos
hypot(x)        # Retorna sqrt(x*x + y*y)
```

####[random][https://docs.python.org/3/library/random.html]
```python
random()                         # Retorna um float em [0.0, 1.0)
choice(seq)                      # Retorna um elemento aleatório de seq
randrange(stop)                  # Retorna um inteiro em [0, stop)
randrange(start, stop[, step])   # Equivalente a choice(range(start, stop[, step]))
shuffle(seq)                     # Embaralha seq (len(seq) não pode ser 0)
sample(population, k)            # Retorna k elementos aleatórios de population	(k não pode ser maior que len(population))
```

####[sys][https://docs.python.org/3/library/sys.html]
```python
argv      # Uma lista com
exit(n)   #
```

Exercícios:
----------

###1. Problema de Monty Hall ([PT][linkpt]/[EN][linken])

Escreva um programa que implemente uma simulação do Problema de Monty Hall.

O jogo consiste no seguinte:

- Monty Hall (o apresentador) apresenta 3 portas ao jogador, sabendo que atrás de uma delas está um carro e que as outras têm cabras.

- O jogador escolhe uma porta (que ainda não é aberta)

- Em seguida Monty abre uma das outras duas portas que o jogador não escolheu (nunca será a porta com o carro)

- Agora com duas portas apenas para escolher e sabendo que o carro está atrás de uma delas, o jogador tem que se decidir se permanece com a porta que escolheu no início do jogo e abre-a ou se muda para a outra porta que ainda está fechada para então a abrir.


O programa deverá receber 2 argumentos pela linha de comando ou pela função `input`: `rounds` (int) e `swap` (bool).

`rounds` determina quantas vezes o jogo será simulado e `swap` determina se o jogador trocará sua escolha após a primeira porta com uma cabra ser aberta.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###2. Ordenação em arquivo


Baixe o arquivo `primes.txt`. Ele contém o primeiro milhão de números primos desordenados e separados por vírgulas.

Abra o arquivo, ordene seus números e salve em outro arquivo.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

###3. Valor do nome

Baixe o arquivo `names.txt`. Ele contém mais de 5000 nomes desordenados.

Ordene-os por ordem alfabética, então aplique o seguinte algoritmo:

- Some o valor todos as letras do nome. (O valor é o índice da letra no alfabeto. O valor de A é 1)
- Multiplique o valor da soma das letras pela posição na lista (o primeiro nome tem posição 1). Este é o valor do nome.

Por exemplo:

COLIN = 3 + 15 + 12 + 9 + 14 = 53

COLIN é o 938º nome da lista, logo o seu valor é 938 × 53 = 49714

Qual a soma do valor de todos os nomes da lista?

<!-- https://projecteuler.net/problem=22 -->


[linkpt]: https://pt.wikipedia.org/wiki/Problema_de_Monty_Hall
[linken]: https://en.wikipedia.org/wiki/Monty_Hall_problem