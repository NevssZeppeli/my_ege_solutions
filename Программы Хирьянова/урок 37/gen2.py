def gen(n: int, items: list, prefix: list):
    if n == len(items):  # больше цифр не надо
        print(prefix)
    else:
        gen(n+1, items, prefix + ['-'])
        gen(n+1, items, prefix + [items[n]])

gen(0, list("ABC"), [])
