def spin_words(sentence):
	sentence = sentence.split()
	for i, word in enumerate(sentence):
		if len(word) >= 5:
			sentence[i] = word[::-1]
	return ' '.join(sentence)

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

if __name__ == '__main__':
	f = apply(lambda x: 2*x, 10)

	f = fib_gen()

	for _ in range(200000):
		print(next(f))