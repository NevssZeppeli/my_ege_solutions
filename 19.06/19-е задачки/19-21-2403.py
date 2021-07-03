from functools import lru_cache

def moves(h):
    a, b = h
    return (a+2, b), (a, b+2), (a*2, b), (a, b*2)

@lru_cache(None)
def g(h):
    def next(*condition):
        return (g(m) in condition for m in moves(h))
    a, b = h
    if a + b >= 74: return "W"
    if any(next('W')): return "P1"
    if all(next('P1')): return "V1"
    if any(next('V1')): return "P2"
    if all(next('P1', 'P2')): return "V2"

#print('19:', [s for s in range(1, 67) if g((7, s)) == 'V1'])
print('20:', [s for s in range(1, 67) if g((7, s)) == 'P2'])
print('21:', [s for s in range(1, 67) if g((7, s)) == 'V2'])
