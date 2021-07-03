def gen(n: int, pairs: list, prefix: list):
    if n == len(pairs):  # больше цифр не надо
        print(prefix)
    else:
        gen(n+1, pairs, prefix + [pairs[n][0]])
        gen(n+1, pairs, prefix + [pairs[n][1]])

gen(0, list(zip("ABCD", "abcd")), [])
