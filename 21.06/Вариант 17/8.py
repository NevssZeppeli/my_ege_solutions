from itertools import product

s = 'КОМЕТА'
res = []
for p in product(s, repeat=6):
    a = ''.join(p)
    if 'ОА' not in a and 'АО' not in a and 'ЕО' not in a and 'ОЕ' not in a and  'ЕА' not in a and  'АЕ' not in a:
        print(a)