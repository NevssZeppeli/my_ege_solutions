from itertools import combinations_with_replacement

a = set([''.join(p) for p in combinations_with_replacement("АБАК", 4)])
for x in a:
    if 'ББ' not in x:
        if 'АА' not in x:

            print(x)
