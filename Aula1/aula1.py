def is_prime(n):
	if n == 1:
		return False

	if n == 2:
		return True

	for d in range(2, n):
		if n % d == 0:
			return False

	return True

def fibonacci(n):
	a, b = 0, 1

	for i in range(n):
		a, b = b, a+b

	return a

def factorial(n):
	for i in range(2, n):
		n = n*i
	return n