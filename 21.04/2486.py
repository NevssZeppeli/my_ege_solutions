def f (start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    K = f(start, x-1)
    K += f(start, x-2)
    if x % 3 == 0:
        K += f(start, x//3)
    return K

print(f(1,12))
