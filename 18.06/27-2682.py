f = open('27-22a.txt')
n = int(f.readline())
s = [0]

for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    cmb = [a+b for a in s for b in pair]
    s = {x%10:x for x in sorted(cmb, reverse=True)}.values()

m = min(x for x in s if x%10 == 4)
print(m)
