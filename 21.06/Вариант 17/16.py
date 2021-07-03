
'''F(n) = n, при n ≤ 3
при n > 3:
  F(n) = n + 3 + F(n–1), при чётном n;
  F(n) = n*n + F(n-2), при нечётном n;'''

def f(n):
    if n <= 3:
        return n
    if n > 3 and n%2==0:
        return n+3 + f(n-1)
    if n > 3 and n%2!=0:
        return n*n + f(n-2)

c = 0
for x in range(1, 1000+1):
    if f(x)%7==0:
        c+=1

print(c)