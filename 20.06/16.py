def f(n):
    if n > 20:
        return n*n*n + n
    if n <= 20 and n%2==0:
        return 3*f(n+1) + f(n+3)
    if n <= 20 and n%2!=0:
        return f(n+2) + 2*f(n+3)

a = []
for x in range(1, 1000+1):
    y = f(x)
    if '1' not in str(y):
        a.append(x)
print(len(a))
