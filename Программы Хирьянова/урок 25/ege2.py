def f(x, y, z, w):
    return bool((x or y)) and not (y == z) and not w


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                result = f(x, y, z, w)
                if result:
                    print(x, y, z, w, result)
