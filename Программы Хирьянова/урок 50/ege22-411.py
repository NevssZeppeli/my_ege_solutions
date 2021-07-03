for X in range(10000, 100000):
    x = X
    a = 0 
    b = 0
    while x > 0: 
        y = x % 10
        if y > 3: a = a + 1
        if y < 8: b = b + 1
        x = x // 10
    if a == 4 and b == 2:
        print(X)
        break
