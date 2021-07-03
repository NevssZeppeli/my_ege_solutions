def F(n):
    return (n*n + 4*n + 3 if n > 25 else
            F(n+1) + 2*F(n+4) if n % 3 == 0 else
            F(n+2) + 3*F(n+5))
k = 0
for n in range(1, 1000+1):
    if sum(int(digit) for digit in str(F(n))) == 24:
        k += 1
print(k)
