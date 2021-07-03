W = [[None]*62 for s in range(0, 62)]
T = [[None]*62 for s in range(0, 62)]

def moves(x, y):
    return [(x+3, y), (x*2, y), (x, y+3), (x, y*2)]
    
def win_rate(x, y):
    if x + y >= 62:
        return -1
    if W[x][y] is None:
        W[x][y] = -min(win_rate(x1, y1) for x1, y1 in moves(x, y))
    return W[x][y]

def turns_to_end(x, y):
    if x + y >= 62:
        return 0
    if T[x][y] is None:
        if win_rate(x, y) > 0:
            m = min(turns_to_end(x1, y1) for x1, y1 in
                    moves(x, y) if win_rate(x1, y1) < 0)
        else:
            m = max(turns_to_end(x1, y1) for x1, y1 in
                    moves(x, y))
        T[x][y] = m + 1
    return T[x][y]

for s in range(1, 61):
    if turns_to_end(7, s) == 3:
        print(s, "Петя за 2 хода")
for s in range(1, 61):
    if turns_to_end(7, s) == 4:
        print(s, "Ваня за 2 хода")



