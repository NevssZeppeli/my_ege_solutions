limit = 133
w = [[(-1 if x + y >= limit else None) for x in range(limit*4)] for y in range(limit*4)]
n = [[(0 if x + y >= limit else None) for x in range(limit*4)] for y in range(limit*4)]

for y in range(limit - 1, 0, -1):
    for x in range(limit - 1 - y, 0, -1):
        w[y][x] = -min(w[y+1][x], w[y][x+1], w[y*4][x], w[y][x*4])
        if w[y][x] == +1: # выиграть хотим поскорее
            n_min = 9999
            for y1, x1 in (y+1, x), (y, x+1), (y*4, x), (y, x*4):
                if w[y1][x1] == -1 and n[y1][x1] < n_min:
                    n_min = n[y1][x1]
            n[y][x] = n_min + 1
        else: # проигрывать хотим подольше
            n[y][x] = max(n[y+1][x], n[y][x+1], n[y*4][x], n[y][x*4])

print('решение 20:')
for s in range(1, limit):
    if n[7][s] == 2 and w[7][s] == +1:
        print(s)
print('решение 21:')
for s in range(1, limit):
    if n[7][s] == 2 and w[7][s] == -1:
        print(s)
