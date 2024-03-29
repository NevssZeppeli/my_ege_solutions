from functools import lru_cache

def moves(h):
    a, b = h
    return (a+2, b), (a, b+2), (a*2, b), (a, b*2)

@lru_cache(None)
def g(h):
    def next(*cond):
        return (g(m) in cond for m in moves(h))
    a, b = h
    if a + b >= 82: return 'W'
    if any(next('W')): return 'P1'
    if all(next('P1')): return 'V1'
    if any(next('V1')): return 'P2'
    if all(next('P1', 'P2')): return 'V2'
#print([s for s in range(1,73) if g((9,s)) == "V1"])
print([s for s in range(1,73) if g((9,s)) == "P2"])
print([s for s in range(1,73) if g((9,s)) == "V2"])