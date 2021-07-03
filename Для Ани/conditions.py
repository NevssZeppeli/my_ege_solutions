# Задача №112162. Сколько дней в месяце

n = int(input())

def month(n):
    if n in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if n == 2:
        return 28
    if n < 1 or n > 12:
        return 0
    return 30

print(month(n))