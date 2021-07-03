n = 0
for x in range(100, 100001):
    divs = []
    y = x
    d = 2
    while y != 1:
        if y % d == 0:
            divs.append(d)
            while y % d == 0:
                y //= d
        d += 1
    if len(divs) == 3:
        #print(x, divs)
        n += 1
print(n)
