def remove_duplicates(arr):
	for e in arr:
		while arr.count(e) > 1:
			arr.remove(e)
	return arr

def domain_name(url):
	url = url.strip('http://')

	url = url.strip('https://')

	url = url.strip('www.')

	return url[:url.find('.')]

def likes(names):
	if not names:
		return 'Ninguém curtiu isso ainda'
	if len(names) == 1:
		return '{} curtiu isso'.format(names[0])
	if len(names) == 2:
		return '{} e {} curtiram isso'.format(names[0], names[1])
	if len(names) == 3:
		return '{}, {} e {} curtiram isso'.format(names[0], names[1], names[2])

	return '{}, {} e {} outros curtiram isso'.format(names[0], names[1], len(names)-2)


def different_evenness(s):
    n = [int(i) % 2 for i in s.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1