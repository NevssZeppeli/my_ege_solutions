f = open('27.txt')
n = int(f.readline())

s = [ [0, 0] ]
mx = 0
l = 0

for i in range(n):
    x = int(f.readline())
    cmb = [[a+x, b+1] for a,b in s] + [[x,1]]
    s = {x[0]%73:x for x in sorted(cmb, key=lambda x:x[0])}.values()
    for a, b in s:
        if a%73==0:
            if a>mx:
                mx = x
                l = b
            if a == mx and b < 1:
                l = b
print(l)