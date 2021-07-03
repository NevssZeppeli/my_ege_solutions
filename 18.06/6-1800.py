for x in range(1, 1000):
    s = x
    n = 80
    while s + n < 160:
      s = s + 15
      n = n - 10
    if s <= 100:
        print(x)