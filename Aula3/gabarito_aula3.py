def spin_words(sentence):
	sentence = sentence.split()
	for i, word in enumerate(sentence):
		if len(word) >= 5:
			sentence[i] = word[::-1]
	return ' '.join(sentence)

def zip(lista):
	menor_len = min([len(lst) for lst in lista])

	for i in range(menor_len):
		yield [lst[i] for lst in lista]

def apply(f, n):
	def func(x):
		h = f(x)
		for _ in range(n-1):
			h = f(h)
		return h
	return func

def fib_gen():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b

def add_by(x):
	def func(y):
		return x+y