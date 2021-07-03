# Задача №112182. Двоичный код

n = int(input())

def octa(n):
    res = ''
    flag = True
    if n == 0:
        print(n)
    if n < 0:
        flag = False
        n = -n
    while n > 0:
        res = str(n % 8) + res
        n //= 8
    if not flag:
        res = '-' + res
        print(res)
    else:
        print(res)

octa(n)