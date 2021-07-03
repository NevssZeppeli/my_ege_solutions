def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

counter=1

for x in range (2422000, 2422080):
    if IsPrime(x):
        print(counter, x)
        counter+=1