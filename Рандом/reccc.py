def G(n):
    print(n+2)
    if n > 1:
        print(n+6)
        G(n-1)
        G(n-2)

G(1000)
