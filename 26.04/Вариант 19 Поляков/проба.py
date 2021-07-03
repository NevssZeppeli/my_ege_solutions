# Задача ЕГЭ №27  с сайта К.Ю.Полякова (#3930 в генераторе)
file = open('27-15b.txt')
N = int(file.readline())
M = 14  # Интересует делимость на 9.
K = 6  # Сумма должна состять ровно из 4 чисел.
s = [[None]*M for i in range(K + 1)]
s[0][0] = 0  # сумма из 0 чисел с 0 остатком - допустима
for i in range(N):
    x = int(file.readline())
    s_new = [[None]*M for i in range(K + 1)]
    s_new[0][0] = 0
    # вычисляем новые мин.суммы для каждого остатка
    # и каждого числа использованных чисел
    for n in range(1, K+1):
        for m in range(M):
            variants = []
            if s[n][m] is not None:  # если не использовать число
                variants.append(s[n][m])  # остаток не меняется, число чисел не растёт
            if s[n-1][(m - x)%M] is not None:
                variants.append(x + s[n-1][(m - x)%M])
            s_new[n][m] = max(variants) if variants else None
    s = s_new
print(max(s[4][m] for m in range(1, M)))# Задача ЕГЭ №27  с сайта К.Ю.Полякова (#3930 в генераторе)
