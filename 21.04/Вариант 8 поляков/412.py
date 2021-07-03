def f(x):
    a = 0 
    b = 0
    y = 1
    while x > 0: 
        if (x % 10) % 2 == 0:
            a = a*10 + x % 10
        else:
            y = y*10 
            b = b*10 + x % 10 
        x = x // 10
    a = a*y + b
    return a
for y in range(10000, 99999):
    if f(y) == 26391:
        print(y)
        break
