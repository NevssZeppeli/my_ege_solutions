begin = None

def insert(x):
	global begin
	begin = [x, begin]


def mprint():
	p = begin
	while p != None:
		data, nxt = p
		print(data)
		p = nxt

for x in range(1, 6):
    insert(x)

mprint()
