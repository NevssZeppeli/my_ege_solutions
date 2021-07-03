def f(n):
    print(f'f({n}) called.')
    if n == 0:
        result = 1
    else:
        result = f(n-1) * n
    print(f'f({n}) returning {result}.')
    return result

print(f(5))

def f(n):
    return 1 if n == 0 else f(n-1) * n

print(f(5))
