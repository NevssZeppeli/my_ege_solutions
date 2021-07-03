f = open('27-B.txt')
n = int(f.readline())
s = [0]

for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    cmb = [a+b for a in s for b in pair]
    s = {x%10:x for x in sorted(cmb)}.values()

m = max(x for x in s if x%3!=0)
print(m)