for x in range(0, 1000):
    s = x
    n = 200
    while s // n >= 2:
      s = s + 5
      n = n + 5
    if len(str(s)) == 3:
        print(x)
