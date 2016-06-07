import unittest
import sys
import gabarito_aula3 as gabarito
from random import randint, shuffle

try:
	import aula3
except ImportError:
	print('Erro: o arquivo aula3.py não foi encontrado')
	sys.exit(1)


class TesteAula3(unittest.TestCase):
	@unittest.skipIf('domain_name' not in vars(aula3),
					 'Função "domain_name" não foi encontrada')
	def test_domain_name(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)