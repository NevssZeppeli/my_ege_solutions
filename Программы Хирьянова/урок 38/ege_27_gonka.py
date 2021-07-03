N = int(input())  # Вершин будет на 1 больше! Но строк именно N
t = int(input())
tA = [0] + [None] * N
tB = [t] + [None] * N
for k in range(1, N+1):
    ak, bk = input().split()
    ak, bk = int(ak), int(bk)
    tA[k] = tA[k-1] + ak
    tB[k] = min(tB[k-1] + bk,
                tA[k] + t)
print(tB[N])
