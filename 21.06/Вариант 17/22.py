for x in range(100, 1000):
    L = x - 18
    M = x + 36
    while L != M:
      if L > M:
        L = L - M
      else:
        M = M - L
    if M == 9:
        print(x)
        break