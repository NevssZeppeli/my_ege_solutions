N = int(input())  # Вершин будет на 1 больше! Но строк именно N
t = int(input())
tA = 0
tB = t
for k in range(1, N+1):
    ak, bk = input().split()
    ak, bk = int(ak), int(bk)
    tA += ak
    tB = min(tB + bk, tA + t)
print(tB)
