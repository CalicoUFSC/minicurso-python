import unittest
import sys

try:
	import aula1_resp as aula1
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

def to_roman(n):
	roman = ''

	while n > 999:
		roman = roman + "M"
		n = n - 1000

	if n > 899:
		roman = roman + "CM"
		n = n - 900

	if n > 499:
		roman = roman + "D"
		n = n - 500

	if n > 399:
		roman = roman + "CD"
		n = n - 400

	while n > 99:
		roman = roman + "C"
		n = n - 100

	if n > 89:
		roman = roman + "XC"
		n = n - 90

	if n > 49:
		roman = roman + "L"
		n = n - 50

	if n > 39:
		roman = roman + "XL"
		n = n - 40

	while n > 9:
		roman = roman + "X"
		n = n - 10

	if n > 8:
		roman = roman + "IX"
		n = n - 9

	if n > 4:
		roman = roman + "V"
		n = n - 5

	if n > 3:
		roman = roman + "IV"
		n = n - 4

	while n > 0:
		roman = roman + "I"
		n = n - 1

	return roman

class TesteAula1(unittest.TestCase):
	@unittest.skipIf('is_prime' not in vars(aula1),
					 'Função "is_prime" não foi encontrada')
	def test_is_prime(self):
		primes = primes_sieve(MAX_PRIMES)

		for i in range(1, MAX_PRIMES):
			if aula1.is_prime(i):
				self.assertIn(i, primes)
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
		for i in range(1, 3999):
			self.assertEqual(to_roman(i), aula1.to_roman(i))

if __name__ == '__main__':
	unittest.main(verbosity=2)