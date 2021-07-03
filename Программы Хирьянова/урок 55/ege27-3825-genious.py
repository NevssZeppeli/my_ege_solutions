import sys
sys.stdin = open('27-61b.txt')
# Задача ЕГЭ №27  с сайта К.Ю.Полякова (#3825 в генераторе)
N = int(input())
M = 100
s = [0] + [None]*(M - 1)
for i in range(N):
    # print(*s, sep='\t')  # DEBUG PRINT
    numbers = [0, int(input())]
    s_new = [None]*M
    # вычисляем новые макс.суммы для каждого остатка
    for k in range(M):
        variants = [x + s[(k - x)%M] for x in numbers
                    if s[(k - x)%M] is not None]
        s_new[k] = max(variants) if variants else None
    s[:] = s_new

print(s[50])
