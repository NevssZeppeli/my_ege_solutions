x = 9 ** 9 + 3 ** 21 - 7
n = 0
while x != 0:
    d = x % 3
    if d == 0:
        n += 1
    x //= 3
print(n)
