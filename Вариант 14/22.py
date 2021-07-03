def f(x):
    L = x - 12
    M = x + 12
    while L != M:
      if L > M:
        L = L - M
      else:
        M = M - L
    return (M)

for x in range(100, 1000):
    if(f(x) == 2):
        print(x)