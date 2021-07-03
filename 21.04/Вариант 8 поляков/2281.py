def f(n):
    if n > 30:
        return(n*n+3*n+5)
    
    if n % 2 == 0 and n <= 30:
        2*f(n+1) + f(n+4)
    if n % 2 != 0 and n <= 30:
        f(n+2) + 3 * f(n+5) 

n = 0
for x in range(1, 1001):
    y = f(x)
    if '00' in y:
        n += 1

print(n)
