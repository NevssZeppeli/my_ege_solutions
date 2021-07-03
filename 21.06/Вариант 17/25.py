for x in range(394441, 394505+1):
    sq = int(x**0.5)
    d = set()
    for i in range(1, sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    print(x, len(d))
