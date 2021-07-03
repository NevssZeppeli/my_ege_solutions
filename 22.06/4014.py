from itertools import product

w = "САКУРА"
c = 0
l = product(w, repeat=5)
a = []
for x in l:
    a.append(''.join(x))
for x in a:
    if x.count('А')<=1 and x.count('У') <= 1:
        c+=1

print(c)
print(a)