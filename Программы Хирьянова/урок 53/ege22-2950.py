for y in range(2, 1000):
    x = y
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a = a + x % 11
        else:
            b = b * (x % 11)
        x = x // 11
    if a == 2 and b == 9:
        print(y)
        break
