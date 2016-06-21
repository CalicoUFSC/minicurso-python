from sys import argv, exit
from random import shuffle, randrange

if len(argv) != 3:
	print('usage: python monty_hall.py <rounds> <swap (y/n)>')

rounds = int(argv[1])
swap = True if argv[2] == 'y' else False

GOAT = 'goat'
CAR = 'car'

doors = [GOAT, GOAT, CAR]

wins = 0

for current_round in range(rounds):
	print('Current try:', current_round)

	shuffle(doors)

	choice = randrange(len(doors))

	print('Chosen door:', choice)

	for i, content in enumerate(doors):
		if i != choice and content == GOAT:
			goat_door = i

	print('A goat was revealed behind door', goat_door)

	if swap:
		for i, _ in enumerate(doors):
			if i != choice and i != goat_door:
				choice = i
				print('Swapping to door', i)
				break
	else:
		print('Did not swap doors')

	if doors[choice] == CAR:
		print('You won!\n')
		wins += 1
	else:
		print('You lost! :(\n')


print('You played', rounds, 'and won', wins)
