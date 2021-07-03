# last recently used cache:
from functools import lru_cache

M = 41

def positions(x, y):
    return [(x+1, y), (x*2, y), (x, y+1), (x, y*2)]

@lru_cache(maxsize=1000)
def win_rate(x: int, y: int):
    if x + y >= M:
        return -1
    else:
        return -min(win_rate(x1, y1) for x1, y1 in positions(x, y))

@lru_cache(maxsize=1000)
def moves_number(x: int, y: int):
    if x + y >= M:
        return 0
    elif win_rate(x, y) == +1:
        return 1 + min(moves_number(*pos) for pos in positions(x, y)
                       if win_rate(*pos) < 0)
    else:  # проигрышная
        return max(moves_number(*pos) for pos in positions(x, y))


print("# 19 задача:", end = ' ')
for s in range(1, 41-9-1):
    # для всех позиций, куда может отправить Петя
    if any(win_rate(x, y) == +1 and
           moves_number(x, y) == 1 for x, y in positions(9, s)):
        break
print(s)

print("# 20 задача:", end = ' ')
for s in range(1, 41-9-1):
    if win_rate(9, s) == +1 and moves_number(9, s) == 2:
        print(s, end=' ')
print()

print("# 21 задача:", end = ' ')
for s in range(1, 41-9-1):
    if win_rate(9, s) == -1 and moves_number(9, s) == 2:
        print(s)
        break
