def f(n):
    y = oct(n)
    x = str(n)[::-1]
    print(x)
    z = int(x, 0)
    print(z)
    return n - z

print(f(255))

