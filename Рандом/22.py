for y in range(0, 100000):
    x = y
    a = 0
    b = 0
    while x > 0:
        a += 1
        if b < (x % 7):
            b = x % 7
        x //= 7
    if a == 4 and b == 5:
        print(y)
