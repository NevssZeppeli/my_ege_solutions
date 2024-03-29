M = 64

def positions(x, y):
    return [(x+3, y), (x*2, y), (x, y+3), (x, y*2)]

w = [[-1]*(2*M) for y in range(2*M)]  # выигрышность позиции
n = [[0]*(2*M) for y in range(2*M)]  # количество ходов до коцна игры

for x in range(M-1, 0, -1):
    for y in range(M-1, 0, -1):
        if x + y >= M:
            continue
        w[x][y] = -min(w[x1][y1] for x1, y1 in positions(x, y))
        if w[x][y] > 0:  # выигрышная
            n[x][y] = 1 + min(n[x1][y1] for x1, y1 in positions(x, y) if w[x1][y1] < 0)
        else: # проигрышная
            n[x][y] = max(n[x1][y1] for x1, y1 in positions(x, y))

print("# 19 задача:", end = ' ')
for s in range(1, 64-7-1):
    # для всех позиций, куда может отправить Петя
    if any(w[x][y] == +1 and n[x][y] == 1 for x, y in positions(7, s)):
        break
print(s)

print("# 20 задача:", end = ' ')
for s in range(1, 64-7-1):
    if w[7][s] == +1 and n[7][s] == 2:
        print(s, end=' ')
print()

print("# 21 задача:", end = ' ')
for s in range(1, 64-7-1):
    if w[7][s] == -1 and n[7][s] == 2:
        print(s)
        break
