class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def greet(self, other):
		return "Hello {}, my name is {}!".format(other, self.name)

	def __add__(self, other):
		return self.age + other.age

	def __lt__(self, other):
		return self.age < other.age

	def __str__(self):
		return self.name

pedro = Person('Pedro', 20)
maria = Person('Maria', 30)

dicionario = { 'Banana' : 5, 'Uva' : 3, 'Goiaba' : 1 }

dicionario['Ameixa'] = 4

del dicionario['Ameixa']

'Uva' in dicionario

for k in dicionario.keys():
	print(k, dicionario[k])