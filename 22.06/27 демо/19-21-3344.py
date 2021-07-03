from functools import lru_cache

def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)

@lru_cache(None)
def g(h):
    def next(*condition):
        return (g(m) in condition for m in moves(h))
    a, b = h
    if a + b >= 30: return "W"
    if any(next("W")): return "P1"
    if all(next("P1")): return "V1"
    if any(next("V1")): return "P2"
    if all(next("P1", "P2")): return "V2"

count = 0
count2 = 0
for k in range(1,30):
    for s in range(1,30):
        if g((k,s)) == "V1":
           count+=1
print('19:', count)
print('20:', [s for s in range(1,30) if g((6, s)) == "P2"])
for k in range(1,30):
    for s in range(1,30):
        if g((k,s)) == "V2":
           count2+=1
print('21: ',count2)
