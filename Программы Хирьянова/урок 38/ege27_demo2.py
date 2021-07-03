# Задача https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=2660
import sys
sys.stdin = open('27-b.txt')
N = int(input())  # Вершин будет на 1 больше! Но строк именно N
old_s = [0, -10**10, -10**10]
s = [None, None, None]

for k in range(1, N+1):
    ak, bk = input().split()
    ak, bk = int(ak), int(bk)
    for residual in range(0, 3):
        variant1 = old_s[(residual - ak) % 3] + ak
        variant2 = old_s[(residual - bk) % 3] + bk
        s[residual] = max(variant1, variant2)
    for i in range(0, 3):
        old_s[i] = s[i]

print(max(s[1], s[2]))
