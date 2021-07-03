from functools import lru_cache

def moves(h):
    return h+1, h*2

@lru_cache(None)
def g(h):
    def next(*condition):
        return (g(m) in condition for m in moves(h))

    if 20 <= h <= 30: return 'W'
    if h > 30: return "P1"
    if any(next('W')): return 'P1'
    if any(next('P1')): return 'V1'
    if any(next('V1')): return 'P2'
    if all(next('P1', 'P2')): return 'V2'

print([s for s in range(1, 20) if g(s) == "V1"]) # для этого условия надо поставить any в 14 строке, а потом поменять на all для 20-21
print([s for s in range(1, 20) if g(s) == "P2"])
print([s for s in range(1, 20) if g(s) == "V2"])
'''
Ответ:
5
9 17
16
'''