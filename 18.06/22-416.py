for y in range(1, 10000):
    x = y
    a = 1
    b = 10
    while x > 0:
      c = x % 10
      a = a*c
      if c < b: b = c
      x = x // 10
    if (a == 45) and (b == 5):
        print(y)
        break