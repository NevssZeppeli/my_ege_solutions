def f(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    k = f(start, x-1)
    if x % 4 == 0:
        k+= f(start, x//4)
    return k
print(f(1,32))
