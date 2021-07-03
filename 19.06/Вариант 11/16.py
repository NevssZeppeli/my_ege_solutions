#F(n) = 2*n*n*n + 1, при n > 25
#F(n) = F(n+2) + 2*F(n+3), при n ≤ 25
def f(n):
    if n > 25:
        return 2*n*n*n + 1
    if n <= 25:
        return f(n+2) + 2*f(n+3)

count = 0
for x in range(1, 1000+1):
    if f(x)%11 == 0:
        count+=1
print(count)