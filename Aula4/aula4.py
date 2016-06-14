def add(x):
	def func(y):
		return x+y
	return func

increment = add(1)

addFive = add(5)

print(increment(3))

def aplicar(f, x):
	return f(x)


def quadrado(x):
	return x**2

print(aplicar(quadrado, 3))