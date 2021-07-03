from functools import lru_cache
@lru_cache(100000)
def f(x, y):
    if x + y >= 69:
        return 0
    return max(-(lambda x: max(x) if x else float('inf'))([f(xc, yc) for xc, yc in [[x+2, y], [x, y+2], [x*2, y], [x, y*2]] if f(xc, yc) <= 0]) + 1,
               -max([f(xc, yc) for xc, yc in [[x+2, y], [x, y+2], [x*2, y], [x, y*2]]]))
print([f(5, s) for s in range(1, 69)])
