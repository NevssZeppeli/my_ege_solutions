# Задача https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=2660
import sys
sys.stdin = open('27-b.txt')
N = int(input())  # Вершин будет на 1 больше! Но строк именно N
s = [[0, -10**10, -10**10]] + [[None, None, None] for i in range(N)]

for k in range(1, N+1):
    ak, bk = input().split()
    ak, bk = int(ak), int(bk)
    for residual in range(0, 3):
        variant1 = s[k-1][(residual - ak) % 3] + ak
        variant2 = s[k-1][(residual - bk) % 3] + bk
        s[k][residual] = max(variant1, variant2)

print(max(s[N][1], s[N][2]))
