limit = 69
W = [[-1]*(limit*2) for i in range(limit*2)]
T = [[0]*(limit*2) for i in range(limit*2)]
for i in range(limit-1, 0, -1):
    for k in range(limit - 1 - i, 0, -1):
        assert i + k < limit
        turns = [(i+2, k), (i*2, k), (i, k+2), (i, k*2)]
        W[i][k] = -min(W[x][y] for x, y in turns)
        if W[i][k] <= 0:
            T[i][k] = 1 + max(T[x][y] for x, y in turns)
        else:
            T[i][k] = 1 + min(T[x][y] for x, y in turns
                              if W[x][y] < 0)
print('выигрышная двухходовка от (5, s): s=', T[5].index(3))
for k in range(1, limit):
    if T[5][k] == 4:
        print('проигрышная двухходовка от (5, s): s =', k)
print(T[5])
