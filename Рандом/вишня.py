from itertools import product
c = 0
w = 'ВИШНЯ'
for i in product(w, repeat=6):
    s = ''.join(i)
    if s.count("В") <= 1 and s[0] != 'Ш' and s[-1] != 'И' and s[-1] != 'Я':
        print(s)
        c+=1
print(c)

