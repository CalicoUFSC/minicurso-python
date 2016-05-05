import unittest
import aula1
import sys

from pprint import pprint

MAX_PRIMES = 10000


def primes_sieve(limit):
	""" Returns  a list of primes < n """
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
	def test_primo(self):
		primes = primes_sieve(MAX_PRIMES)

		for i in range(1, MAX_PRIMES):
			if aula1.is_prime(i):
				self.assertIn(i, primes)
			else:
				self.assertNotIn(i, primes)

	def test_fibonacci(self):
		for i in range(0, 20):
			self.assertEqual(fibonacci(i), aula1.fibonacci(i))

	def test_factorial(self):
		for i in range(1, 70):
			self.assertEqual(factorial(i), aula1.factorial(i))

	@unittest.skipIf('to_roman' not in vars(aula1),
					 'o desafio não foi encontrado, logo não será testado')
	def test_to_roman(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)