from math import isqrt
for x in range(10**6, 2*10**6 + 1):
    divs = []
    for a in range(isqrt(x+2500)-50, isqrt(x) + 1):
        if x % a == 0:
            b = x // a
            if b - a <= 100:
                divs.append(a)
    if len(divs) == 3:
        print(x)
1