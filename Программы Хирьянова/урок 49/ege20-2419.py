def moves(pos):
    x, y = pos
    return [(x + 3, y),
            (x, y + 3),
            (2*x, y),
            (x, 2*y)]
s = 13  # МОЖНО обойтись ручным перебором
pos0 = (7, s)
pos1_p = moves(pos0)

for pos in pos1_p:
    pos1_v = moves(pos)
    print(pos, pos1_v)
    if all(max(x, y)*2 + min(x, y) >= 62 for x, y in pos1_v):
        print(pos, "подходит!")
    
