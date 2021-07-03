def f(s):
    n = 10
    while s > n + 20:
      s = s - 6
      n = n + 11
    return n

for x in range(1, 1000):
    if f(x) >= 450:
        print(x)
        break