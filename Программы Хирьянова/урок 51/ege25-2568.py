for x in range(164700, 164752+1):
	divs = []
	for d in range(2, x + 1):
		if x % d == 0:
			divs.append(d)
	if len(divs) == 6:
		print(divs[-1], x)
