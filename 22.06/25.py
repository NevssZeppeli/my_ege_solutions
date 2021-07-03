def isPrime(x):
    sq = int(x**0.5)
    for i in range(1, sq+1):
        if x%i == True:
            return False
    return True

print([x for x in range(2422000, 2422080+1) if isPrime(x)])

