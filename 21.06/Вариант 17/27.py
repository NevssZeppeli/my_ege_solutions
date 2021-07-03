f = open('27-17a.txt')
n = int(f.readline())
k = 0
d = [0] * 26

q = [int(f.readline()) for i in range(4)]
for _ in range(n-4):
    x = int(f.readline())
    for y in range(26):
        if (x*y)%26==0 and (x+y)%2!=0:
            k+=d[y]
    d[q[0]%26] += 1
    q.pop(0)
    q.append(x)
print(k)