#F(n) = 2*n*n*n + n*n, при n > 25
#F(n) = F(n+2) + 2*F(n+3), при n ≤ 25

def f(n):
    if n > 25:
        return 2*n*n*n + n*n
    if n <= 25:
        return f(n+2) + 2*f(n+3)

print(f(2))
