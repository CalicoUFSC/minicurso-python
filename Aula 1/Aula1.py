# Aula 1 - Tipos primitivos, Estruturas e Funcões
#
# ====================================== Notas de aula ================================================

# Bem vindos à primeira aula de Python. Nela abordaremos os tipos
# primitivos disponíveis na linguagem, como utilizá-los, como
# mostrá-los na tela e como pedimos externamente o valor de um
# tipo primitivo e armazenamos esse valor, estruturas de controle
# (if, else), estruturas de repetição (for, while) e funções


#========================================================================================================
#========================================================================================================

# Variáveis

# Tipos primitivos

	# Strings: 
	palavra

	# Tipos numéricos:
	inteiro
	decimal 
	booleano

	# Outros:
	listas
	dicionarios

# Print/input

	print()
	input()
	raw_input()

#========================================================================================================
#========================================================================================================

# Estruturas de controle
	
	if :
		pass

	else

# Estruturas de repeticão

	for x in xrange(1,10):
		pass

	while :
		pass


#========================================================================================================
#========================================================================================================

# Funcões
	
	def nomeDaFuncao1 (parametros1):

		# comportamento

	def nomeDaFuncao2 (parametros2):

		# comportamento


	# Exemplo: Função Fibonacci

	def fib2(n): 
 	#Retorna a lista contendo a serie de Fibonacci ate n

		result = []
	     a, b = 0, 1
		
		while b < n:
			
			result.append(b)
			a, b = b, a + b
		
		return result

#========================================================================================================
#========================================================================================================

# Exercício: algarismos romanos

# Fazer um programa que escreva a representação em algarismos romanos de um número inteiro positivo.
# O usuário deve entrar com um número (input) e o resultado deve ser impresso no console (print).
	
# 	Exemplo de execução:
# 		- Entre com um numero positivo: 
# 			1985
# 		- Em algarismos romanos:
# 			MCMLXXXV

#========================================================================================================

# Exercício: números primos

# 	Um número natural é primo se é divisível apenas por si mesmo ou pela unidade.
# 	Isto sugere o seguinte algoritmo:

# 		Se o número é 1, então não é primo.
# 		Se o número é 2, então é primo.
# 		Caso contrário,
# 		Seja 'd' um possível divisor, cujo valor é inicialmente 2.

# 		Repetir:
		
# 		Se o resto da divisão do número por 'd' é zero, então o número não é primo.
# 		Caso contrário,
# 		Incrementar 'd'.
# 		Se 'd' é igual ou maior que o número, então terminar repetição diagnosticando o número como primo


#========================================================================================================
#========================================================================================================
#========================================================================================================
