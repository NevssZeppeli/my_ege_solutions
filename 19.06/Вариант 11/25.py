count = 0
for x in range(190201, 190260+1):
    sq = int(x ** 0.5)
    d = set()
    for i in range(1, sq+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    d = [i for i in d if i%2==0]
    if len(d) == 4:
        print(sorted(d, reverse=1)[0:2])
