x = int(input())
A = []
d = 2
while x != 1:
    if x % d == 0:
        A.append(d) # празднуем нахождение очередного делителя
        x //= d  # x = x // d
    else:  # не поделился x на d нацело...
        d += 1  # что ж, пробуем следующее число
print(A)
print(*A)
