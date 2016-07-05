inputfile = open('primes.txt')

lista = inputfile.read().split(',')

inputfile.close()

lista = sorted([int(i) for i in lista])

outputfile = open('primes_sorted.txt', 'w')

for i in lista:
	outputfile.write(str(i)+',')
