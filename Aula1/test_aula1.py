import unittest
import sys

try:
	import aula1
except ImportError:
	print('Erro: o arquivo aula1.py não foi encontrado')
	sys.exit(1)

MAX_PRIMES = 10000

def primes_sieve(limit):
	limitn = limit+1
	not_prime = [False] * limitn
	primes = []

	for i in range(2, limitn):
		if not_prime[i]:
			continue
		for f in range(i*2, limitn, i):
			not_prime[f] = True

		primes.append(i)

	return primes

def fibonacci(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
	return a

def factorial(n):
	for i in range(2, n):
		n *= i
	return n

class TesteAula1(unittest.TestCase):
	@unittest.skipIf('is_prime' not in vars(aula1),
					 'Função "is_prime" não foi encontrada')
	def test_is_prime(self):
		primes = primes_sieve(MAX_PRIMES)

		for i in range(1, MAX_PRIMES):
			if aula1.is_prime(i):
				self.assertEqual(i, primes)
			else:
				self.assertNotIn(i, primes)

	@unittest.skipIf('fibonacci' not in vars(aula1),
					 'Função "fibonacci" não foi encontrada')
	def test_fibonacci(self):
		for i in range(0, 30):
			self.assertEqual(fibonacci(i), aula1.fibonacci(i))

	@unittest.skipIf('factorial' not in vars(aula1),
					 'Função "factorial" não foi encontrada')
	def test_factorial(self):
		for i in range(1, 70):
			self.assertEqual(factorial(i), aula1.factorial(i))

	@unittest.skipIf('to_roman' not in vars(aula1),
					'Função "to_roman" não foi encontrada')
	def test_to_roman(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)