def f(s):
    n = 1
    while n < 21:
        s = s - 1
        n = n + 2
    if s > 600:
        return s

for x in range(1, 1000):
    print(f(x))
    
