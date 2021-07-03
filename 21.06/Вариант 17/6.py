for x in range(1, 10000):
    s = x
    remember = s
    n = 40
    while s + n < 100:
      s = s + 25
      n = n - 5
    if s == remember:
        print(x)