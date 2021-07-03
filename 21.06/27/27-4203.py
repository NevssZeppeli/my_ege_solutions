f = open('27-69b.txt')
n = int(f.readline())
s = [0]

for i in range(n):
    p = [int(x) for x in f.readline().split()]
    pair = [p[0]+p[1], p[0] + p[2], p[1]+p[2]]
    cmb = [a+b for a in s for b in pair]
    s = {x%10:x for x in sorted(cmb)}.values()
m = max(x for x in s if (x%7==3 and x%10!=5) and (x%7==3 or x%10!=5))
print(m)