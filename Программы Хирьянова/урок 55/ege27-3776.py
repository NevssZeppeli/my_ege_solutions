# Задача ЕГЭ №27  с сайта К.Ю.Полякова (#3776 в генераторе)

file = open('27-57a.txt')
N, *data = map(int, file.readlines())
M = 9
data.sort()
stat = [[] for i in range(M)]
for x in data:
    stat[x%M].append(x)
variants = []
for a in range(9):
    for b in range(a, 9):
        for c in range(b, 9):
            d = (0 - a - b - c) % 9
            if d >= c:
                variants.append((a, b, c, d))
#for a, b, c, d in variants:
#    .... NOT TODAY...
    
