# не эффективно (зато тупо):
def F(n):
    if n > 30:
        return n*n + 5*n + 4
    elif n % 2 == 0:  # чётное
        return F(n+1) + 3*F(n+4)
    else:  # нечётное
        return 2*F(n+2) + F(n+5)

f = [F(n) for n in range(0, 1000+1)]

# эффективно:
F = [None] *(1000+1)
for n in range(31, 1000+1):
    F[n] = n*n + 5*n + 4
for n in range(30, -1, -1):
    if n % 2 == 0:
        F[n] = F[n+1] + 3*F[n+4]
    else:
        F[n] = 2*F[n+2] + F[n+5]

# подытоживание:
count = 0
for n in range(1, 1000+1):
    s = 0
    x = F[n]
    while x != 0:
        s += x % 10
        x //= 10
    if (s == 27):
        count += 1

print(count)
