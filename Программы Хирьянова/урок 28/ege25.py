for x in range(174457, 174505 + 1):
    n = 0
    for d in range(2, x):
        if x % d == 0:
            y = d  # remember it
            n += 1
    if n == 2:
        print(x // y, y)

            
