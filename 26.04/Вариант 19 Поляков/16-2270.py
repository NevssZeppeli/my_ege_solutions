import sys
sys.setrecursionlimit(5000)

def f(n):
    if n <= 3:
        return n
    
    if n > 3 and n % 2 == 0:
        return n + f(n-1)
    if n > 3 and n % 2 != 0:
        return n*n + f(n-2)
    
c = 0
for x in range(1, 10000):
    if f(x) < 10**8:
        c+=1
print(c)
