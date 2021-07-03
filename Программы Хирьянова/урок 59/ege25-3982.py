A = []
for m in range(1, 28+1, 2):
    for n in range(0, 10+1, 2):
        x = 2**m * 7**n
        if 100000000 <= x <= 300000000:
            A.append((x, m + n))

A.sort()
for x, mn in A:
    print(x, mn)
    
