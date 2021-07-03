from functools import lru_cache

def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)

@lru_cache(None)
def g(h):
    a, b = h
    if a + b >= 53: return "W"
    if any(g(m) == "W" for m in moves(h)): return "P1"
    if all(g(m) == "P1" for m in moves(h)): return "V1"
    if any(g(m) == "V1" for m in moves(h)): return "P2"
    if all(g(m) == "P1" or g(m) == "P2" for m in moves(h)): return "V2"

print([s for s in range(1, 44) if g((9,s)) == "V1"])
print([s for s in range(1, 44) if g((9,s)) == "P2"])
print(len([s for s in range(1, 44) if g((9,s)) == "V2"]))
