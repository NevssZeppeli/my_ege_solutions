def gen(n: int, prefix: list):
    if n == 0:  # больше цифр не надо
        print(prefix)
    else:
        gen(n-1, prefix + [0])
        gen(n-1, prefix + [1])

gen(3, [])
