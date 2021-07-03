from itertools import *
C = starmap(chain, (permutations([a, b, 'К']) for a, b in product('ШОЛА', 'ШОЛА')))
print(set(C))
print(len(set(C)))
