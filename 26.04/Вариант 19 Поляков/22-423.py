for y in range(101, 10000):
    x = y
    L = x - 16
    M = x + 32
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 4:
        print(y)
        break
