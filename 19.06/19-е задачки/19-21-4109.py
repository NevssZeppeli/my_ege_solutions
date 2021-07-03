from functools import lru_cache

def moves(h):
    return h+1, h*3

@lru_cache(None)
def g(h):
    def next(*condition):
        return (g(m) in condition for m in moves(h))

    if 65 <= h <=  100: return "W"
    if h > 100: return "P1"

    if any(next("W")): return "P1"
    if all(next("P1")): return "V1"
    if any(next("V1")): return "P2"
    if all(next("P1", "P2")): return "V2"

print([s for s in range(1, 65) if g(s) == "P2"])
print([s for s in range(1, 65) if g(s) == "V2"])
