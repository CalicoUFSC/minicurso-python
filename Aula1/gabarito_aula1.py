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
	if n <= 1:
		return 1
	else:
		return n*factorial(n-1)






while x <= 10:
	if x > 0:
		x = x+1
	else:
		x = 2*x
print('x é maior que 10')




print(10)

print(-12.34)

print(False)

print('hello')

print(10, 'é menor que', 30)



if y:
	print('y é verdadeiro')

if not y:
	print('y é falso')

if y and z:
	print('y e z são verdadeiros')

if y or z:
	print('y ou z é verdadeiro')


while x < 0:
	print('O valor de x é', x)
	x += 1





integer = 10

floatingpoint = 5.5

boolean = True

string = 'hello, world'

none = None



def greet(name):
	print('Hello,', name)

greet('Maria')
greet('João')


def sqrt(n):
	return n**(1/2)

x = sqrt(2)
y = sqrt(3)
z = sqrt(5)


def raiz(base, expoente=2):
	return base**(1/expoente)

x = raiz(2)
y = raiz(3)
z = raiz(5)

