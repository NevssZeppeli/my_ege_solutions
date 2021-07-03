for x in range(1, 10000):
    s = x
    n = 0
    while s + n < 450:
      s = s - 5
      n = n + 25
    if n <= 50:
        print(x)
        break