for x in range(652938, 1744328+1):
    d = set()
    sq = int(x**0.5)
    for i in range(1, sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    if len(d) == 5:
        print(d)