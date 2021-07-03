for x in range(190061, 190072 + 1):
    sq = int(x**0.5)
    d = set()
    for i in range(1, x):
        if x%i==0:
            d.add(i)
            d.add(x//i)

    if len(sorted(d)) == 4:
        print(sorted(d))
