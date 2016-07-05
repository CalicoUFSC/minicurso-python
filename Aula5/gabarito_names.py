namesfile = open('names.txt')

names = namesfile.read().strip('"').split('","')

namesfile.close()

names.sort()

total = 0

for i, name in enumerate(names):
    semitotal = 0
    for char in name:
        # subtrai o valor ascii de char do valor ascii de A e soma 1
        semitotal += ord(char) - ord('A') + 1

    total += semitotal * (i+1)

print(total)