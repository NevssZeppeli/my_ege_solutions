q = 0
n = int(input())
for i in range(1, n):
    if n % i == 0:
        q = i
print(q)