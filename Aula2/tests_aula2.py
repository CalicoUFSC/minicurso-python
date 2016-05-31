import unittest
import sys
from random import randint, shuffle

with open('.gabarito_aula2.py') as file_gabarito:
	global str_gabarito
	str_gabarito = file_gabarito.read()

exec(str_gabarito)

print(remove_duplicates([1,2,2,3,3,4,4,1,2,3,4]))

try:
	import aula2
except ImportError:
	print('Erro: o arquivo aula2.py não foi encontrado')
	sys.exit(1)


class TesteAula2(unittest.TestCase):
	@unittest.skipIf('domain_name' not in vars(aula2),
					 'Função "domain_name" não foi encontrada')
	def test_domain_name(self):
		test_cases = [
			'http://github.com/calicoufsc/minicurso-python',
			'http://www.facebook.com',
			'https://ufsc.br'
		]

		for s in test_cases:
			self.assertEqual(aula2.domain_name(test_cases), domain_name(test_cases))

	@unittest.skipIf('likes' not in vars(aula2),
					 'Função "likes" não foi encontrada')
	def test_likes(self):
		for i in range(10):
			x = map(str, list(range(i)))

			self.assertEqual(aula2.likes, second)

	@unittest.skipIf('remove_duplicates' not in vars(aula2),
					 'Função "remove_duplicates" não foi encontrada')
	def test_remove_duplicates(self):
		for _ in range(40):
			t = [randint(0,5) for _ in range(randint(0, 30))]

			self.assertEqual(aula2.remove_duplicates(t), remove_duplicates(t))

	@unittest.skipIf('different_evenness' not in vars(aula2),
					 'Função "different_evenness" não foi encontrada')
	def test_different_evenness(self):
		for _ in range(40):
		    testlen=randint(3,50)
		    oddeven=randint(0,1)
		    testmat=[randint(0,25)*2+oddeven for x in range(testlen)]
		    solution=randint(1,testlen)
		    testmat[solution-1]+=1
		    testmat=(" ").join(map(str,testmat))
		    self.assertEqual(different_evenness(testmat), solution)

if __name__ == '__main__':
	unittest.main(verbosity=2)