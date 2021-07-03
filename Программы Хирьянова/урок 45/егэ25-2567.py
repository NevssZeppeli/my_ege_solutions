for x in range(338472, 338494 + 1):
    divisors = [d for d in range(1, x+1) if x % d == 0]
    if len(divisors) == 4:
        print(divisors[2], divisors[3])
