import sys
sys.stdin = open('27-4b.txt')
# Задача ЕГЭ №27  с сайта К.Ю.Полякова (#2664 в генераторе)
N = int(input())
M = 5
s = [0] + [None]*(M - 1)
for i in range(N):
    # print(*s, sep='\t')  # DEBUG PRINT
    numbers = [int(x) for x in input().split()]
    s_new = [None]*M
    # вычисляем новые макс.суммы для каждого остатка
    for k in range(M):
        variants = [x + s[(k - x)%5] for x in numbers
                    if s[(k - x)%5] is not None]
        s_new[k] = max(variants) if variants else None
    s[:] = s_new
print(*s, sep='\t')
