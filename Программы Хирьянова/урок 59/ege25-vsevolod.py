primes = [x for x in range(3, 80) if all(x % d != 0 for d in range(2, x))]

A = []
for p in primes:
    x = p ** 4
    while x < 35000000:
        x *= 2
    while x <= 40000000:
        A.append(x)
        x *= 2
A.sort()
for x in A:
    print(x)
