#     а) +1 камень;   б) +2 камня;  г) в три раза.
#     Игра завершается, когда камней в куче превышает 64
def pos(x):
    return x + 1, x + 2, 3 * x

GO = 64

w = [-1] * GO * 3
n = [0] * GO * 3
for x in range(GO-1, 0, -1):
    w[x] = -min(w[t] for t in pos(x))
    if w[x] == +1:
        n[x] = 1 + min(n[t] for t in pos(x) if w[t] == -1)
    else:
        n[x] = max(n[t] for t in pos(x))

print('№19:', end=' ')
print(*(x for x in range(1, GO) if w[x] == -1 and n[x] == 1))
print('№20:', end=' ')
print(*(x for x in range(1, GO) if w[x] == +1 and n[x] == 2))
print('№21:', end=' ')
print(*(x for x in range(1, GO) if w[x] == -1 and n[x] == 2))
