for x in range(0, 100000):
    s = x
    n = 5
    while s > 5:
      s = s // 2
      n = n + 4
    if n == 29:
        print(n, x)