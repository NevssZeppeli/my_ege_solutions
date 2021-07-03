for x in range(100, 1000):
    n = x
    a = -1
    while n > 7 and a != n % 8:
        a = n % 8
        n //= 8
        if a == n % 8:
            if a == 5:
                print(n)
                break
        else:
            n == 5
            print(n)
            break
